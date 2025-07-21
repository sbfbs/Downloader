# Everything Downloader

**Everything Downloader** is a powerful and versatile command-line tool designed to download multiple URLs simultaneously, including multimedia content like YouTube videos. Created by **Muhammad Saleh** from **CC Education System**, this tool is built to be efficient, user-friendly, and highly capable with advanced features.

## Features

- **Multiple URL Downloads**: Download multiple files or videos at once by providing URLs separated by spaces.
- **YouTube Video Support**: Seamlessly download YouTube videos in the highest available resolution.
- **Concurrent Downloads**: Speed up the downloading process with configurable concurrent downloads.
- **Progress Tracking**: Monitor the progress of each download with detailed progress bars for files and percentage updates for YouTube videos.
- **Error Handling**: Gracefully handles errors such as invalid URLs, network issues, or unsupported content.
- **Customizable Output**: Specify the output directory for your downloads.

## Installation

To use Everything Downloader, ensure you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install requests pytube tqdm
```

### Prerequisites
- Python 3.6 or higher
- An active internet connection

## Usage

Run the script using the following command in your terminal or command prompt:

```bash
python everything_downloader.py [urls] [-o OUTPUT] [-c CONCURRENCY]
```

### Arguments
- **`urls`**: One or more URLs to download, separated by spaces. (Required)
- **`-o OUTPUT`, `--output OUTPUT`**: Specify the directory where files will be saved. (Optional, default: "downloads")
- **`-c CONCURRENCY`, `--concurrency CONCURRENCY`**: Set the number of simultaneous downloads. (Optional, default: 5)

### Detailed Instructions
1. **Open a terminal**: Navigate to the directory containing `everything_downloader.py`.
2. **Run the script**: Use the command format above, replacing `[urls]` with your list of URLs.
3. **Monitor progress**: The script will display progress bars for regular files and percentage updates for YouTube videos.
4. **Check output**: Once completed, find your downloaded files in the specified output directory (or "downloads" by default).

### Examples

1. **Download a single file**:
   ```bash
   python everything_downloader.py https://example.com/file.zip
   ```
   Downloads `file.zip` to the "downloads" directory with a progress bar.

2. **Download multiple files**:
   ```bash
   python everything_downloader.py https://example.com/file1.zip https://example.com/file2.zip
   ```
   Downloads both files concurrently to the "downloads" directory.

3. **Download a YouTube video**:
   ```bash
   python everything_downloader.py https://www.youtube.com/watch?v=video_id
   ```
   Downloads the YouTube video in the highest resolution to the "downloads" directory with progress updates.

4. **Download multiple YouTube videos with a custom output directory**:
   ```bash
   python everything_downloader.py https://www.youtube.com/watch?v=video1 https://www.youtube.com/watch?v=video2 -o my_videos
   ```
   Downloads both videos to the "my_videos" directory.

5. **Adjust concurrency for faster downloads**:
   ```bash
   python everything_downloader.py https://example.com/file1.zip https://example.com/file2.zip -c 10
   ```
   Downloads both files with up to 10 concurrent threads.

### Notes
- Ensure URLs are valid and accessible. Invalid URLs will display an error message and continue with the next download.
- For YouTube videos, the highest resolution available is downloaded, typically in MP4 format.
- Large concurrency values may depend on your system's capabilities and network speed.

## Contact

For support, feedback, or inquiries, please reach out to:
- **Email**: developinc3@gmail.com, developinc4@gmail.com, msxmsxmsx3339@gmail.com
- **Phone**: 03455098100

**Creator**: Muhammad Saleh, CC Education System

---

Everything Downloader combines power and simplicity, making it your go-to tool for all downloading needs. Whether it's a single file or a batch of multimedia content, this tool handles it with ease and efficiency. Start downloading like a pro today!
