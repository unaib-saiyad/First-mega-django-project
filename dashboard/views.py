from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from login.models import Login


class Dashboard(View):
    def post(self, request):
        return JsonResponse({"status": False, "Message": "wrong request!..."})

    def get(self, request):
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
        return render(request, 'dashboard/index.html', params)


class About(View):
    def post(self, request):
        return JsonResponse({"status": False, "Message": "wrong request!..."})

    def get(self, request):
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
        return render(request, 'dashboard/about.html', params)


class Contact(View):
    def post(self, request):
        return JsonResponse({"status": False, "Message": "wrong request!..."})

    def get(self, request):
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
        return render(request, 'dashboard/contact.html', params)
