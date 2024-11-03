from pytubefix import YouTube

link = str(input("Video URL > "))
decision = ""

if link != "":
    yt = YouTube(link)

    while decision == "":
        print("1 - Get highest quality\n2 - Download audio")
        decision = str(input())
        match decision:
            case "1":
                print("Downloading video in highest quality.")
                streams = yt.streams.get_highest_resolution().download()
            case "2":
                print("Downloading the audio from the video.")
                streams = yt.streams.get_audio_only().download(mp3=True)
            case _:
                print("Invalid option")    
                break 
        decision = ""
        
else:
    print("Invalid URL")
    
