from django.forms import ModelForm
from .models import Case, roomForum

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'


class RoomForm(ModelForm):
    class Meta:
        model = roomForum
        fields = '__all__'
        exclude = ['host', 'participants']