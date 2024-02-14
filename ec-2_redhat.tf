provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0fe630eb857a6ec83"  # Red Hat Enterprise Linux 9 (64-bit x86) AMI ID
  instance_type = "t2.micro"                # Change instance type as needed

  tags = {
    Name = "example-instance"
  }
}
