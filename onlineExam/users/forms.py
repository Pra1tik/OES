from django import forms
from .models import User, Student, Teacher
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

class studentRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.isStudent = True
        user.save()
        student = Student.objects.create(user=user, first_name=user.first_name, last_name=user.last_name)
       
        return user


class teacherRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.isTeacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        return user



