from multiprocessing.util import ForkAwareThreadLock
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MyUserForm(UserCreationForm):
   email=forms.EmailField(required=True,label='Email')

   class Meta:
    model=User
    fields=['username','email','password1','password2']
def save(self,commit=True):
    user=super(UserCreationForm,self).save(commit=False)
    user.email=self.changed_data['email']
    if commit:
        user.save()

