from django.shortcuts import render
# Create your views here.
def index(request):
	return render(request,'kmrc_app/index.html')
def aboutus(request):
	return render(request,'kmrc_app/aboutus.html')
def footer(request):
	return render(request,'kmrc_app/footer.html')
def login(request):
	return render(request,'kmrc_app/login.html')
def help(request):
	return render(request,'kmrc_app/help.html')	
def map(request):
	return render(request,'kmrc_app/map.html')	
def journey(request):
	return render(request,'kmrc_app/journey.html')
def signup(request):
	return render(request,'kmrc_app/signup.html')
def viewmore(request):
	return render(request,'kmrc_app/viewmore.html')