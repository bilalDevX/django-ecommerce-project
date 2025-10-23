from django.shortcuts import render, HttpResponse

def category_list(request):
    # Logic to retrieve and display a list of categories
    return HttpResponse("this running category list view")

def category_detail(request, slug):
    # Logic to retrieve and display details of a specific category by slug
    return HttpResponse(f"this running category detail view for slug: {slug}")

    # You can replace the HttpResponse with actual rendering logic

    