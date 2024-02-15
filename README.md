# Terraform_Senior_Project by the API Group
**Authors: Jeffrey, Dominica, John**
## Project Goal:
We plan to create a capture-the-flag (CTF) scenario that will be contributed to the CloudGoat GitHub page by Rhino Security Labs. 

**Coding languages used:**
-- Terraform (HCL) 
-- Python3
## Content:
#### ec-2_redhat.tf
This code automates the process of creating instances, so the user does not have to configure the instance manually on AWS. It specifies the region (us-east-1), the Amazon Machine Image (ami), the instance type, and instance name. For now, this code creates a Red Hat Enterprise Linux 9 EC2 instance, but it can serve as a template to create other types of instances if needed.

**Coding language(s) used:**
-- Terraform (HCL)
#### our_scenario.py
This is the code for our CTF scenario. Following CloudGoat Github convention, it consists of python code that is a wrapper for the Terraform code. This is so the project can be more scalable and easier to run/operate. 
As of now, the code can run Terraform commnds: 'init' and 'apply.'

**Coding language(s) used:**
--Python3
#### terraform.tfstate
This code stores the current state of the project's infrastructure. It specifies things such as: the instance's public and private IP address, AMI, Amazon Region Number (ARN), Availability Zone (AZ), type, state, security group, private key, etc. 
As such it is important that this code is well-maintained. In the event of the file getting corrupted, a backup for this .tfstate file is stored on this Github page as well as in an S3 bucket in AWS. 
**Coding language(s) used:**
--Terraform (HCL)

---
### HOW TO USE: 
1. Download the Repository, open your terminal and CD to the repo
2. Run the following command "python3 our_scenario.py"
3. Standby, your EC-2 instance will be created
#### Requirements
- Linux or MacOS. Windows is not officially supported.
- Argument tab-completion requires bash 4.2+ (Linux, or OSX with some difficulty).
- Python3.6+ is required.
- Terraform >= 0.14 installed and in your $PATH.
- The AWS CLI installed and in your $PATH, and an AWS account with sufficient privileges to create and destroy resources.
- jq 
