from django.shortcuts import render, redirect, HttpResponse
from .models import Course


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def courses_view(request):
    posts = Course.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'courses.html', context)


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print("\n____________")
#         print(name)
#         print(email)
#         print(message)
#         print("____________\n")
#         return redirect('.')
#     return render(request, 'contact.html', {})


def courses_detail_view(request, slug):
    post = Course.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'courses_detail.html', context)

# def add_view(request, a, b):
#     return HttpResponse(f"</h1>{a} + {b} = {a + b}</h1>")
