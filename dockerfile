# Use an official Python image as a base
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the application will run on
EXPOSE 8003

# Run the command to start the application when the container launches
CMD ["python", "app/utils/download.py"]