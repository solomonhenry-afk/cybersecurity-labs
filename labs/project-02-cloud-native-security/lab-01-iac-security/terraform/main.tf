provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-insecure-cloud-lab"
  location = "East US"
}

resource "azurerm_storage_account" "storage" {
  name                     = "insecurestorage${random_integer.rand.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  # NOTE: Public access is intentionally enabled at the container level
# to demonstrate insecure storage exposure for CNAPP / CSPM detection.
# This lab focuses on design-time risk identification before deployment.

  network_rules {
    default_action = "Allow"
  }

  tags = {
    Environment = "Dev"
  }
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "aks-insecure-cluster"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "insecureaks"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  role_based_access_control_enabled = false
}
