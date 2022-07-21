from django.urls import path
from users.api.v1.views import GetAuthToken ,Logout, UserCreateAPIView, UserRetrieveAPIView

app_name = 'user'

urlpatterns = [
  path('token/',GetAuthToken.as_view()),
  path('logout/', Logout.as_view()),

  path('user/<int:pk>', UserRetrieveAPIView.as_view()),
  path('user/create', UserCreateAPIView.as_view()),

]
