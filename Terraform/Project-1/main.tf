terraform {
  required_version = "1.14.5"
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.32.1"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}


resource "aws_instance" "my-instance" {
  ami = "ami-0c1fe732b5494dc14"
  instance_type = "t3.micro"

  tags = {
    Name = "server-from-terraform"
  }
}