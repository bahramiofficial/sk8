from django.urls import path

from term.api.v1.views import (
    TermRetrieveUpdateDestroyAPIView,
    SessionAPIView,
TermListAPIView
)



app_name = 'term'

urlpatterns = [
    path('term/', TermListAPIView.as_view(), name='TermAPIView'),
    path('term/create', TermListAPIView.as_view(), name='TermListAPIView'),
    path('term/<int:pk>', TermRetrieveUpdateDestroyAPIView.as_view(), name='TermRetrieveUpdateDestroyAPIView'),
    path('session/', SessionAPIView.as_view(), name='SessionAPIView'),

]
