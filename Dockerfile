FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (removed build-essential as it's not needed)
RUN apt-get update && apt-get install -y espeak-ng \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code and model
COPY app/ app/
COPY voice_model.onnx .
COPY voice_model.onnx.json .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 