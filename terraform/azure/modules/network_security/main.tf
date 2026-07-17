resource "azurerm_network_security_group" "public" {
    name = var.public_nsg_name
    location = var.location
    resource_group_name = var.resource_group_name

    tags = var.tags
}

resource "azurerm_network_security_group" "private" {
    name = var.private_nsg_name
    location = var.location
    resource_group_name = var.resource_group_name

    tags = var.tags
}

resource "azurerm_network_security_rule" "allow_ssh" {
    name = "Allow-SSH"
    priority = 100
    direction = "Inbound"
    access = "Allow"
    protocol = "Tcp"

    source_port_range = "*"
    destination_port_range = "22"

    source_address_prefix = "*"
    destination_address_prefix = "*"

    resource_group_name = var.resource_group_name
    network_security_group_name = azurerm_network_security_group.public.name
}

resource "azurerm_network_security_rule" "allow_http" {
    name = "Allow-HTTP"
    priority = 200
    direction = "Inbound"
    access = "Allow"
    protocol = "Tcp"

    source_port_range = "*"
    destination_port_range = "80"
    
    source_address_prefix = "*"
    destination_address_prefix = "*"

    resource_group_name = var.resource_group_name
    network_security_group_name = azurerm_network_security_group.public.name
}

resource "azurerm_network_security_rule" "allow_https" {
  name                        = "Allow-HTTPS"
  priority                    = 300
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"

  source_port_range           = "*"
  destination_port_range      = "443"

  source_address_prefix       = "*"
  destination_address_prefix  = "*"

  resource_group_name          = var.resource_group_name
  network_security_group_name  = azurerm_network_security_group.public.name
}

resource "azurerm_subnet_network_security_group_association" "public" {
    subnet_id = var.public_subnet_id
    network_security_group_id = azurerm_network_security_group.public.id
}

resource "azurerm_subnet_network_security_group_association" "private" {
    subnet_id = var.private_subnet_id
    network_security_group_id = azurerm_network_security_group.private.id
}