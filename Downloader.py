import argparse
import os
import requests
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def download_file(url, output_dir):
    """
    Downloads a regular file from the given URL and saves it to the output directory.
    Displays a progress bar using tqdm.
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()
    filename = os.path.join(output_dir, url.split("/")[-1])
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as f, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)

def on_progress(stream, chunk, bytes_remaining):
    """
    Callback function to display progress for YouTube video downloads.
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"\rDownloading {stream.title}: {percentage:.2f}%", end="")

def download_youtube(url, output_dir):
    """
    Downloads a YouTube video from the given URL to the output directory.
    Uses pytube and displays progress via the on_progress callback.
    """
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=output_dir)
    print(f"\nDownloaded {yt.title} to {output_dir}")

def download(url, output_dir):
    """
    Determines whether the URL is a YouTube video or a regular file and downloads it accordingly.
    Handles errors gracefully.
    """
    try:
        if "youtube.com" in url or "youtu.be" in url:
            download_youtube(url, output_dir)
        else:
            download_file(url, output_dir)
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    """
    Main function to parse command-line arguments and initiate concurrent downloads.
    """
    parser = argparse.ArgumentParser(description="Everything Downloader by Muhammad Saleh, CC Education System")
    parser.add_argument("urls", nargs="+", help="URLs to download, separated by spaces")
    parser.add_argument("-o", "--output", default="downloads", help="Output directory (default: 'downloads')")
    parser.add_argument("-c", "--concurrency", type=int, default=5, help="Number of concurrent downloads (default: 5)")
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)
    
    # Use ThreadPoolExecutor for concurrent downloads
    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        for url in args.urls:
            executor.submit(download, url, args.output)

if __name__ == "__main__":
    main()
