from django.shortcuts import render, redirect
from blogs.models import Blogs
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict

# Create your views here.

# assigning User as our User model i.e. as User_details
User = get_user_model()

@login_required(login_url="Base:Login")
def Home(request):
    Blogs_obj = Blogs.objects.filter(Author = request.user)
    blogs = []
    for i in Blogs_obj:
        blogs.append(model_to_dict(i))
    if (len(blogs) == 0):
        UserBlogs = False
    else:
        UserBlogs = True
    context = {
        "UserBlogs":UserBlogs,
        "blogs":blogs
    }
    return render(request,'blogs/home.html',context = context)

@login_required(login_url="Base:Login")
def CreateBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Author = request.user
        new_blog = Blogs.objects.create(Author = Author, title = title, content = content)
        new_blog.save()
        return redirect('blogs:Home')
    return render(request,'blogs/create_blog.html')

def BlogDisplay(request,search):
    search = search.split('-')
    search1 = ''
    for i in search:    search1 = search1+' '+i
    print("SEARCH1:",search1)
    result = Blogs.objects.filter(title = search1[1:]).first()
    if result:
        context = {
            "title":result.title,
            "content":result.content.split('\n'),
        }
    else:
        return redirect('blogs:home')
    return render(request,'blogs/blog_display.html',context)

@login_required(login_url="Base:Login")
def UserBlogs(request):
    if request.method == 'GET':
        user = request.user
        user_blogs = Blogs.objects.filter(Author=user)
        blogs = {}
        count = 0
        for blog in user_blogs:
            blogs[count] = model_to_dict(user_blogs[count])
            count = count + 1
        # print(blogs)
        blogging = {}
        blogging["blogs"] = dict(blogs)
        return render(request,'blogs/user_blogs.html',blogging)
    elif request.method == 'POST':
        search = request.POST['search-title']
        return BlogDisplay(request,search)

@login_required(login_url="Base:Login")
def DeletePost(request,id):
    post = Blogs.objects.get(id = id).delete()
    return redirect('blogs:home')

def Learn(request):
    return render(request,"blogs/learn.html")