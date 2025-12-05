# Dockerfile
# -----------------------------------------------------------------------------
# STEP 2: Dockerfile (Multi-stage build)
# Uses a build stage for dependencies and a lean runtime stage.
# -----------------------------------------------------------------------------

# Stage 1: Build/Dependencies Stage
# Use a Python image with development headers for package installation
FROM python:3.11-slim as builder

# Set the working directory
WORKDIR /app

# Install dependencies needed for the application
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Runtime Stage
# Use the absolute minimal Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy only the installed dependencies from the builder stage
# This significantly reduces image size compared to installing everything here
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy application files (main.py and the model artifact)
# The model artifact must be in the image for the API to load it
COPY main.py .
COPY model.pkl . 

# Expose the port the application runs on
EXPOSE 80

# Command to run the application using uvicorn (an ASGI server)
# The application will listen on all interfaces (0.0.0.0) on port 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]