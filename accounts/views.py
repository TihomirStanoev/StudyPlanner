from rest_framework import generics
from accounts.serializer import RegisterSerializer



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
