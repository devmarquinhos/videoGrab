from pytubefix import YouTube

link = str(input("Video URL > "))

if link != "":
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution().download()
else:
    print("Invalid URL")
    
