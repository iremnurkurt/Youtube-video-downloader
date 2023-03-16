from pytube import YouTube

# Enter the video URL
video_url = "https://www.youtube.com/watch?.."

# Create the YouTube object
yt = YouTube(video_url)

# list video qualities
for stream in yt.streams:
    print(stream)

# Select the video quality to download.
itag = input("Hangi kaliteyi indirmek istersiniz? (itag değeri): ")

#Download video
stream = yt.streams.get_by_itag(itag)
stream.download()
