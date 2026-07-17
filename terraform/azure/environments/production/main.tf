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