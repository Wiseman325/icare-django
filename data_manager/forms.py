from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Case, roomForum, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']


class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        exclude = ['user','status']


class RoomForm(ModelForm):
    class Meta:
        model = roomForum
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'avatar', 'name', 'email', 'phone_number']
