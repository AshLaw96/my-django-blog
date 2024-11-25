from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.


def about_me(request):
    """
    Renders the most recent information on the website author
    and handles the collaboration request form
    Displays an individual instance of :model:`about.About`.
    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.
    **Template**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == 'POST':
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaboration = collaborate_form.save(commit=False)
            collaboration.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your collaboration request has '
                'been submitted! I will endeavor to respond within 2 working days.'
            )
    else:
        collaborate_form = CollaborateForm()

    return render(
        request, 'about/about.html', {
            'about': about,
            'collaborate_form': collaborate_form,
        },
    )
