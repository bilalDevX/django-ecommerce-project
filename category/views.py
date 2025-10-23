from django.shortcuts import HttpResponse

def category_list(request):
    return HttpResponse("This is the category list view.")

def category_detail(request, category_slug):
    return HttpResponse(f"This is the detail view for category {category_slug}.")

