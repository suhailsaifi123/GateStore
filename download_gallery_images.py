import os
import requests

# List of real gate image URLs from Unsplash
image_urls = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=800&q=80"
]

gallery_dir = os.path.join("static", "img", "gallery")
os.makedirs(gallery_dir, exist_ok=True)

for idx, url in enumerate(image_urls, start=1):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(gallery_dir, f"gallery{idx}.jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {file_path}")
    else:
        print(f"Failed to download {url}")

print("All downloads complete.") 