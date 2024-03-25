from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')


def error_404(request, exception):
    return render(request, 'errors/404.html', {}, status=404)

def error_500(request):
    return render(request, 'errors/500.html', {}, status=500)