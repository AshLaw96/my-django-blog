from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.


def about_me(request):
    """
    Renders the About page and handles the collaboration request form.
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == 'POST':
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaboration = collaborate_form.save(commit=False)
            collaboration.save()
            messages.add_message(
                request, messages.SUCCESS, 'Your collaboration request has been submitted! I will endeavor to respond within 2 working days.'
            )
    else:
        collaborate_form = CollaborateForm()


    return render(
        request, 'about/about.html', {
            'about': about,
            'collaborate_form': collaborate_form,
        },
    )