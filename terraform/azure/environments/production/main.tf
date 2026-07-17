module "resource_group" {
  source = "../../modules/resource_group"

  resource_group_name = var.resource_group_name
  location            = var.location
}

module "networking" {
  source = "../../modules/networking"

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location

  vnet_name             = var.vnet_name
  address_space         = var.address_space
  public_subnet_name    = var.public_subnet_name
  public_subnet_prefix  = var.public_subnet_prefix
  private_subnet_name   = var.private_subnet_name
  private_subnet_prefix = var.private_subnet_prefix

  tags = local.common_tags
}

module "network_security" {
  source = "../../modules/network_security"

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location

  public_nsg_name  = var.public_nsg_name
  private_nsg_name = var.private_nsg_name

  public_subnet_id  = module.networking.public_subnet_id
  private_subnet_id = module.networking.private_subnet_id

  tags = local.common_tags
}

module "public_ip" {
  source = "../../modules/public_ip"

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location

  public_ip_name = var.public_ip_name

  tags = local.common_tags
}

module "network_interface" {
  source = "../../modules/network_interface"

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location

  nic_name = var.nic_name

  public_subnet_id = module.networking.public_subnet_id
  public_ip_id     = module.public_ip.public_ip_id

  tags = local.common_tags
}

module "virtual_machine" {
  source = "../../modules/virtual_machine"

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location

  vm_name        = var.vm_name
  vm_size        = var.vm_size
  admin_username = var.admin_username
  ssh_public_key = var.ssh_public_key

  network_interface_id = module.network_interface.network_interface_id

  tags = local.common_tags
}