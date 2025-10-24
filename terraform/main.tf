resource "azurerm_resource_group" "rg" {
name = var.rg_name
location = var.location
}


resource "azurerm_kubernetes_cluster" "aks" {
name = var.aks_name
location = azurerm_resource_group.rg.location
resource_group_name = azurerm_resource_group.rg.name
dns_prefix = "devopsaks"


default_node_pool {
name = "default"
node_count = var.node_count
vm_size = var.node_vm_size
}


identity {
type = "SystemAssigned"
}


role_based_access_control {
enabled = true
}


network_profile {
network_plugin = "azure"
}


sku_tier = "Paid"
}


resource "azurerm_container_registry" "acr" {
name = lower("devopsacr${random_integer.prefix.result}")
resource_group_name = azurerm_resource_group.rg.name
location = azurerm_resource_group.rg.location
sku = "Standard"
admin_enabled = false
}