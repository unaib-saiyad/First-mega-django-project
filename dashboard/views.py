from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from login.models import Login
from .models import Query


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
        if request.user.is_authenticated:
            user = request.user
            username = request.POST.get('username')
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip = request.POST.get('zip')
            query = request.POST.get('query')
            if (username and fullname and email and mobile and city and state and zip and query) == "":
                return JsonResponse({"status": False, "Error": "Fields should not be empty!..."})
            if username != user.username:
                return JsonResponse({"status": False, "Error": "Incorrect username!..."})
            Query.objects.create(username=username, fullname=fullname, email=email, mobile=mobile,
                                 city=city, state=state, zip=zip, query=query)
            if Login.objects.filter(user=user).exists():
                login = Login.objects.filter(user=user).get()
            else:
                login = ""
            params = {"user": user, "login": login, "messages": ["Your response have been saved Successfully..."]}
        else:
            return JsonResponse({"status": False, "Message": "User is not authenticated!..."})
        return render(request, 'dashboard/contact.html', params)

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
