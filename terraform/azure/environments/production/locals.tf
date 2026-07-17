locals {
  project     = "student-result-platform"
  environment = "production"

  common_tags = {
    Project     = local.project
    Environment = local.environment
    ManagedBy   = "Terraform"
    Owner       = "DevOps"
  }
}