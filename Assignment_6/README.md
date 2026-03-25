# Assignment 6 - OpenAI Image Generator

This simple Python project demonstrates how to use the OpenAI API to generate an image from a text prompt and download it locally.

## Features

- Loads OpenAI API key from a `.env` file using `python-dotenv`.
- Sends a prompt to the OpenAI `dall-e-3` model.
- Downloads and saves the generated image as `openai_output.png`.
- Handles basic error cases.

## Prerequisites

- Python 3.7 or later
- An OpenAI account and an API key

## Setup

1. **Clone or download** this repository.
2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Create a `.env` file** in the project root with your OpenAI key:
   ```text
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the script directly from the command line:

```bash
python main.py
```

The script will generate an image for the hard‑coded prompt and save it as `openai_output.png`.

To use a custom prompt, modify the `user_prompt` variable in `main.py` or adapt the code to accept command line arguments.

## Notes

- The script uses the `openai` Python package and `requests` for downloading the image.
- Adjust image `size`, `quality`, or `n` in the `generate_openai_image` function if needed.

## License

This project is provided for educational purposes as part of a university assignment.
