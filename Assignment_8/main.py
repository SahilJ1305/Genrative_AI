import os
import wave
from google import genai
from google.genai import types

# 1. Initialize Client (ensure your key is valid)
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")
def save_as_wav(filename, pcm_data):
    """Saves raw 24kHz 16-bit Mono PCM data into a WAV file."""
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)       # Mono
        wf.setsampwidth(2)      # 16-bit (2 bytes)
        wf.setframerate(24000)  # Gemini TTS default rate
        wf.writeframes(pcm_data)

def generate_speech(text):
    print(f"Synthesizing: '{text}'...")
    
    try:
        # 2. Add response_modalities to the config
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts", 
            contents=text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"], # THIS IS THE KEY FIX
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name='Kore' 
                        )
                    )
                )
            )
        )

        # 3. Extract the audio bytes
        # The model returns audio data in the first part of the candidate
        audio_part = response.candidates[0].content.parts[0]
        
        if audio_part.inline_data:
            audio_bytes = audio_part.inline_data.data
            save_as_wav("output_audio.wav", audio_bytes)
            print("Success!")
        else:
            print("No audio data found in the response.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    generate_speech("Welcome to the 2026 AI Summit, where we explore the future of human-machine collaboration! Speak with the infectious energy of a professional radio host.")
