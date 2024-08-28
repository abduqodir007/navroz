from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegsiterSuper(UserCreationForm):
    class Meta:
        model = User
        fileds = ['username','password1','password2']