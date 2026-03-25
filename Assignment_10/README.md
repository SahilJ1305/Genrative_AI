# Assignment 10 - Transformer Image Generation

This repository contains a Python script (`main.py`) which demonstrates the
capabilities of the OpenAI DALL·E 3 model for generating highly-detailed
images from textual prompts. It is part of a Gen AI course assignment.

## Features

- Loads an API key from environment variables using a `.env` file.
- Sends text prompts to the DALL·E 3 model and retrieves a revised prompt
enhanced by the model.
- Downloads and saves the resulting images to the local filesystem.
- Displays images using the default system image viewer (via Pillow).

## Setup

1. Create a virtual environment and install requirements:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1     # on Windows
   pip install -r requirements.txt   # create this file if not already present
   ```

2. Create a `.env` file in the project root and add your OpenAI API key:
   ```text
   OPENAI_API_KEY=sk-...your-key...
   ```
   (This script currently uses a hard‑coded key for demonstration, but it's
   recommended to load it from the environment.)

3. Run the script:
   ```powershell
   python main.py
   ```
   Two images will be generated and saved in the working directory.

## Example Prompts and Outputs

### 1. Mechanical Hand & Clockwork Hummingbird
- **Prompt:**
  > "A hyper-realistic close-up of a futuristic mechanical hand assembling a
  tiny clockwork hummingbird on a mahogany desk, with soft morning light
  filtering through a window."
- **Transformer Revised Prompt:**
  > "Create a hyper-realistic close-up image of a futuristic mechanical hand.
  This advanced robotic appendage is deftly piecing together a miniature
  clockwork hummingbird. The meticulous assembly is taking place on a table
  made of mahogany, which adds a warm, subtle color contrast to the cold
  metallic elements. The surrounding scene is softly lit by the morning sun,
  as if telling the start of a new day, with the light rays penetrating
  through a nearby window, casting long, soft shadows and enhancing the
  overall depth of the image."
- **Result:** Saved as `clockwork_hummingbird.png`

### 2. Fauvist Stained-Glass Library
- **Prompt:**
  > "An 8k digital painting of a Fauvist-style library where the books are
  actually made of cascading stained glass that glows with internal light."
- **Transformer Revised Prompt:**
  > "Generate an 8K digital painting representing a library. The style should
  exhibit the bold, vibrant, and non-naturalistic colors typically associated
  with the Fauvism movement. The uniqueness of the scene comes from the
  books, which are not ordinary. They are made of cascading stained glass that
  emits an internal glow, bathing the library in a series of wonderfully
  radiant light-shows. Please keep the setting and objects abstract and
  fanciful alike, with a primary medium of oil on canvas."
- **Result:** Saved as `stained_glass_library.png`

## Notes

- The `revised_prompt` field returned by the API illustrates how DALL·E 3
  expands and refines user prompts to better capture detail and intent.
- Modify `main.py` to experiment with different prompts, image sizes, and
  output filenames.

---

