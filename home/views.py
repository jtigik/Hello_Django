
from django.http import HttpResponse

# Create your views here.

def home(request):
    print('HOME')
    return HttpResponse('HOME do App 2')