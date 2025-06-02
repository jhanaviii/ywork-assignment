from django.urls import path
from .views import EntryCreateAPIView, EntryListAPIView

urlpatterns = [
    path('add/', EntryCreateAPIView.as_view(), name='entry-add'),
    path('fetch/', EntryListAPIView.as_view(), name='entry-fetch'),
]
