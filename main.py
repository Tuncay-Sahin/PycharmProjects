import pytube

url = input("enter video url: ")


pytube.YouTube(url).streams.get_highest_resolution().download