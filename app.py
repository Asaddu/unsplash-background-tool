import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your Unsplash access key and image save path
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')
IMAGE_SAVE_PATH = os.path.join(os.getenv('IMAGE_SAVE_PATH'), 'background.jpg')

# Unsplash API endpoint
UNSPLASH_URL = "https://api.unsplash.com/photos/random"

# Set query parameters for the image
params = {
    'query': 'space',
    'client_id': UNSPLASH_ACCESS_KEY
}

# Fetch the image
response = requests.get(UNSPLASH_URL, params=params)
if response.status_code == 200:
    data = response.json()
    image_url = data['urls']['regular']
    
    # Save the image to the local directory
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open(IMAGE_SAVE_PATH, 'wb') as file:
            file.write(img_response.content)
        print(f"Image saved to {IMAGE_SAVE_PATH}")
    else:
        print(f"Failed to fetch image: {img_response.status_code}")
    
    # Register the download to meet Unsplash's guidelines
    download_location = data['links']['download_location']
    download_response = requests.get(download_location, params={'client_id': UNSPLASH_ACCESS_KEY})
    if download_response.status_code == 200:
        print("Download registered with Unsplash.")
    else:
        print(f"Failed to register download: {download_response.status_code}")
else:
    print(f"Failed to get image from Unsplash: {response.status_code}")
