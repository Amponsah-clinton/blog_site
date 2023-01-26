from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from django.http import HttpResponseRedirect
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.conf import settings


  
# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
    


class HomeView(ListView):
    model = Post 
    template_name = 'home.html'
    ordering = ['-post_date']   # sort by date
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
    

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ''))
    return render(request,'categories.html', {'cats': cats.title().replace('-', ''), 'category_posts': category_posts})


# news details views
class ArticleDetailView(DetailView):
    model = Post                #specifies the model you are working with
    template_name='article_details.html'      #specifies the template you are working with
    # ordering = ['-id']   # automatically sort the posts by id

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        return context



# add post views
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name='add_post.html'
    # fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name='add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class UpdatePostView(UpdateView):
    model = Post
    template_name='update_post.html'
    fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')  # redirect to home page


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name='add_comment.html'
    #fields = '__all__'
    success_url = reverse_lazy('home') 
    ordering = ['-post_date']
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)