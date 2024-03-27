from pytube import YouTube, Playlist
import os
import re

# Constants
VIDEO_REGEX = r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+'
DEFAULT_PATH = os.path.join(os.path.expanduser("~"), 'Downloads')

# Functions
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)}%")

def get_validated_input(prompt, pattern=None):
    user_input = input(prompt)
    while pattern and not re.match(pattern, user_input):
        print("Invalid input. Please try again.")
        user_input = input(prompt)
    return user_input

def construct_path():
    path = input("Enter download directory path (leave empty for default): ").strip()
    if not path:
        return DEFAULT_PATH
    else:
        return os.path.join(os.path.expanduser("~"), path)

def download_video(video_url, path_to_download):
    video = YouTube(video_url, on_progress_callback=on_progress)
    print(f'Video title: {video.title}')
    stream = video.streams.filter(progressive=True).first()
    stream.download(path_to_download, on_progress=on_progress)
    print("Download completed.")

def download_playlist(playlist_url, path_to_download):
    playlist = Playlist(playlist_url)
    print(f'Downloading Playlist: {playlist.title}')
    for video in playlist.videos:
        print(f'Downloading: {video.title}')
        stream = video.streams.filter(progressive=True).first()
        stream.download(path_to_download, on_progress=on_progress)
    print("Download completed.")

# Main Script
if __name__ == "__main__":
    choose = get_validated_input("Download a Video (v) or Playlist (p): ", pattern=r'[VvPp]')
    url = get_validated_input("Enter the link: ", pattern=VIDEO_REGEX)
    path_to_download = construct_path()
    
    if choose.lower() == 'v':
        download_video(url, path_to_download)
    else:
        download_playlist(url, path_to_download)
