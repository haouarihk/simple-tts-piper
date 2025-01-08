import io
import numpy as np
from piper.voice import PiperVoice
import wave

class TTSService:
    def __init__(self):
        self.model = PiperVoice.load(model_path="./model.onnx")

    def generate_audio(self, text: str, voice_name: str = None, language: str = None):
        # Generate audio using Piper
        audio_data = np.array([], dtype=np.int16)
        for audio_chunk in self.model.synthesize_stream_raw(text):
            chunk_data = np.frombuffer(audio_chunk, dtype=np.int16)
            audio_data = np.concatenate([audio_data, chunk_data])
        
        # Convert to WAV bytes
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wav_file:
            wav_file.setnchannels(1)  # mono
            wav_file.setsampwidth(2)  # 16-bit
            wav_file.setframerate(self.model.config.sample_rate)
            wav_file.writeframes(audio_data.tobytes())
        
        buffer.seek(0)
        return buffer.read(), None  # No phonemes in Piper

    async def generate_audio_stream(self, text: str, voice_name: str = None, language: str = None):
        for audio_bytes in self.model.synthesize_stream_raw(text):
            # Convert bytes to int16 array and back to ensure proper format
            int_data = np.frombuffer(audio_bytes, dtype=np.int16)
            yield int_data.tobytes()