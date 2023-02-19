import sys 
import os
if len(sys.argv)!=5:
    print("Incorrect Number of Parameters")
    exit(0)
else:
    if(int(sys.argv[2])<=10):
        print("Videos must be greater than 10")
        exit(0)
    if(int(sys.argv[3])<=20):
        print("Trim size should be greater than 20sec")
        exit(0)
    if (".mp3" != (os.path.splitext(sys.argv[4]))[1]):
                print("ERROR : Output file extension is wrong")
                exit(0)

from youtube_search import YoutubeSearch
name=sys.argv[1]
n=int(sys.argv[2])
duration=int(sys.argv[3])
results = YoutubeSearch(name, max_results=n).to_dict()
link=['https://www.youtube.com/'+results[i]['url_suffix'] for i in range(n)]
from pytube import YouTube
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

for i in range(0,n):    
    Download(link[i])

directory = os.getcwd()


files = os.listdir(directory)


mp4_files = [file for file in files if file.endswith('.mp4')]

for file in mp4_files:
    print(file)

print(mp4_files)

from moviepy.editor import VideoFileClip,AudioFileClip

for i in range(0,len(mp4_files)):
    video = VideoFileClip(mp4_files[i])
    audio = video.audio
    audio.write_audiofile("audio_file"+str(i)+".mp3")

from pydub import AudioSegment

import os


directory = os.getcwd()

files = os.listdir(directory)

mp3_files = [file for file in files if file.endswith('.mp3')]

for file in mp3_files:
    print(file)

from moviepy.editor import *

# Load the audio file
audio = AudioFileClip(mp3_files[0])

# Trim the audio file
merged_audio = audio.subclip(0,0)
        

for i in range(0,len(mp3_files)):
    audio = AudioFileClip(mp3_files[i])
    trimmed=audio.subclip(0,duration)
    merged_audio = concatenate_audioclips([merged_audio, trimmed])
name1=sys.argv[4]
merged_audio.write_audiofile(name1)
