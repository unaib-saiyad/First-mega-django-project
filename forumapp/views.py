from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from login.models import Login


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
        params = {"user": user, "login": login}
        return render(request, "forum/forum.html", params)


def add_forum(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        tags = request.POST.get('tags')
        textarea = request.POST.get('textarea')
        print(subject, tags, textarea)

        return HttpResponse(f'''Subject: {subject}<br>Tags: {tags}<br><br>{textarea}''')
    else:
        return render(request, "forum/add-forum.html")
