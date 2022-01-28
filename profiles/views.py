from django.shortcuts import render


def profile(request):
    """ Display the user """
    
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)

