# Use the official lightweight Python image for ARM architecture (Raspberry Pi)
FROM arm32v7/python:3.8.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the working directory
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Set the command to run your application
CMD ["python", "app.py"]