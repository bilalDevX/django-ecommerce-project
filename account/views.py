from django.shortcuts import render, HttpResponse

# Create your views here.
def profile_view(request):
    return HttpResponse("This is the profile view.")

# def settings_view(request):
#     return render(request, "account/settings.html")

# def logout_view(request):
#     return render(request, "account/logout.html")

# def login_view(request):
#     return render(request, "account/login.html")

# def register_view(request):
#     return render(request, "account/register.html")

# def password_reset_view(request):
#     return render(request, "account/password_reset.html")

# def password_change_view(request): 
#     return render(request, "account/password_change.html")

# def dashboard_view(request):
#     return render(request, "account/dashboard.html")

