from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """
    Render the index page for lettings.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - Rendered response for the lettings index page.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Render the page for a specific letting.

    Parameters:
    - request: HttpRequest object.
    - letting_id: ID of the letting to be displayed.

    Returns:
    - Rendered response for the letting page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
