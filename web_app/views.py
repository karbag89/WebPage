from django.shortcuts import render
from django.template.response import TemplateResponse
from web_app.models import Questions


# def index(request):
#     return render(request, 'webapp/index.html')


def home(request):
    return render(request, 'webapp/home.html')


# def about(request):
#     return render(request, 'webapp/about.html')


# def portfolio(request):
#     return render(request, 'webapp/portfolio.html')


# def applications(request):
#     return render(request, 'webapp/applications.html')
    # return render(request, 'webapp/applications1.html')


# def resume(request):
#     return render(request, 'webapp/resume.html')


# def millionaire(request):
#     quest = Questions.objects.all()
#     # for item in quest:
#     #     answer = quest.
#     answer = quest[0]
#     return TemplateResponse(request, 'webapp/millionaire.html', {"quest": quest, 'ans': answer})


# def atm(request):
#     return render(request, 'webapp/atm.html')
#     # return render(request, 'webapp/atm1.html')


def tic_tac_toe(request):
    return render(request, 'webapp/tic_tac_toe.html')
    # return render(request, 'webapp/tic_tac_toe1.html')
