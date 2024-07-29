# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the necessary ports (optional, for documentation purposes)
EXPOSE 8000
EXPOSE 8501

# The default command to run uvicorn and streamlit can be overridden in docker-compose
