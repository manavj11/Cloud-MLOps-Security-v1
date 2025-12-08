# How to Run This POC - Cloud-MLOps-Security-v1
## 1. Project Setup

### Bash
mkdir cloud-mlops-security-v1
cd cloud-mlops-security-v1

(Create the files above: model_trainer.py, main.py, requirements.txt, Dockerfile)

mkdir -p .github/workflows

(Create the build.yml file inside .github/workflows/)

## 2. Train the Model

### Bash
pip install -r requirements.txt 
python model_trainer.py

(This creates the essential 'model.pkl' file.)
(Optional: Create and activate a Python virtual environment)

## 3. GitHub CI/CD Automatic building and checking

GitHub CI/CD:

Initialize a Git repository, commit the files, and push to a new GitHub repository's main branch.

The build.yml workflow will automatically trigger, executing the Build, Scan, and Publish steps. The final image will be available in your repository's Packages section on GitHub Container Registry (ghcr.io).

## 4. Review CI/CD Logs in Github Actions

As of 08 Dec 2025, the build pipeline will fail at the below error, thereby showcasing the checks working as expected to not allow older libraries with CVEs to run.

│       Library        │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version


│ starlette (METADATA) │ CVE-2024-47874 │ HIGH     │ fixed  │ 0.27.0            │ 0.40.0


Happy testing!

