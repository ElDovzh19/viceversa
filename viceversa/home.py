from django.shortcuts import render 

def home(request):
	return render(request,'home.html')

def revers(request):
	user_text=request.GET['usertext']
	text_cout=len(user_text.split())
	revers_text= user_text[::-1]
	return render(request,'revers.html',{'usertext':user_text,'reversedText':revers_text,'textcount':text_cout})