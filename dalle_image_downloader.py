def get_image_from_dall_e(prompt):
    import openai
    import requests

    import shutil


    import openai
    import requests
    import os

    # Replace with your actual DALL-E API key

    openai.api_key = "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"
    # Set image generation parameters

    n = 1  # Number of images to generate (set to 1 for single image)
    size = "1024x1024"  # Image resolution (adjust as needed)



    # Generate images using OpenAI API

    response = openai.Image.create(
        model="dall-e-3",  # or "dall-e-3" if available
        prompt=prompt,
        n=n,
        size=size,
    )

    # Access the single image data
    image = response.data[0]
    image_url = image.url

    # Download the image using requests
    filename = f"dall-e_1.jpg"  # Customize filename
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(filename, "wb") as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
            print(f"Image downloaded successfully: {filename}")
        else:
            print(f"Image download failed: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {e}")

    return filename




