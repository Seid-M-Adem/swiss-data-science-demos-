FROM mcr.microsoft.com/devcontainers/python:3.9

# Set working directory
WORKDIR /workspace

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

