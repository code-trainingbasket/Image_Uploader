from django.shortcuts import render,redirect
from.models import User
from .forms import UserForm

# Create your views here.
def home(request):
	user= UserForm()
	if request.method=='POST':
		user = UserForm(request.POST,request.FILES)
		if user.is_valid():
			user.save()
		return redirect('/')
	return render(request,'home.html',{'user':user})