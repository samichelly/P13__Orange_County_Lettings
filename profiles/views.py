from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Render the index page for profiles.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - Rendered response for the profiles index page.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Render the profile page for a specific user.

    Parameters:
    - request: HttpRequest object.
    - username: Username of the profile to be displayed.

    Returns:
    - Rendered response for the profile page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
