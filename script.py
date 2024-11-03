from pytubefix import YouTube

link = str(input("Video URL > "))
decision = ""

# 
if link != "":
    yt = YouTube(link)

    while decision == "":
        print("1 - Get highest quality\n2 - Download audio\n0 - Exit")
        decision = str(input())
        match decision:
            case "1":
                print("Downloading video in highest quality.")
                streams = yt.streams.get_highest_resolution().download(output_path="./DownloadedMedia")
            case "2":
                print("Downloading the audio from the video.")
                streams = yt.streams.get_audio_only().download(
                    output_path="./DownloadedMedia",
                    mp3=True
                    )
            case "0":
                print("Exiting")
                break
            case _:
                print("Invalid option")    
                break 
        decision = ""
        
else:
    print("Invalid URL")
    
