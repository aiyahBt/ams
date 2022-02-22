from django.shortcuts import render

# Create your views here.

def home_view(request):

    # if  not(request.user.is_authenticated):
    #     stuff_for_frontend = {
    #         'valid_search_str': False,
    #         'search_str': 'You have no permission to view this profile.',
    #     }
    stuff_for_frontend = {
        'greeting_text' : 'hello'

    }

    return render(request, 'home/home.html', stuff_for_frontend)