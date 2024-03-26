from pytube import YouTube
import os
from pathlib import Path



video_link = input("Video link: ")

# Write a regular expression for the link 
# https://youtu.be/EKDSKynq0xs?list=PLgRZV-Axn6g7n6dmtVfQVnS75ZvKOZ8y9
# https://www.youtube.com/watch?v=EKDSKynq0xs&list=PLgRZV-Axn6g7n6dmtVfQVnS75ZvKOZ8y9&index=3&t=1s


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)}%")

# if the regular expression is true then make a youtube object
yt = YouTube(video_link,on_progress_callback=on_progress)


for stream in yt.streams.filter(progressive=True):
    print(stream)
    
itag = input("Itag: ")
    
path = input("Path: ")
path_to_download = os.path.join(os.path.expanduser("~"), path)

stream = yt.streams.get_by_itag(itag)
stream.download(path_to_download)