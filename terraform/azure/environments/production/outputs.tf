output "resource_group_name" {
  value = module.resource_group.resource_group_name
}

output "location" {
  value = module.resource_group.location
}

output "vm_name" {
  value = module.virtual_machine.vm_name
}

output "public_ip" {
  value = module.public_ip.public_ip_address
}