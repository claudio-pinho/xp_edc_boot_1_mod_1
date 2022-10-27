
# Centralizar o arquivo de controle de estado do Terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-xp"
    key = "state/xp/edc/modulo1/terraform.tfstate"
    region = "us-east-1"
  }
}