# ==========================================
# LifeOS Dockerfile
# Tynovate AI Internship 2026
# Weeks 1 - 6
# ==========================================

# Use official Python image
FROM python:3.13-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Enable real-time console output
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI application
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]