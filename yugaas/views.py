from django.shortcuts import render

# Create your views here.
def ourservices(request):
    return render(request,"ourservices.html")
def humanresource(request):
    return render(request,"humanresource.html")
def technologyservices(request):
    return render(request,"technologyservices.html")
def cybersecurityservices(request):
    return render(request,"cybersecurityservices.html")
def learningacademy(request):
    return render(request,"learningacademy.html")
def career(request):
    return render(request,"career.html")
def home(request):
    return render(request,"Hom1.html")
def about(request):
    return render(request,"aboutus.html")
def contactus(request):
    return render(request,"contactus.html")