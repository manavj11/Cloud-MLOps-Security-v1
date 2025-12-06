How to Run This POC
Project Setup:

Bash
mkdir minimal-mlops-poc
cd minimal-mlops-poc
# Create the files above: model_trainer.py, main.py, requirements.txt, Dockerfile
mkdir -p .github/workflows
# Create the build.yml file inside .github/workflows/
Train the Model (Local Step 0):

Bash
# (Optional: Create and activate a Python virtual environment)
pip install -r requirements.txt 
python model_trainer.py
# This creates the essential 'model.pkl' file.

GitHub CI/CD:

Initialize a Git repository, commit the files, and push to a new GitHub repository's main branch.

The build.yml workflow will automatically trigger, executing the Build, Scan, and Publish steps. The final image will be available in your repository's Packages section on GitHub Container Registry (ghcr.io).

