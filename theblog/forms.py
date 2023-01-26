# this is used when you want to style the forms from models.py
from django import forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

# choices =[('coding','coding'), ('sports','sports'), ('Entertainment','Entertainment'),]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','title_tag', 'author', 'body','snippet','header_image')
        
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter title'}),
            'category': forms.Select(choices = choice_list ,attrs={'class': 'form-control',}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter title tag'}),
             'author': forms.TextInput(attrs={'class': 'form-control','value':'','id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control',}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter details of the post'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter name'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Comment'}),
        }