terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}


resource "azurerm_resource_group" "cv_rg" {
  name     = "rg-cloud-native-cv"
  location = "westeurope"
}


resource "azurerm_container_registry" "cv_acr" {
  name                = "cvregistryfranck"
  resource_group_name = azurerm_resource_group.cv_rg.name
  location            = azurerm_resource_group.cv_rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

# Création du cluster AKS
resource "azurerm_kubernetes_cluster" "cv_aks" {
  name                = "aks-cv-cluster"
  location            = azurerm_resource_group.cv_rg.location
  resource_group_name = azurerm_resource_group.cv_rg.name
  dns_prefix          = "aks-cv"

  default_node_pool {
    name       = "default"
    node_count = 1
   vm_size    = "Standard_D2s_v3"
  }

  identity {
    type = "SystemAssigned"
  }
}