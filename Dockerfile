# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the application
CMD bash -c 'sleep 50 && uvicorn app.main:app --host 0.0.0.0 --port 8000'

