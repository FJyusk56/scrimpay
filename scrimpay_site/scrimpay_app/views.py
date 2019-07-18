from django.shortcuts import render

from .models import User
from .models import Service

# Create your views here.
def index(request):
    data = Service.objects.all()
    my_dict = {
        'title':'契約サービス',
        'val':data,
    }
    return render(request, 'scrimpay_app/index.html',my_dict)