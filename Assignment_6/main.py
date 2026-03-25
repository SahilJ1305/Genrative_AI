import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

# 1. Load the API key from the .env file
load_dotenv()
client = OpenAI(api_key="OPENAI_API_KEY")

def generate_openai_image(prompt):
    print(f"Generating image for: '{prompt}'...")
    
    try:
        # 2. Call the OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard", # Use "hd" for better detail
            n=1,
        )

        # 3. Extract the URL
        image_url = response.data[0].url
        print(f"Image created! Downloading from: {image_url}")

        # 4. Save the image locally
        img_data = requests.get(image_url).content
        filename = "openai_output.png"
        
        with open(filename, 'wb') as handler:
            handler.write(img_data)
            
        print(f"Success! Image saved as {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    user_prompt = "A futuristic university campus in India, neon lights, 3d render"
    generate_openai_image(user_prompt)

