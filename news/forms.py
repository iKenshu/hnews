from django import forms
from django.forms import ModelForm

from .models import New, Comment

class NewForm(ModelForm):

    error_message = {
        'url_exists': 'The url alredy exists'
    }

    class Meta:
        model = New
        fields = ('title', 'url')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super(NewForm, self).clean()
        print(cleaned_data)

    def clean_url(self):
        url = self.cleaned_data['url'] 
        if New.objects.filter(url=url).exists():
            raise forms.ValidationError('The URL alredy exists')
        return url

class VoteForm(ModelForm):
    class Meta:
        model = New
        exclude = ('title', 'url')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }