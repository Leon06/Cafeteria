
from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from .models import Post , Category


class Blog(TemplateView):
    template_name='blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    
def category(request,category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category,id=category_id)
    #posts = Post.objects.filter(categories=category)
    return render(request,'blog/category.html',{'category':category})