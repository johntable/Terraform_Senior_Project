import subprocess

# Initiate Terraform
def run_terraform_init():
    subprocess.run(["terraform", "init"], check=True)

# Apply and Auto-Approve the Terraform instance
def run_terraform_apply():
    subprocess.run(["terraform", "apply", "-auto-approve"], check=True)


def main():
    # Run Terraform init
    run_terraform_init()

    # Run Terraform apply
    run_terraform_apply()


if __name__ == "__main__":
    main()
