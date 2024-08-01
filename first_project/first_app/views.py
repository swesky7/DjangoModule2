from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


def index(request):
    # return HttpResponse("Welcome to My First App.Iam coming from Index")
    # mydict = {'insert_me': "Iam coming from Index html of first app"}
    # return render(request, 'first_app/index.html', context=mydict)
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": webpages_list}
    return render(request, 'first_app/index.html', date_dict)


def about(request):
    return HttpResponse("Welcome to About Page")
