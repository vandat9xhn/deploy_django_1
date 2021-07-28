from django.urls import path
#
from . import views

#


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.logout),
    path('define-user/', views.DefineUser.as_view()),
    path('refresh-token/', views.CustomTokenRefreshView.as_view()),
]
