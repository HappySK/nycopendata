terraform {

  required_version = ">=0.12"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.93.0"
    }
  }
  backend "azurerm" {
      resource_group_name  = "${env.RG_NAME}"
      storage_account_name = "${env.STORAGE_ACCOUNT_NAME}"
      container_name       = "terraform"
      key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
  skip_provider_registration = true
}

# Import the Azure Resource Group
resource "azurerm_resource_group" "k8s" {
  name     = var.resource_group_name
  location = var.resource_group_location
}
