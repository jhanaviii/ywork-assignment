from rest_framework import generics, permissions
from .models import Entry
from .serializers import EntrySerializer

class EntryCreateAPIView(generics.CreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_email=self.request.user.email)

class EntryListAPIView(generics.ListAPIView):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Entry.objects.filter(user_email=self.request.user.email)
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset
