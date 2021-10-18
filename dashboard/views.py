from django.shortcuts import render

# Create your views here.
from django.views import View


class Dashboard(View):
    def post(self, request):
        return None

    def get(self, request):
        return render(request, 'dashboard/index.html')
