# Image Captioning with Gemini API

This repository contains a simple Python script that uses the Google Gemini API to generate a detailed caption for an image. It demonstrates how to perform multimodal analysis (visual feature extraction and natural language captioning) using the `gemini-2.0-flash` model.

## Requirements

- Python 3.x
- `google-genai` package (install via `pip install google-genai`)
- `Pillow` for image handling (install via `pip install pillow`)
- A valid Gemini API key stored in an environment variable or placed directly in `main.py` (not recommended for production).

## Setup

1. Clone or download this repository.
2. Place an image file (e.g., `sample_image.png`) in the project folder.
3. Set your Gemini API key, for example:
   ```powershell
   setx GEMINI_API_KEY "YOUR_GEMINI_API_KEY"
   ```
4. (Optional) Update the `image_file` variable in `main.py` if using a different image name.

## Usage

Run the script:

```powershell
python main.py
```

The script will open the specified image, send it to the Gemini model, and print a professional caption generated from the visual features.

## Output

```
--- Generated Caption ---
A glowing futuristic metropolis at night, with towering skyscrapers illuminated by neon lights. A central water feature reflects the vibrant colors, and sleek architectural walkways curve around plazas filled with small groups of people. The atmosphere is both bustling and tranquil, evoking a vision of advanced urban elegance beneath a soft, digital sky.
```

> **Note:** Actual captions will vary depending on the content of the provided image and the model's interpretation.

## Notes

- Ensure your `sample_image.png` is a valid JPEG or PNG file; the script currently sets the MIME type to `image/jpeg` when sending bytes.
- Handle API errors graciously—see the `try/except` block in `main.py` for an example.


Feel free to extend this project by adding command-line arguments, supporting more image formats, or integrating the caption into a web application.
