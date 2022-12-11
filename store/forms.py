from ast import Mod
from django.forms import FileField, Form, ModelForm
# from .models import Post

# class BlogPostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['slug', 'title', 'description', 'date', 'author', 'tags', 'image', 'image_alt']

    
class UploadCSVForm(Form):
    csv_file = FileField(label='Select a file')