from django.shortcuts import render

#Dummy data to pass
posts = [
    {
        'author':'Hemanth',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'November 5'
    },
    {
        'author':'Kumar',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'November 6'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Blog Home' # We can also add title here and pass the key in total
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # we can pass the title individually