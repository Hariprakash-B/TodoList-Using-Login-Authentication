from django import forms
from .models import *
class ContactForm(forms.Form):
    name=forms.CharField( max_length=50)
    email= forms.EmailField()
    password=forms.CharField(max_length=50)
    def clean(self):
        super(ContactForm, self).clean()

      # getting username and password from cleaned_data
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
      # validating the username and password
        print(type(name),type(password),'hello')
        for hari in login.objects.all():
            print(hari.name,name)
            if(name==hari.name):
                self._errors['name'] = self.error_class(['A Name is already in use'])
        if len(str(name)) < 5:
               self._errors['name'] = self.error_class(['A minimum of 5 characters is required'])

        if len(str(password)) < 8:
           self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])

        return self.cleaned_data    

class loginForm(forms.Form):
    name=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
    def clean(self):
        super(loginForm, self).clean()

      # getting username and password from cleaned_data
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        name=str(name)
        password=str(password)
      # validating the username and password
        print(type(name),type(password),'hellologin')
        temp=1
        if name in login.objects.values_list('name', flat=True):
              if password in login.objects.values_list('password', flat=True):
                    place=login.objects.get(name=name)
                    if(password==place.password):
                        pass
                    else:
                      self._errors['password'] = self.error_class(['invalid password'])      
              else:
                self._errors['password'] = self.error_class(['invalid password'])    
        else:
              self._errors['name'] = self.error_class(['invalid username']) 
        if len(str(name)) < 5:
            self._errors['name'] = self.error_class(['A minimum of 5 characters is required'])
        if len(str(password)) < 8:
           self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])
        return self.cleaned_data    
class taskform(forms.ModelForm):
    class Meta:
        model = taskmodel
        fields='__all__'