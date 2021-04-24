from django.shortcuts import render

def Home(request):
	return render(request,'myapp/base.html')

def Features(request):
	return render(request,'myapp/features.html')

def About(request):
	return render(request,'myapp/about.html')

def Contact(request):
	return render(request,'myapp/contact.html')
