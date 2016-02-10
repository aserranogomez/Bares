from django import forms
from django.contrib.auth.models import User
from rango.models import Tapas, Bares, UserProfile

class BaresForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the bares name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bares
        fields = ('name',)


class TapasForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the tapa.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the tapa.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapas
        exclude = ('bares',)

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)
    
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
