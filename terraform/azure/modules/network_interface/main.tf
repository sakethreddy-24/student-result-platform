resource "azurerm_network_interface" "this" {
    name = var.nic_name
    location = var.location
    resource_group_name = var.resource_group_name

    ip_configuration {
        name = "primary"
        subnet_id = var.public_subnet_id
        private_ip_address_allocation = "Dynamic"
        public_ip_address_id = var.public_ip_id
    }

    tags = var.tags
}