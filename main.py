import os
import requests
from yt_downloader import download_video

def download_images(urls, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for url in urls:
        url = url.strip()
        if not url:
            continue
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            filename = os.path.basename(url.split("?")[0])
            if not filename:
                filename = "image_" + str(urls.index(url)) + ".jpg"
            filepath = os.path.join(output_folder, filename)
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"✅ Downloaded: {filename}")
        except Exception as e:
            print(f"❌ Failed to download {url} - {e}")

def main():
    print("🛠️ Image/Video Downloader CLI")
    print("1️⃣ Download Images")
    print("2️⃣ Download YouTube Videos")

    choice = input("👉 Choose an option (1 or 2): ").strip()

    if choice == "1":
        urls = input("🔗 Enter Image URLs (comma separated): ").split(",")
        output_folder = input("📂 Enter output folder path: ").strip()
        download_images(urls, output_folder)

    elif choice == "2":
        url = input("🔗 Enter YouTube video URL: ").strip()
        output_folder = input("📂 Enter output folder path: ").strip()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        download_video(url, output_folder)

    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
