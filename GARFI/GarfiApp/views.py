from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,View
from GarfiApp.models import UserAccount,Code
from django import forms
import random
# Create your views here.



class HomePage(TemplateView):

    template_name = 'GarfiApp/homepage.html'


class AboutPage(TemplateView):

    template_name = 'GarfiApp/aboutpage.html'

def SignUp(request):

    return render(request,"GarfiApp/signup_page.html")

def SignUpSuccess(request):
    user = UserAccount.objects.all()

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('mobilenumber')
        password = request.POST.get('password')

        data = UserAccount.objects.create(firstname = firstname , lastname = lastname , email = email , mobilenumber = mobilenumber , password = password, points=0)
        data.save()


        return render(request,"GarfiApp/signup_success.html")


def LoginPage(request):

    return render (request, "GarfiApp/loginpage.html")

def UserHome(request):

    user = UserAccount.objects.all()

    if request.method == 'POST':
        global code
        code = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
        user = UserAccount.objects.all()
        data = Code.objects.create(code = str(code))
        data.save()
        print(code)

        email = request.POST.get('email')
        password = request.POST.get('password')

        for item in user:

            if item.email == email and item.password == password:


                break
        dict = {'email': email,'password':password,'firstname':item.firstname,'lastname':item.lastname,'points':item.points}
        return render (request,"GarfiApp/user_home.html", context = {'dict': dict, 'code':code} )



def InputCode(request):

    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        code = request.POST.get('code')
        user_details = {'name':name,'email':email,'password':password}


        return render(request,"GarfiApp/code.html", {'user': user_details,'code':code})

def SavePoints(request):

    if request.method == 'POST':

        user = UserAccount.objects.all()
        #data = Code.objects.all()

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        input_code = request.POST.get('input-code')


        for item in user:

            if (item.email == email and item.password == password):
                print('SavePoints')
                print(code)
                print(name)
                print(email)
                print(password)

                if input_code == code:
                    item.points += 10
                    cond = True
                    item.save()
                    Code.objects.all().delete()
                    break
                else:

                    cond=False
                    break

        if cond == True:
            return render(request,"GarfiApp/save_points.html", {'cond':True})
        else:
            return render(request,"GarfiApp/save_points.html", {'cond':False})



# def CodeVer(request):
#
#     cloudcode = Code.objects.all()
#     if request.method == 'POST':
#
#         code = request.POST.get('code')
#
#         if cloudcode.code == code:
#
#             return HttpResponse("Codes match!")








# class LoginPage(View):
#
#     pass
