# Simple TTS API Service

A FastAPI-based Text-to-Speech API service using Piper TTS. This service provides a simple REST API for converting text to speech with streaming capabilities.

## Features

- Text-to-Speech conversion using Piper TTS
- RESTful API with FastAPI
- Support for both full response and streaming audio
- Dockerized deployment
- WAV audio output

## Requirements

- Docker and Docker Compose
- ONNX voice model file (`voice_model.onnx` and `voice_model.onnx.json`)

## Quick Start

1. Place your ONNX voice model files in the project root:
   - `voice_model.onnx`
   - `voice_model.onnx.json`

2. Build and run the Docker container:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Convert Text to Speech
```http
POST /api/v1/tts
```

Request body:
```json
{
    "text": "Your text to convert to speech"
}
```

Response: WAV audio file

### 2. Stream Text to Speech
```http
POST /api/v1/tts/stream
```

Request body:
```json
{
    "text": "Your text to convert to speech"
}
```

Response: Streamed WAV audio

## Example Usage

Using curl:
```bash
# Full response
curl -X POST "http://localhost:8000/api/v1/tts" \
     -H "Content-Type: application/json" \
     -d '{"text":"Hello, world!"}' \
     --output output.wav

# Streaming response
curl -X POST "http://localhost:8000/api/v1/tts/stream" \
     -H "Content-Type: application/json" \
     -d '{"text":"Hello, world!"}' \
     --output output.wav
```

Using Python requests:
```python
import requests

# Full response
response = requests.post(
    "http://localhost:8000/api/v1/tts",
    json={"text": "Hello, world!"}
)
with open("output.wav", "wb") as f:
    f.write(response.content)

# Streaming response
response = requests.post(
    "http://localhost:8000/api/v1/tts/stream",
    json={"text": "Hello, world!"},
    stream=True
)
with open("output.wav", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

## Development

To run the service without Docker:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the service:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the service is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 