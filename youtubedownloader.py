from pytube import YouTube

Link  = input('Enter the link')

yt = YouTube(Link)
print('title: ',yt.title)

print('number of views :',yt.views)

print('Length of vedio :',yt.length,'seconds')

print("Description: ",yt.description)

print("Ratings",yt.rating)

print(yt.streams)

print(yt.streams.filter(only_audio=True))
print(yt.streams.filter(only_video=True))

print(yt.streams.filter(progressive=True))

ys = yt.streams.get_highest_resolution()
ys = yt.streams.get_by_itag('22')
ys.download()
ys.download('location')
