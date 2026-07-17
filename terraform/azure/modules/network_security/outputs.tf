output "public_nsg_id" {
    value = azurerm_network_security_group.public.id
}

output "private_nsg_id" {
    value = azurerm_network_security_group.private.id
}