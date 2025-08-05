from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.deletion import CASCADE


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('officer', 'Police Officer'),
        ('commander', 'Station Commander'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='citizen')  

        # ForeignKeys (normalized fields)
    rank = models.ForeignKey('Rank', null=True, blank=True, on_delete=models.SET_NULL)
    station = models.ForeignKey('Station', null=True, blank=True, on_delete=models.SET_NULL)
    speciality = models.ForeignKey('Speciality', null=True, blank=True, on_delete=models.SET_NULL)
    management_level = models.ForeignKey('ManagementLevel', null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.ForeignKey('Gender', null=True, blank=True, on_delete=models.SET_NULL)

    # Others
    badge_number = models.CharField(max_length=50, null=True, blank=True)
    years_of_service = models.IntegerField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username



class CaseType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Case(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    assigned_officer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_cases'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    case_type = models.ForeignKey(CaseType, on_delete=models.SET_NULL, null=True)
    incident_date = models.DateField(null=True, blank=True)  # new field
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    status_reason = models.TextField(max_length=2500, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', '-submitted_at']

    def __str__(self):
        return self.title

class CaseStatusHistory(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='status_history')
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    reason = models.TextField(max_length=2500, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.case.title} - {self.status.name} by {self.updated_by.username}"
    
class EvidenceFile(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='evidence_files')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='evidence/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.case.title} - {self.file.name}"

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class ManagementLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Gender(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class roomForum(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participants', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    room = models.ForeignKey(roomForum, on_delete=CASCADE)
    body = models.TextField(max_length=5000)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.body[:50]  # First 50 chars
