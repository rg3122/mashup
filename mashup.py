from pytube import YouTube
from pydub import AudioSegment
import urllib.request
import re
import os
import sys


def main():
    delete_after_use = True
    if len(sys.argv) == 5:
        x = sys.argv[1]
        x = x.replace(' ','') + "songs"
        n = int(sys.argv[2])
        y = int(sys.argv[3])

    
        output_name = sys.argv[4]
    else:
        sys.exit('Arguments<4 ')
    

    url = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + str(x))

    vd = re.findall(r"watch\?v=(\S{11})", url.read().decode())

    for i in range(n):
        yt = YouTube("https://www.youtube.com/watch?v=" + vd[i]) 
        
        audfiles = yt.streams.filter(only_audio=True).first().download(filename='Vidtoaudio-'+str(i)+'.mp3')

    print("Download Complete")
    

    if os.path.isfile("vidtoaudio-0.mp3"):
        final = AudioSegment.from_file("vidtoaudio-0.mp3")[0:y*1000]
    for i in range(1,n):
        aud_file = str(os.getcwd()) + "/Vidtoaudio-"+str(i)+".mp3"
        final = final.append(AudioSegment.from_file(aud_file)[0:y*1000],crossfade=1000)
  

    final.export(output_name, format="mp3")
    print("Output File " + str(output_name))
    
        
    if delete_after_use:
        for i in range(n):
            os.remove("vidtoaudio-"+str(i)+".mp3")


if __name__ == '__main__':
    main()