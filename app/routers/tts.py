from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse, Response
from app.models.tts import TTSRequest
from app.services.tts_service import TTSService

router = APIRouter()
tts_service = TTSService()

@router.post("/tts")
async def text_to_speech(request: TTSRequest):
    try:
        audio_bytes, _ = tts_service.generate_audio(request.text)
        return Response(
            content=audio_bytes,
            media_type="audio/wav"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tts/stream")
async def stream_tts(request: TTSRequest):
    try:
        return StreamingResponse(
            tts_service.generate_audio_stream(request.text),
            media_type="audio/wav"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 