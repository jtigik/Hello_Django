
from django.http import HttpResponse

# Create your views here.

def blog(request):
    print('BLOG')
    return HttpResponse('BLOG do App 2')