from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Ironman(request):
    return HttpResponse('<h1>And I am Ironman!!!!!</h1>')

def CaptainAmerica(request):
    return HttpResponse('''<h1><b>Avengers Assemble</b></h1>
    <img src='https://tse4.mm.bing.net/th?id=OIP.dsataml3OKPrdNky_6ykMAHaEK&pid=Api&P=0&h=180'>''')

def Thanos(request):
    return HttpResponse('<h1><marquee>I am Inevitable</marquee></h1>')
