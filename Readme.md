## 🚀 Cloud-MLOps-Security-v1 Proof of Concept (PoC)

Welcome to the Cloud-MLOps-Security-v1 PoC! This guide will walk you through setting up and running the project, culminating in a demonstration of **CI/CD security checks** using GitHub Actions.

---

## 1. Project Setup and File Structure

Begin by creating the project directory and necessary files.

### 🛠️ Directory and File Creation

* **Create Project Directory:**
    ```bash
    mkdir cloud-mlops-security-v1
    cd cloud-mlops-security-v1
    ```
* **Create Application Files:**\
    You must create the following files in the root directory:
    - `model_trainer.py`
    - `main.py`
    - `requirements.txt`
    - `Dockerfile`

* **Create CI/CD Workflow Directory and File:**
    ```bash
    mkdir -p .github/workflows
    ```
    Create the following file:
    - `.github/workflows/build.yml`

---

## 2. Model Training (Local)

Before running the application, you need to train the model locally.

### 💻 Training Steps

1.  **(Optional but Recommended):** Create and activate a Python virtual environment.
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run Trainer:**
    ```bash
    python model_trainer.py
    ```


---

## 3. GitHub CI/CD: Automated Build and Security Scan

This step triggers the automated pipeline that showcases the **security scanning** in action.

### ☁️ CI/CD Trigger

1.  **Initialize Git:**
    ```bash
    git init
    git add .
    git commit -m "Initial commit for PoC setup"
    ```
2.  **Set Up and Push to GitHub:**
    * Create a new repository on GitHub.
    * Connect your local repository and push the code to the `main` branch.

### 🚀 Action:
Pushing to the `main` branch will **automatically trigger** the `build.yml` workflow. \
This workflow executes the **Build**, **Scan**, and **Publish** steps. \
The final image will be published to your repository's **Packages** section on GitHub Container Registry (`ghcr.io`)—*if the scan passes*. 

---

## 4. Reviewing the CI/CD Security Failure

The pipeline is intentionally configured to fail to demonstrate effective security gatekeeping.

### 🛑 Expected Failure and Log Review

Review the logs in your repository's **GitHub Actions** tab. You will see the pipeline fail at the security scan step.

* **Date of Test:** As of **08 Dec 2025**, the build pipeline is expected to fail at this step.
* **Reason:** The pipeline uses a security scanner to prevent deployment of an image with known **Common Vulnerabilities and Exposures (CVEs)** in older dependencies.

| Library (Source) | Vulnerability | Severity | Status | Installed Version | Fixed Version |
| :--------------- | :------------ | :------- | :----- | :---------------- | :------------ |
| `starlette`      | `CVE-2024-47874` | **HIGH** | fixed  | `0.27.0`          | `0.40.0`      |

 ✅ **Conclusion:** This failure confirms the security checks are **working as expected** by blocking images that rely on vulnerable, un-patched libraries.

---


Happy testing! 

