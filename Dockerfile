# Use the official Python image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the main application
CMD ["python", "src/main.py"]