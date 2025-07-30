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
        exclude = ['user','status', 'status_reason', 'assigned_officer']

class AssignOfficerForm(ModelForm):
    class Meta:
        model = Case
        fields = ['assigned_officer']

    
    def __init__(self, *args, **kwargs):
        super(AssignOfficerForm, self).__init__(*args, **kwargs)
        # Filter to only users who are officers
        self.fields['assigned_officer'].queryset = User.objects.filter(role='officer')

class CaseStatusForm(ModelForm):
    class Meta:
        model = Case
        fields = ['status', 'status_reason']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['assigned_officer'].required = False


class RoomForm(ModelForm):
    class Meta:
        model = roomForum
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'avatar', 'name', 'email', 'phone_number']
