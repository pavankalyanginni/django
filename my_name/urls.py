# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # your existing URLs
    # path('', home, name='register'),
    path("register/", RegistrationpostView.as_view(), name="regsitrationpostview"),
    path("update/<int:id>", UserProfileDetailView.as_view(), name="UserProfileDetailView"),
    # path("get/", RegistrationgetView.as_view(), name="regsitrationgetview"),
    # path("data/", showdata, name="showdata"),
    # path("editdata/<int:id>", editdata, name="editdata"),
    # path("deletedata/<int:id>", deletedata, name="deletedata"),
    # path('listdata',listData().as_view())
    # path('data/edit/<int:id>/', editdata, name='editdata'),
    # path('data/delete/<int:id>/', deletedata, name='deletedata'),
    #  path('updatedata/<int:id>/', RegistrationViewRetrieveUpdateDestroyView.as_view(), name='Registrationview-retrieve-update-destroy'),
]


