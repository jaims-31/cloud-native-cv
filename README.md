# 🔍 Cloud-Native CV Application

This project is a modern online CV display and generation application, designed using a **microservices** architecture and deployed in a highly available Cloud environment. The main objective is to practice key **DevOps** concepts: Infrastructure as Code (IaC), containerization, Kubernetes orchestration, and continuous deployment (CI/CD).

## 🏗️ Technical Architecture

The application is split into three distinct, autonomous, and scalable microservices:

| Component | Technology | Role |
| :--- | :--- | :--- |
| **`cv-frontend`** | React / Nginx | Responsive web user interface to view the CV. |
| **`cv-api`** | Node.js / Express | REST API managing dynamic profile data. |
| **`cv-pdf`** | Node.js Worker | PDF generation and export service for the CV. |

---

## 🛠️ DevOps & Cloud Stack

* **Cloud Provider:** Microsoft Azure (Managed resources)
* **Orchestration:** **Azure Kubernetes Service (AKS)** (Cluster: `aks-cv-cluster`)
* **Image Registry:** **Azure Container Registry (ACR)** (`cvregistryfranck.azurecr.io`)
* **CI/CD:** **GitHub Actions** (Automated Build & Push)
* **Routing & Ingress:** **Nginx Ingress Controller** (Reverse-proxy and single entry point to the cluster)
* **IaC:** Terraform (Automated provisioning of Azure infrastructure)

---

## 🔀 Deployment Workflow (CI/CD Pipeline)

The code lifecycle is fully automated using a GitHub Actions pipeline (`ci.yml`):

1. **Build & Tag:** On every commit to the `main` branch, GitHub Actions triggers Docker image builds for each microservice.
2. **Push to ACR:** Secure authentication to Azure via repository deployment secrets, followed by pushing images with both the `latest` tag and the commit hash (SHA).
3. **Rotation Strategy:** Managed Azure access keys with dual-entry rotation to ensure continuous security without service interruption.

