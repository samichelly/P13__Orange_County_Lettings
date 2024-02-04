from django.shortcuts import render
from sentry_sdk import capture_message


def index(request):
    """
    Render the index page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - Rendered response for the index page.
    """
    return render(request, "index.html")


def custom_404(request, exception):
    """
    Render a custom 404 error page.

    Parameters:
    - request: HttpRequest object.
    - exception: Exception object representing the error.

    Returns:
    - Rendered response for the custom 404 error page.
    """
    capture_message("Page not found!", level="error")
    return render(request, "404_error.html", status=404)


def custom_500(request):
    """
    Render a custom 500 error page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - Rendered response for the custom 500 error page.
    """
    capture_message("Internal Server Error", level="error")
    return render(request, "500_error.html", status=500)
