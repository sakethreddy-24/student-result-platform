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

variable "public_nsg_name" {
  type = string
}

variable "private_nsg_name" {
  type = string
}

variable "public_ip_name" {
  type = string
}

variable "nic_name" {
  type = string
}

variable "vm_name" {
  type = string
}

variable "vm_size" {
  type = string
}

variable "admin_username" {
  type = string
}

variable "ssh_public_key" {
  type = string
}