from pytube import YouTube, Playlist
import os

# Write a regular expression for the link 
# -------Video--------
# https://youtu.be/EKDSKynq0xs?list=PLgRZV-Axn6g7n6dmtVfQVnS75ZvKOZ8y9
# https://www.youtube.com/watch?v=EKDSKynq0xs&list=PLgRZV-Axn6g7n6dmtVfQVnS75ZvKOZ8y9&index=3&t=1s
# https://www.youtube.com/watch?v=vXukSWdjad4

# -------Playlist-----
# https://www.youtube.com/watch?v=41qgdwd3zAg&list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)}%")


choose = ''
choose = input("if you want to download a Video press v or Playlist p: ")

if choose == 'v' or choose == 'V':
    
    video_url = input("Video link: ")
    # if the regular expression is true then make a youtube object
    yt = YouTube(video_url,on_progress_callback=on_progress)


    for stream in yt.streams.filter(progressive=True):
        print(stream)
        
    itag = input("Itag: ")
        
    path = input("Path: ")
    path_to_download = os.path.join(os.path.expanduser("~"), path)

    stream = yt.streams.get_by_itag(itag)
    stream.download(path_to_download)
    
else:
    playlist_url = input("Playlist link: ")
    
    p = Playlist(playlist_url)
    
    print(f'Downloading: {p.title}')
    
    path = input("Path: ")
    path_to_download = os.path.join(os.path.expanduser("~"), path)
    
    for video in p.videos:
        
        print(video.title)
        
        stream = video.streams
        
        for stream in video.streams.filter(progressive=True):
            print(stream)    
            
        itag = input("Itag: ")

        stream = video.streams.get_by_itag(itag)
        stream.download(path_to_download)




