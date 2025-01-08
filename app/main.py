from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tts

app = FastAPI(
    title="Kokoro TTS API",
    description="API for Kokoro Text-to-Speech model",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tts.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Kokoro TTS API"} 