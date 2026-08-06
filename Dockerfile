# ==========================================
# LifeOS Dockerfile
# Tynovate AI Internship 2026
# Weeks 1 - 7
# ==========================================

# Use official Python image
FROM python:3.13-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Expose Streamlit port
EXPOSE 8501

# Default command (FastAPI Backend)
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]