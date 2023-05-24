from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
# from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = None
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number=models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self) -> str:
        return self.first_name

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

ROLE_CHOICES = (
    ('HR', 'HR'),
    ('Manager', 'Manager'),
    ('Team Leader', 'Team Leader'),
    ('Python Developer', 'Python Developer'),
)

class EmployeeDetail(models.Model):
    emp_name = models.CharField(max_length=50, null=True, blank=True)
    emp_role = models.CharField(max_length=20, default="Python Developer", choices=ROLE_CHOICES)
    salary = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, default="Male", choices=GENDER_CHOICES)
    emp_code = models.CharField(max_length=70, null=True, blank=True) 
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Employee Name:- {self.emp_name}"
    
  