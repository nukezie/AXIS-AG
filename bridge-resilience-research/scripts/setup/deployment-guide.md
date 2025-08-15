# Deployment Guide for Bridge Access Resilience Testing Environment

**Document Classification:** RESTRICTED  
**Version:** 1.0  
**Date:** [Current Date]  

## Deployment Overview

This guide provides step-by-step instructions for deploying the bridge access resilience testing environment in controlled lab environments. The deployment includes all necessary components for bridge entry relays, impairment tools, telemetry collection, and monitoring systems.

## Prerequisites

### Hardware Requirements
- **Minimum:** 4 servers with 16GB RAM, 8 CPU cores each
- **Recommended:** 8 servers with 32GB RAM, 16 CPU cores each
- **Storage:** 1TB SSD per server for data collection
- **Network:** 10Gbps network interfaces for high-throughput testing

### Software Requirements
- **Operating System:** Ubuntu 20.04 LTS or CentOS 8
- **Container Runtime:** Docker 20.10+ or Kubernetes 1.21+
- **Database:** PostgreSQL 13+ or InfluxDB 2.0+
- **Monitoring:** Prometheus 2.30+ and Grafana 8.0+

### Security Requirements
- **Network Isolation:** Dedicated lab network segment
- **Access Control:** VPN access with multi-factor authentication
- **Encryption:** TLS 1.3 for all communications
- **Audit Logging:** Comprehensive logging of all activities

## Deployment Architecture

### Component Layout
```
[Border Gateway] → [Load Balancer] → [Relay Nodes] → [Impairment Layer] → [Core Services]
                                                      ↓
[Monitoring Stack] ← [Telemetry Collection] ← [Data Processing] ← [Analysis Engine]
```

### Network Segments
- **Segment 1:** External interface and border gateway
- **Segment 2:** Relay infrastructure and load balancing
- **Segment 3:** Core testing environment and impairment tools
- **Segment 4:** Monitoring and data storage

## Deployment Steps

### Phase 1: Infrastructure Setup

#### Step 1.1: Network Configuration
```bash
# Configure network interfaces
sudo ip link set eth0 up
sudo ip addr add 192.168.1.10/24 dev eth0
sudo ip route add default via 192.168.1.1

# Configure firewall rules
sudo ufw enable
sudo ufw allow 22/tcp  # SSH
sudo ufw allow 80/tcp  # HTTP
sudo ufw allow 443/tcp # HTTPS
sudo ufw allow 8080/tcp # Application ports
```

#### Step 1.2: System Preparation
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y docker.io docker-compose curl wget git

# Configure Docker
sudo usermod -aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker
```

#### Step 1.3: Security Hardening
```bash
# Configure SSH security
sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart ssh

# Install security tools
sudo apt install -y fail2ban ufw
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

### Phase 2: Core Services Deployment

#### Step 2.1: Database Setup
```bash
# Create database directory
sudo mkdir -p /opt/bridge-resilience/data/postgres
sudo chown 999:999 /opt/bridge-resilience/data/postgres

# Deploy PostgreSQL
cat > docker-compose-db.yml << EOF
version: '3.8'
services:
  postgres:
    image: postgres:13
    container_name: bridge-postgres
    environment:
      POSTGRES_DB: bridge_resilience
      POSTGRES_USER: bridge_user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - /opt/bridge-resilience/data/postgres:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    restart: unless-stopped
EOF

docker-compose -f docker-compose-db.yml up -d
```

#### Step 2.2: Monitoring Stack
```bash
# Deploy Prometheus
cat > docker-compose-monitoring.yml << EOF
version: '3.8'
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: bridge-prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./config/prometheus.yml:/etc/prometheus/prometheus.yml
      - /opt/bridge-resilience/data/prometheus:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: bridge-grafana
    ports:
      - "3000:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_PASSWORD}
    volumes:
      - /opt/bridge-resilience/data/grafana:/var/lib/grafana
    restart: unless-stopped
EOF

docker-compose -f docker-compose-monitoring.yml up -d
```

### Phase 3: Bridge Access Components

#### Step 3.1: Relay Node Deployment
```bash
# Create relay node configuration
cat > docker-compose-relays.yml << EOF
version: '3.8'
services:
  relay-node-1:
    image: bridge-resilience/relay:latest
    container_name: bridge-relay-1
    environment:
      NODE_ID: relay-1
      RELAY_PORT: 8081
      AUTH_TOKEN: ${RELAY_AUTH_TOKEN}
    ports:
      - "8081:8081"
    volumes:
      - ./config/relay:/etc/relay
    restart: unless-stopped

  relay-node-2:
    image: bridge-resilience/relay:latest
    container_name: bridge-relay-2
    environment:
      NODE_ID: relay-2
      RELAY_PORT: 8082
      AUTH_TOKEN: ${RELAY_AUTH_TOKEN}
    ports:
      - "8082:8082"
    volumes:
      - ./config/relay:/etc/relay
    restart: unless-stopped
EOF

docker-compose -f docker-compose-relays.yml up -d
```

#### Step 3.2: Load Balancer Configuration
```bash
# Deploy HAProxy load balancer
cat > docker-compose-lb.yml << EOF
version: '3.8'
services:
  haproxy:
    image: haproxy:latest
    container_name: bridge-haproxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./config/haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    restart: unless-stopped
EOF

docker-compose -f docker-compose-lb.yml up -d
```

### Phase 4: Impairment Tools Deployment

#### Step 4.1: ToxiProxy Setup
```bash
# Deploy ToxiProxy for network impairment
cat > docker-compose-toxiproxy.yml << EOF
version: '3.8'
services:
  toxiproxy:
    image: shopify/toxiproxy:latest
    container_name: bridge-toxiproxy
    ports:
      - "8474:8474"
    volumes:
      - ./config/toxiproxy.json:/etc/toxiproxy.json
    restart: unless-stopped
EOF

docker-compose -f docker-compose-toxiproxy.yml up -d
```

#### Step 4.2: Network Impairment Tools
```bash
# Install tc/netem tools
sudo apt install -y iproute2

# Configure network impairment scripts
cat > /opt/bridge-resilience/scripts/impairment/latency.sh << 'EOF'
#!/bin/bash
# Add latency impairment
sudo tc qdisc add dev eth0 root netem delay ${1}ms
EOF

cat > /opt/bridge-resilience/scripts/impairment/packet-loss.sh << 'EOF'
#!/bin/bash
# Add packet loss impairment
sudo tc qdisc add dev eth0 root netem loss ${1}%
EOF

chmod +x /opt/bridge-resilience/scripts/impairment/*.sh
```

### Phase 5: Telemetry and Analysis

#### Step 5.1: Telemetry Collection
```bash
# Deploy telemetry collector
cat > docker-compose-telemetry.yml << EOF
version: '3.8'
services:
  telemetry-collector:
    image: bridge-resilience/telemetry:latest
    container_name: bridge-telemetry
    environment:
      DATABASE_URL: postgresql://bridge_user:${DB_PASSWORD}@postgres:5432/bridge_resilience
      PROMETHEUS_URL: http://prometheus:9090
    volumes:
      - ./config/telemetry:/etc/telemetry
    restart: unless-stopped
EOF

docker-compose -f docker-compose-telemetry.yml up -d
```

#### Step 5.2: Analysis Engine
```bash
# Deploy analysis engine
cat > docker-compose-analysis.yml << EOF
version: '3.8'
services:
  analysis-engine:
    image: bridge-resilience/analysis:latest
    container_name: bridge-analysis
    environment:
      DATABASE_URL: postgresql://bridge_user:${DB_PASSWORD}@postgres:5432/bridge_resilience
      SLO_CONFIG: /etc/analysis/slo-config.json
    volumes:
      - ./config/analysis:/etc/analysis
    restart: unless-stopped
EOF

docker-compose -f docker-compose-analysis.yml up -d
```

## Configuration Files

### Environment Variables
Create `.env` file with the following variables:
```bash
# Database Configuration
DB_PASSWORD=secure_password_here
DB_HOST=localhost
DB_PORT=5432

# Monitoring Configuration
GRAFANA_PASSWORD=secure_grafana_password
PROMETHEUS_RETENTION=30d

# Relay Configuration
RELAY_AUTH_TOKEN=secure_auth_token_here
RELAY_NODES=2

# Security Configuration
ENCRYPTION_KEY=secure_encryption_key_here
JWT_SECRET=secure_jwt_secret_here
```

### Prometheus Configuration
```yaml
# config/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "bridge_rules.yml"

scrape_configs:
  - job_name: 'bridge-relays'
    static_configs:
      - targets: ['relay-node-1:8081', 'relay-node-2:8082']

  - job_name: 'bridge-telemetry'
    static_configs:
      - targets: ['telemetry-collector:8080']

  - job_name: 'bridge-analysis'
    static_configs:
      - targets: ['analysis-engine:8080']
```

## Verification and Testing

### Health Checks
```bash
# Check all services are running
docker ps

# Verify database connectivity
docker exec bridge-postgres psql -U bridge_user -d bridge_resilience -c "SELECT version();"

# Check monitoring stack
curl http://localhost:9090/api/v1/status/targets
curl http://localhost:3000/api/health

# Test relay nodes
curl http://localhost:8081/health
curl http://localhost:8082/health
```

### Baseline Testing
```bash
# Run baseline performance tests
./scripts/testing/baseline-test.sh

# Verify SLO measurements
./scripts/testing/slo-verification.sh

# Test impairment tools
./scripts/testing/impairment-test.sh
```

## Security Hardening

### Network Security
```bash
# Configure firewall rules
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 192.168.1.0/24 to any port 22
sudo ufw allow from 192.168.1.0/24 to any port 80
sudo ufw allow from 192.168.1.0/24 to any port 443
sudo ufw enable
```

### Container Security
```bash
# Run containers with security options
docker run --security-opt=no-new-privileges \
           --cap-drop=ALL \
           --read-only \
           -v /tmp:/tmp:rw \
           your-image
```

### Data Encryption
```bash
# Encrypt sensitive data
echo "sensitive_data" | openssl enc -aes-256-cbc -salt -out encrypted.txt

# Configure TLS certificates
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

## Maintenance Procedures

### Backup Procedures
```bash
# Database backup
docker exec bridge-postgres pg_dump -U bridge_user bridge_resilience > backup.sql

# Configuration backup
tar -czf config-backup.tar.gz ./config/

# Data backup
tar -czf data-backup.tar.gz /opt/bridge-resilience/data/
```

### Update Procedures
```bash
# Update containers
docker-compose pull
docker-compose up -d

# Update system packages
sudo apt update && sudo apt upgrade -y

# Restart services
docker-compose restart
```

### Monitoring and Alerting
```bash
# Check service logs
docker-compose logs -f

# Monitor resource usage
docker stats

# Check disk space
df -h

# Monitor network traffic
iftop -i eth0
```

## Troubleshooting

### Common Issues
1. **Container startup failures:** Check logs with `docker-compose logs`
2. **Database connection issues:** Verify credentials and network connectivity
3. **Performance degradation:** Monitor resource usage and adjust limits
4. **Security alerts:** Review audit logs and update configurations

### Support Contacts
- **Technical Support:** [Contact Information]
- **Security Team:** [Contact Information]
- **Operations Team:** [Contact Information]

---

**IMPORTANT:** This deployment guide is for authorized personnel only. All deployments must be conducted in controlled lab environments and comply with DoD security policies and current ROE.