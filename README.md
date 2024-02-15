# Terraform_Senior_Project
API Group presents...our senior project! We are planning on contributing to the CloudGoat GitHub page, with our "capture the flag" scenario. This project will be written with Terraform (HCL) and Python 3.

Authors: Jeffrey, Dominica, John

Content:
ec-2_redhat.tf
  - This is our terraform code that creates and initializes an EC-2 instance in AWS. We've added certain specifications,        such as the server being based in RedHat Linux.
  - We only have a single EC-2 instance at the moment, we have the ability to launch multiple instances and multiple            services by adding more terraform files

our_scenario.py
  - This is our Python code that acts as a wrapper for our terraform code.
  - When ran, the Python code will run the various Terraform commands including "Init" and "Apply"
  - This approach is more scalable and easier to Run/Operate
  - Its also the convention for the CloudGoat Github page

terraform.tfstate
  - This file is critical for storing the state of our infrastructure
  - If this were to get corrupted, it could lead to serious issues when attempting to run the code.
  - We have a backup of this file included to act as a failsafe for the .tfstate file
  - We've also saved the .tfstate file in an S3 bucket in AWS

HOW TO USE: 
1. Download the Repository, open your terminal and CD to the repo
2. Run the following command "python3 our_scenario.py"
3. Standby, your EC-2 instance will be created

Requirements

- Linux or MacOS. Windows is not officially supported.
- Argument tab-completion requires bash 4.2+ (Linux, or OSX with some difficulty).
- Python3.6+ is required.
- Terraform >= 0.14 installed and in your $PATH.
- The AWS CLI installed and in your $PATH, and an AWS account with sufficient privileges to create and destroy resources.
- jq 
