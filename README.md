# AKS DevOps Assignment ✅

This project provisions a production-like Azure Kubernetes Service (AKS) environment using Terraform, deploys a sample microservice application through CI/CD automation, and configures cluster monitoring using Prometheus and Grafana.

---

## 📌 Architecture Overview

**Tools & Services Used**
| Function | Technology |
|---------|------------|
| IaC | Terraform |
| Containerization | Docker |
| Orchestration | Azure Kubernetes Service |
| CI/CD | GitHub Actions |
| Security Scanning | Checkov + Terrascan |
| Monitoring | Prometheus + Grafana |
| Reporting | Automated Grafana report export |

---

## 🏗️ Infrastructure

Terraform provisions:
- Azure Resource Group
- Virtual Network + Subnets
- AKS Cluster (RBAC Enabled)
- Azure Container Registry (ACR)
- Managed Identity for AKS → ACR Pull
- Secure Networking

### Terraform Deployment Steps

```sh
cd terraform
terraform init
terraform validate
terraform plan -out tfplan
terraform apply tfplan

