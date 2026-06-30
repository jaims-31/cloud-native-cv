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

### 🐳 Alternative: Fast Local Run (Docker Compose)
If you want to test the application locally without deploying to Azure/Kubernetes, you can spin up the entire stack in seconds using Docker Compose:

1. Clone the repository and navigate to the root directory.
2. Run the following command:
```bash
docker-compose up --build
```
Open your browser and navigate to http://localhost:3000 (or the port configured for your frontend) to view the application.

## 🔀 Deployment Workflow (CI/CD Pipeline)

The code lifecycle is fully automated using a GitHub Actions pipeline (`ci.yml`):

1. **Build & Tag:** On every commit to the `main` branch, GitHub Actions triggers Docker image builds for each microservice.
2. **Push to ACR:** Secure authentication to Azure via repository deployment secrets, followed by pushing images with both the `latest` tag and the commit hash (SHA).
3. **Rotation Strategy:** Managed Azure access keys with dual-entry rotation to ensure continuous security without service interruption.





[ Code Commit ] ──> [ GitHub Actions ] ──> [ Azure Container Registry (ACR) ]
│
(Image Pull)
▼
[ Azure Kubernetes Service ]
├── Ingress Nginx Controller
├── Pod cv-frontend (Running)
├── Pod cv-api      (Running)
└── Pod cv-pdf      (Running)






*Note: All application pods are configured to run resiliently and are self-managed by Kubernetes.*

---

## ⚙️ Configuration & Environment

The proper functioning of the application depends on the configuration of environment variables.

### 1. Local Configuration
Before running the project locally, create a `.env` file at the root by copying the provided example:

```bash
cp .env.example .env

---

## 🚀 Local Deployment & Key Commands

### Prerequisites
* Configured Azure CLI
* `kubectl` connected to the AKS cluster

### 1. Apply Kubernetes Manifests
To deploy the entire stack (Deployments, Services, Ingress) to the cluster:
```bash
kubectl apply -f k8s/
```



2. Check Cluster Health Status
```bash
kubectl get pods -n default
```

Expected status: All components (cv-frontend, cv-api, cv-pdf, ingress-nginx) must display a Running status.




3. Retrieve Public Access IP
```bash
kubectl get ingress
```

Copy the public IP address from the ADDRESS column to browse the live application.




🧠 Skills Validated Through This Project
Microservices Architecture: Decoupling responsibilities and managing inter-service communication.

Cloud Security: Advanced secret management (GitHub Secrets), network isolation, and access role management (AcrPull) between Azure services.

Resilience & High Availability: Configuring Kubernetes deployment strategies, automatic container restarts upon failure, and traffic management via Ingress.

Troubleshooting: Deep container log analysis (kubectl logs), investigating Pod lifecycles (ImagePullBackOff debugging), and workflow pipeline analysis.
