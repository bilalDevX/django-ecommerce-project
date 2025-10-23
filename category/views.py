from django.http import HttpResponse
from .models import Category

def category_list(request):
    queryset = Category.objects.all()
 
    return HttpResponse(queryset)

def category_detail(request, category_slug):
    return HttpResponse(f"This is the detail view for category {category_slug}.")

