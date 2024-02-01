# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import *
# from django.views.generic import ListView
# def register(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login page after successful registration

#     return render(request, 'registration/register.html', {"form": form})


# def home(request):
#     return render(request, "base.html")
# def registration(request):
#     if request.method == 'POST':
#         usermodel = UserProfile()
#         usermodel.username = request.POST['username']
#         usermodel.email = request.POST['email']
#         usermodel.password = request.POST['password']
#         usermodel.save()
#         print(request.POST)
#         # data = request.POST
#         return redirect("/register/")
    
#     data = UserProfile.objects.all()

#     return render(request,'myName/register.html')
    
# def showdata(request):
#     data=UserProfile.objects.all()
#     print('--------',data)
#     return render(request,'myName/userdata.html',{"data": data} )


# def editdata(request, id):
#     if request.method == "POST":
#         editedUser = UserProfile.objects.get(id = id)
#         editedUser.email = request.POST['email']
#         editedUser.username = request.POST['username']
#         editedUser.password = request.POST['password']
#         editedUser.save()

#         # data = UserProfile.objects.all()
#         return redirect("/data/")
#     # data=UserProfile.objects.all()
#     user = UserProfile.objects.get(id = id)
#     print(user)
#     # form=RegistrationForm(instance=UserProfile)

#     return render(request,'myName/update.html',{"user":user} )
# def deletedata(request,id):
#     return redirect("/data/")
#     UserProfile.objects.get(id=id).data.delete()
#     if request.method=="POST":
#     #  data.delete()
#     # data= UserProfile.objects.get(id = id)
#         print(data)
#     # form=RegistrationForm(instance=UserProfile)

#         return render(request,'myName/userdata.html',context={"data":data} )
#     return HttpResponse("Data deleted successfully")
#     messages.info(request,"data deleted succesfully")
#     return render(request, "myName/userdata.html")

# def RegistrationForm(request):

#     if request.method=='POST':
#         print(request.POST)

#         return redirect ('register')
#     return render (request,'form.html')




from rest_framework.generics import ListAPIView
from .forms import *

# class listData(ListAPIView):
#     serializer_class = RegistrationForm
#     queryset = UserProfile.objects.all()

from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,CreateAPIView ,RetrieveUpdateDestroyAPIView
from .models import UserProfile
from .serializers import UserProfileSerializer
# from rest_framework.decorators import api_view
# @api_view(['GET'])
class RegistrationpostView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# class RegistrationgetView(ListAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

# class RegistrationViewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'

        