import requests
from bs4 import BeautifulSoup
import urllib
import os

url = "https://www.istockphoto.com/photo/steel-washer-isolated-on-white-background-top-view-closeup-gm857711718-141492795"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all image tags on the page
image_tags = soup.find_all("img")

# Create a directory to save the images
save_dir = "images"
os.makedirs(save_dir, exist_ok=True)

# Download each image
for img_tag in image_tags:
    # Get the source URL of the image
    image_url = img_tag["src"]

    # Extract the filename from the URL
    filename = image_url.split("/")[-1].split("?")[0]

    # Construct the full path to save the image
    save_path = os.path.join(save_dir, filename)

    # Download the image
    image_data = requests.get(image_url).content

    # Save the image to a file
    with open(save_path, "wb") as f:
        f.write(image_data)
        print(f"Image '{filename}' downloaded successfully.")
