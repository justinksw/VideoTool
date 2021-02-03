from pytube import YouTube

url = 'https://youtu.be/P9U1kwg6toY'
YouTube(url).streams.get_highest_resolution().download()

