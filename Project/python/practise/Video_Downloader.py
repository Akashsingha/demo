from pytube import YouTube
# from tqdm import tqdm
import pyperclip

link = pyperclip.paste()
Video_Save = "C:\\Users\\AKASH\\Desktop\\python\\practise\\Video" 

try:
    url = YouTube(link)
    print("Getting video ready..")
    video = url.streams.get_highest_resolution()

    print("Downloding.......")
    video.download(Video_Save)

    print("Video Downloaded Sucessfully!!")

except:
    print("Something went wrong!!!")