from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Case, roomForum, User, EvidenceFile
from django import forms
from datetime import date
from django.utils import timezone
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']


class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        exclude = ['user','status', 'status_reason', 'assigned_officer']

    def clean_incident_date(self):
        incident_date = self.cleaned_data.get('incident_date')

        if incident_date:
            now = timezone.now()
            # Prevent future date/time
            if incident_date > now:
                raise ValidationError("Incident date and time cannot be in the future.")

        return incident_date

class EvidenceUploadForm(forms.ModelForm):
    class Meta:
        model = EvidenceFile
        fields = ['file', 'description', 'category', 'date_collected']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = False


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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'avatar', 'name', 'username', 'email', 'phone_number',
            'age', 'gender', 'address', 'id_number',
            'badge_number', 'rank', 'station', 'speciality', 'years_of_service',
            'management_level'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserForm, self).__init__(*args, **kwargs)

        if user:
            if user.role == 'citizen':
                exclude_fields = [
                    'badge_number', 'rank', 'station', 'speciality',
                    'years_of_service', 'management_level'
                ]
            elif user.role == 'officer':
                exclude_fields = ['management_level', 'id_number', 'address', 'age', 'gender']
            else:  # commander
                exclude_fields = ['id_number', 'address', 'age', 'gender', 'speciality', 'rank', 'years_of_service', 'station']

            for field in exclude_fields:
                if field in self.fields:
                    self.fields.pop(field)

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        id_number = cleaned_data.get('id_number')

        if id_number and len(id_number) >= 6:
            try:
                dob_str = id_number[:6]  # YYMMDD
                year = int(dob_str[:2])
                month = int(dob_str[2:4])
                day = int(dob_str[4:6])

                # Assume 1900s if year > current YY
                current_year = date.today().year % 100
                full_year = 1900 + year if year > current_year else 2000 + year
                dob = date(full_year, month, day)

                today = date.today()
                calculated_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

                if age and calculated_age != age:
                    self.add_error('age', f"Entered age ({age}) does not match ID number (calculated age: {calculated_age})")
            except Exception:
                self.add_error('id_number', "Could not extract valid date from ID number.")

        return cleaned_data
