from django.shortcuts import render

user_data = {
    'full_name': 'Акбашев Владислав Игоревич',
    'status': 'Студент',
    'course': '4',
    'group': '015',
    'email': 'example@gmail.com',
    'phone': '+7 (987) 098-98-87',
}

def showProfile(request):

    options = {
        'title':'Профиль',
        'user': 'Акбашев Владислав',
        'user_data':user_data
    }

    return render(request, 'Profile\\index.html', options)
