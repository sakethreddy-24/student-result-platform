variable "resource_group_name" {
  type = string
}

variable "location" {
  type = string
}

variable "nic_name" {
  type = string
}

variable "public_subnet_id" {
  type = string
}

variable "public_ip_id" {
  type = string
}

variable "tags" {
  type = map(string)
}