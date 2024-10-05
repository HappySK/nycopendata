variable "resource_group_location" {
  description = "The Resource Group location should be passed as Environment Variable"
}

variable "resource_group_name" {
  description = "The Resource Group name should be passed as Environment Variable"
}

variable "agent_count" {
  default = 3
}

variable "ssh_public_key" {
  default = "./public_key.pub"
}

variable "dns_prefix" {
  default = "k8sguru"
}

variable "cluster_name" {
  default = "k8sguru"
}

variable "aks_service_principal_app_id" {
  description = "The Service Principal Client ID should be passed as Environment Variable"
}

variable "aks_service_principal_client_secret" {
  description = "The Service Principal Secret should be passed as Environment Variable"
}