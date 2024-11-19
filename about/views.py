from django.shortcuts import render
from .models import Profile

# Create your views here.


def profile_detail(request):
    """
    Render the About page.
    """
    about_me = Profile.objects.all().order_by('-updated_on').first()
    return render(
        request, 'about/about.html', {'about': about_me},
    )