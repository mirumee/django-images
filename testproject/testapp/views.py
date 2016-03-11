from django.shortcuts import render
from testapp.models import Product


def index(request):
    return render(request, 'index.html', {
        'products': Product.objects.all(),
    })
