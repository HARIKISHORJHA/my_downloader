from django.shortcuts import render,HttpResponse
from django.contrib import messages
from pytube import YouTube
from pathlib import Path
#from tqdm import tqdm
#import time
from django.views.decorators.csrf import csrf_protect
#Create your views here.
def home(request):
    return render(request,"index.html")
def index(request):
    return render(request,"index.html")
def service(request):
    try:
        if request.method=="POST":
            url=request.POST.get("name", None)
            #messages.info(request,message="Download processing.. please wait..")
            #download(url)
            yt=YouTube(url)
            video=yt.streams.first()
            video.download()
            message="Successfully Downloaded...."
            context={"variable":message}
        return render(request,"next.html",context)
    except Exception as e:
        print("error: ",e)
        return HttpResponse("Something went wrong..... check your url or check your connection.")
#def download(url):
    
    #SAVE_PATH= str(Path.home() / "Downloads")

    #yt = YouTube(url) 
    
    #video=yt.streams.first() #it will fetch the first stream of the video
    #video.download(SAVE_PATH)
    #video.download()