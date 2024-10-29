FROM python:3.9-alpine

# Install dependencies for Python packages that may require compilation
RUN apk add --no-cache  gcc g++ make libffi-dev musl-dev libc-dev openblas-dev

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies, preferring binary wheels
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy the entire project into the working directory
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Set the command to run your application
CMD ["python", "app.py"]