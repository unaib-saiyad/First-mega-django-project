import base64
import datetime
import json
import os
from io import BytesIO

from PIL import Image
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from forum.settings import SECRET_KEY

from .models import Login, UserUrl, UserWork


class SingupIn(View):
    def post(self, request):
        """
        :param request:
            Signup:
                email, username, password
            Signin:
                email, password
        :return:
            success / fail
            => user
        """
        email = request.POST.get('signup-email')
        username = request.POST.get('signup-username')
        password = request.POST.get('signup-password')

        login_username = request.POST.get('signin-username')
        login_password = request.POST.get('signin-password')

        if email or username or password != "":
            if User.objects.filter(username=username).count() != 0:
                return render(request, "login/login-signup.html",
                              {'error': 'Something Went Wrong', 'message': "User Already Exist"})
            try:
                User.objects.create_user(username=username, email=email, password=password)
                user_obj = authenticate(username=username, password=password)
                auth_login(request, user_obj)
                return redirect("user-profile/", user_obj)
            except:
                User.objects.filter(username=username).delete()
                return render(request, "login/login-signup.html",
                              {'error': 'Something Went Wrong',
                               'message': "Some data is Not Satisfies like: Username, Password, Email"})

        else:
            if User.objects.filter(username=login_username).count() == 0:
                return render(request, "error/index.html",
                              {'error': '''Username doesn't exist!...''',
                               'message': "This username doesn't exist please make sure you have spelled correctly"})
            user_obj = authenticate(request, username=login_username, password=login_password)
            if user_obj is None:
                return render(request, "error/index.html",
                              {'error': 'Wrong password entered!...',
                               'message': "password doesn't match please check it twice and try again"})
            auth_login(request, user_obj)
            return redirect("user-profile/", user_obj)

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            try:
                login = Login.objects.filter(user=user).get()
            except:
                login = ""
            params = {'user': user, 'login': login}
            return redirect("user-profile/", params)
        return render(request, "login/login-signup.html",
                      {'error': 'Wrong Method',
                       'message': "Only POST method Allowed"})


class Profile(View):
    def post(self, request):
        """
        :param request:
            userdata
        :return:
            success / fail
        """
        if request.user.is_authenticated:
            user = request.user
            username = request.POST.get('username')
            email = request.POST.get('email')
            full_name = request.POST.get('fullname')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            tag = request.POST.get('tag', '')
            website = request.POST.get('website')
            github = request.POST.get('github')
            twitter = request.POST.get('twitter')
            instagram = request.POST.get('instagram')
            facebook = request.POST.get('facebook')
            list_of_para = ['first', 'second', 'third', 'fourth', 'fifth']
            element_of_titles = []
            element_of_progress = []
            for element in list_of_para:
                element_of_titles.append(request.POST.get(f'{element}' + '-title', ""))
                element_of_progress.append(request.POST.get(f'{element}' + '-progress'))
            for element in element_of_progress:
                if element == "":
                    element_of_progress[element_of_progress.index(element)] = 0

            if username == "" or email == "" or full_name == "" or mobile == "" or address == "":
                return JsonResponse({'status': False,
                                     'massage': "Required fields are empty!..."
                                     })
            if user.username != username or email != user.email:
                if user.username != username and User.objects.filter(username=username).exists():
                    return JsonResponse({'status': False,
                                         'massage': "Username already exists!..."
                                         })
                try:
                    if Login.objects.filter(user=user).exists():
                        login = Login.objects.filter(user=user).get()
                    else:
                        login = ''

                    if UserUrl.objects.filter(user=user).exists():
                        user_urls = UserUrl.objects.filter(user=user).get()
                    else:
                        user_urls = ''
                    if UserWork.objects.filter(user=user).exists():
                        user_work = UserWork.objects.filter(user=user).get()
                    else:
                        user_work = ''

                    user.username = username
                    user.email = email
                    user.save()
                    if login != '':
                        login.user = user
                        login.save()

                    if user_urls != '':
                        user_urls.user = user
                        user_urls.save()

                    if user_work != '':
                        user_work.user = user
                        user_work.save()


                except:
                    return JsonResponse({'status': False,
                                         'massage': "Cant get user login details!..."
                                         })
            if Login.objects.filter(user=user).exists():
                Login.objects.filter(user=user).update(full_name=full_name, mobile=mobile, Address=address, tag=tag)
                login = Login.objects.filter(user=user).get()
            else:
                login = Login.objects.create(user=user, full_name=full_name, mobile=mobile, Address=address,
                                             tag=tag)

            if UserUrl.objects.filter(user=user).exists():
                UserUrl.objects.filter(user=user).update(website=website, github=github, twitter=twitter,
                                                         facebook=facebook, instagram=instagram)
                urls = UserUrl.objects.filter(user=user).get()
            else:
                urls = UserUrl.objects.create(user=user, website=website, github=github, twitter=twitter,
                                              facebook=facebook, instagram=instagram)

            if UserWork.objects.filter(user=user).exists():
                UserWork.objects.filter(user=user).update(work_title_1=element_of_titles[0],
                                                          work_title_2=element_of_titles[1],
                                                          work_title_3=element_of_titles[2],
                                                          work_title_4=element_of_titles[3],
                                                          work_title_5=element_of_titles[4],
                                                          work_val_1=element_of_progress[0],
                                                          work_val_2=element_of_progress[1],
                                                          work_val_3=element_of_progress[2],
                                                          work_val_4=element_of_progress[3],
                                                          work_val_5=element_of_progress[4])
                progress = UserWork.objects.filter(user=user).get()
            else:
                progress = UserWork.objects.create(user=user, work_title_1=element_of_titles[0],
                                                   work_title_2=element_of_titles[1],
                                                   work_title_3=element_of_titles[2], work_title_4=element_of_titles[3],
                                                   work_title_5=element_of_titles[4], work_val_1=element_of_progress[0],
                                                   work_val_2=element_of_progress[1], work_val_3=element_of_progress[2],
                                                   work_val_4=element_of_progress[3], work_val_5=element_of_progress[4])

            params = {'user': user, 'login': login, 'urls': urls, 'progress': progress}
            return render(request, 'login/user_profile.html', params)
        return redirect('../')

    def get(self, request):
        """
            :param request:
                user-authentication
            :return:
                True/False
        """
        if request.user.is_authenticated:
            user = request.user
            messages = []
            try:
                login = Login.objects.filter(user=user).get()
            except:
                login = Login.objects.create(user=user)
            try:
                urls = UserUrl.objects.filter(user=user).get()
            except:
                urls = ""
            try:
                progress = UserWork.objects.filter(user=user).get()
            except:
                progress = ""
            if (login.full_name and login.mobile and login.Address and user.email) == "":
                messages.append('Please enter fullname, email, mobile-number and address properly')
            params = {'user': user, 'login': login, 'urls': urls, 'progress': progress, "messages": messages}
            return render(request, 'login/user_profile.html', params)
        else:
            return redirect('../')


class Logout(View):
    """
        :param request:
            user should authenticated
        :return:
            True/False
    """

    def post(self, request):
        return JsonResponse({'error': 'Wrong request',
                             'message': "Only get request is allowed!..."})

    def get(self, request):
        if request.user.is_authenticated:
            auth_logout(request)
            return redirect('../')
        return JsonResponse({'error': 'User us not login!...',
                             'message': "You cant logout before login"})


class Avtar(View):
    """
        :param request:
            user-authentication, profile-image
        :return:
            True/False
    """

    def imgProcess(self, file, user, login):
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
                if login != "" and login != 'default.png':
                    os.remove(login.path)
                newFile = InMemoryUploadedFile(thumbnailString, None, f'{user}.jpg', 'image/jpeg',
                                               thumbnailString,
                                               None)
                return newFile
            else:
                return None
        except:
            return JsonResponse({"Status": False, "Message": "Something went wrong while opening the file!..."})

    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            file = request.FILES.get('avtar')
            if file is None:
                return redirect("../")
            if Login.objects.filter(user=user).exists():
                login = Login.objects.filter(user=user).get()
                newFile = self.imgProcess(file, user.username, login.avtar)
                if newFile is None:
                    return JsonResponse({'error': 'Wrong file',
                                         'message': "Only image file accepted!..."})
                login.avtar = newFile
                login.save()
            else:
                newFile = self.imgProcess(file, user.username, "")
                if newFile is None:
                    return JsonResponse({'error': 'Wrong file',
                                         'message': "Only image file accepted!..."})
                login = Login.objects.create(user=user, full_name="", mobile="", Address="",
                                             tag="", avtar=newFile)
            return redirect('../')

    def get(self, request):
        return JsonResponse({'error': 'Wrong request',
                             'message': "Only post request is allowed!..."})


def key_maker(username):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'\xcfz\xfc\xdcF\xc1d\xc1\xb4\xfa5%\xe7\xa5\x14\x16',
        iterations=100000,
        backend=default_backend()
    )
    return Fernet(base64.urlsafe_b64encode(kdf.derive(str(SECRET_KEY + username[::-1]).encode())))


class ForgotPass(View):
    """
        :param request:
            username, email
        :return:
            True/False
    """

    def post(self, request):
        username = request.POST.get('username')
        if username == "":
            return JsonResponse({"error": "Required fields are empty!...",
                                 "massage": "Please enter username properly and try again later"})
        try:
            user_obj = User.objects.filter(username=username).get()
        except:
            return JsonResponse({"error": "Username doesn't exist!...",
                                 'massage': "Username is incorrect please enter the correct username"})
        email = user_obj.email
        key = key_maker(username)
        data = {
            "username": username,
            "valid_time": str(datetime.datetime.today() + datetime.timedelta(minutes=30))
        }
        token = key.encrypt(json.dumps(data).encode()).decode()
        if user_obj.email == email:
            try:
                confirmation_email(user_obj, token)
                return JsonResponse({'status': True,
                                     'error': "Email sent successfully"
                                     })
            except:
                return JsonResponse({'error': '''Problem to sending email!...''',
                                     'message': "Problem when we try to send email, please try again later"})

        return JsonResponse({'error': '''Invalid email!...''',
                             'message': f"Username with {username} do not have email id connected"})

    def get(self, request):
        return render(request, 'login/forgot_pass.html')


class UpdatePassword(View):
    """
        :param request:
            username, old_password, new_password
        :return:
            True/False
    """

    def post(self, request):
        if request.user.is_authenticated:
            username = request.POST.get('username')
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            if username == "" or old_password == "" or new_password == "":
                return render(request, "error/index.html",
                              {'error': 'Wrong data entered!...',
                               'message': "Make sure you have filled every block properly"})
            if User.objects.filter(username=username).count() == 0:
                return render(request, "error/index.html",
                              {'error': '''Username doesn't exist!...''',
                               'message': "This username doesn't exist please make sure you have spelled correctly"})
            user_obj = authenticate(request, username=username, password=old_password)
            if user_obj is None:
                return render(request, "error/index.html",
                              {'error': '''Wrong password!...''',
                               'message': "password is not match with the username password"})
            User.objects.filter(username=username).update(password=new_password)
            return JsonResponse({'status': True,
                                 'Massage': "Password updated..."
                                 })
        return render(request, "error/index.html",
                      {'error': '''User is not login!...''',
                       'message': "Please login first with your id and try again"})

    def get(self, request):
        return JsonResponse({'status': False,
                             'error': "Only POST method Allowed..."
                             })


class NewPassGeneration(View):
    def post(self, request, username, token):
        key = key_maker(username)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return JsonResponse({"error": "No same password!...", "Message": "Please enter the same password"})
        try:
            data = key.decrypt(token.encode()).decode()
            data = json.loads(data)

            valid_time = datetime.datetime.strptime(data["valid_time"], '%Y-%m-%d %H:%M:%S.%f')

            if datetime.timedelta(minutes=0) <= valid_time - datetime.datetime.today() <= datetime.timedelta(
                    minutes=30) and username == data['username']:
                try:
                    user = User.objects.filter(username=username).get()
                    user.set_password(password1)
                    user.save()
                except:
                    return JsonResponse({'status': False,
                                         'error': "Unable to Extract user data...!"
                                         })

                return JsonResponse({
                    'username': username,
                    'data': data,
                    'valid_status': True
                })
            return JsonResponse({'status': False,
                                 'error': "Link is Not Valid...!"
                                 })

        except:
            return JsonResponse({'status': False,
                                 'error': "Something went wrong...!"
                                 })

    def get(self, request, username, token):
        key = key_maker(username)
        try:
            data = key.decrypt(token.encode()).decode()
            data = json.loads(data)
            valid_time = datetime.datetime.strptime(data["valid_time"], '%Y-%m-%d %H:%M:%S.%f')

            if datetime.timedelta(minutes=0) <= valid_time - datetime.datetime.today() <= datetime.timedelta(
                    minutes=30) and username == data['username']:
                params = {"username": username, "token": token}
            else:
                return JsonResponse({"Status": False, "Error": "Link is not valid!..."})
        except:
            return JsonResponse({"Message": "Something went wrong!..."})

        return render(request, 'login/new-pass-gen.html', params)


def confirmation_email(user, token):
    email_from = settings.EMAIL_HOST_USER
    message = '''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <h1>This email is from forum-web and team</h1>
    <h3>''' + str(user.username) + ''' wanted to reset login password at forum-web</h3>
    <p>Click the bellow button to reset password</p>
    <a href="http://127.0.0.1:8000/login/new_pass_gen/''' + str(user.username) + '/' + str(token) + '''
    ">Click Here to reset password</a>
    <h5>Link is valid for 30 minutes only</h5>
    <p>Don't click if it was not you!...</p>
  </body>
</html>'''
    try:
        send_mail(f"{user.username} wanted to reset login password", "Forum-web", email_from, [user.email, ],
                  fail_silently=False, html_message=message)
        return True
    except:
        return False
