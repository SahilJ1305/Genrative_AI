# Assignment 8 – Text-to-Speech with Gemini TTS

This Python script demonstrates using Google’s Gemini TTS
model to synthesize speech from text and save the result as a WAV file.

## 🧠 Overview

- **`main.py`**
  - Initializes a `genai.Client` with an API key.
  - Defines `generate_speech()` that calls the `gemini-2.5-flash-preview-tts` model.
  - Requests an **AUDIO** response modality and uses the prebuilt `Kore` voice.
  - Writes the returned PCM data to `assignment_8_output.wav`.

- Example usage (executed when run as a script) speaks a sample welcome message.

## ⚙️ Prerequisites

1. **Python 3.8+** installed on your machine.
2. Install dependencies:

   ```sh
   pip install google-genai
   ```

3. Set your API key:

   ```python
   client = genai.Client(api_key="YOUR_API_KEY_HERE")
   ```

   Replace the placeholder key in `main.py` or configure via environment variable.

## 🚀 Running

From the project directory:

```sh
python main.py
```

After execution you should see console output like:

```
Synthesizing: 'Welcome to the 2026 AI Summit…'
Success!
```

…and a file named `assignment_8_output.wav` will be created.

## 📁 Output

- `assignment_8_output.wav` – the generated speech audio (24 kHz, 16‑bit mono PCM).

## 💡 Notes

- Change the text in `generate_speech()` or call the function with other strings.
- Modify `voice_name` or other `SpeechConfig` settings as needed.
- Handle errors by catching exceptions around the `generate_content` call.

---

Feel free to adapt this README to your assignment requirements or extend the script with CLI arguments, additional voices, etc.
