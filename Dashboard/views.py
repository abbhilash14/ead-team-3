from django.shortcuts import render


# Create your views here.
def Login(request):
    return render(request,"Dashboard/login.html")

def Dashboard(request):
    return render(request,"Dashboard/Dashboard.html")

def LawyerAccount(request):
    return render(request,"Dashboard/LawyerAccount.html")

def ValuationDetails(request):
    return render(request,"Dashboard/ValuationDetails.html")