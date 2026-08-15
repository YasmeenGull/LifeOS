# ==========================================
# LifeOS - Multi-Stage Dockerfile
# Tynovate AI Internship 2026
# Week 8 - Deployment
# ==========================================

# ==========================================
# Base Stage
# ==========================================
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# System dependencies required by some ML packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies first for Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir \
    --default-timeout=1000 \
    --retries=10 \
    -r requirements.txt

# ==========================================
# API Stage
# ==========================================
FROM base AS api

COPY . .

# Make sure Python can import the project package
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]

# ==========================================
# Dashboard Stage
# ==========================================
FROM base AS dashboard

COPY . .

# Make sure Streamlit can import src.*
ENV PYTHONPATH=/app

EXPOSE 8501

CMD ["streamlit", "run", "/app/src/dashboard/app.py", "--server.address=0.0.0.0", "--server.port=8501"]