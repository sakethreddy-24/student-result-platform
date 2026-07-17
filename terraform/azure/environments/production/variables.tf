variable "resource_group_name" {
  description = "Azure Resource Group Name"
  type        = string
}

variable "location" {
  description = "Azure Region"
  type        = string
}

variable "vnet_name" {
  type = string
}

variable "address_space" {
  type = list(string)
}

variable "public_subnet_name" {
  type = string
}

variable "public_subnet_prefix" {
  type = list(string)
}

variable "private_subnet_name" {
  type = string
}

variable "private_subnet_prefix" {
  type = list(string)
}