# Use an official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]