output "resource_group_name" {
  value = azurerm_resource_group.cv_rg.name
}

output "acr_login_server" {
  value = azurerm_container_registry.cv_acr.login_server
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.cv_aks.name
}

output "kube_config" {
  value     = azurerm_kubernetes_cluster.cv_aks.kube_config_raw
  sensitive = true # Cela masque la valeur dans la console, car c'est un secret
}
