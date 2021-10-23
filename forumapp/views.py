import os
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from login.models import Login
from .models import Forum


# Create your views here.
def index(request):
    if request.method == "POST":
        return JsonResponse({"status": False, "Message": "wrong request!..."})
    else:
        if request.user.is_authenticated:
            user = request.user
            if Login.objects.filter(user=user).exists():
                login = Login.objects.filter(user=user).get()
            else:
                login = ""
        else:
            user = "anonymous-user"
            login = ""
        try:
            forums = Forum.objects.all()
        except:
            forums = None
        params = {"user": user, "login": login, "forums": forums}
        return render(request, "forum/forum.html", params)


def imgProcess(file, user):
    try:
        img = Image.open(file)
        image_format = ['JPEG', 'PNG', 'TIFF', 'EPS', 'RAW']
        if img.format in image_format:
            img.thumbnail((640, 480), Image.ANTIALIAS)
            thumbnailString = BytesIO()
            if file.size > 5242880:
                img.save(thumbnailString, 'JPEG', quality=50)
            else:
                img.save(thumbnailString, 'JPEG', quality=100)
            newFile = InMemoryUploadedFile(thumbnailString, None, f'{user}.jpg', 'image/jpeg',
                                           thumbnailString,
                                           None)
            return newFile
        else:
            return None
    except:
        return JsonResponse({"Status": False, "Message": "Something went wrong while opening the file!..."})


def add_forum(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            subject = request.POST.get('subject')
            tags = request.POST.get('tags')
            languages = request.POST.get('languages')
            textarea = request.POST.get('textarea')
            file = request.FILES['image']
            if (subject and tags and languages and textarea) != "":
                if file is not None:
                    newfile = imgProcess(file, user.username)
                else:
                    newfile = ''
                Forum.objects.create(user=user, subject=subject, tags=tags, languages=languages, body=textarea,
                                     image=newfile)
            else:
                return JsonResponse({'Status': False, 'Error': 'Required fields are empty!...'})
            return JsonResponse({'status': True, 'Message': 'Your response hase been successfully saved'})
        else:
            return JsonResponse({'status': False, 'Message': 'User is not authenticated!...'})
    else:
        return render(request, "forum/add-forum.html")


def open_forum(request, username=None):
    return JsonResponse({'status': True, 'Message': f'Done with {username}'})
