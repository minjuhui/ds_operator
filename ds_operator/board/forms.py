from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['file', 'title','pwd']

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['file'].required = False

# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image') 
#     class Meta:
#         model = Images
#         fields = ('image', )