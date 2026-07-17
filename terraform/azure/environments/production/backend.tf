terraform {
    backend "azurerm" {
        resource_group_name = "terraform-backend-rg"
        storage_account_name = "tfstatesaketh2026"
        container_name = "tfstate"
        key = "student-result-platform-prod.tfstate"
    }
}