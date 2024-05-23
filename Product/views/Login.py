from django.shortcuts import redirect,render
from django.views import View
from Product.model.register import Register


class Login(View):
    def get(self,request):
        return render(request,'Login.html')
    def post(self,request):
        email=request.POST.get('email1')
        password=request.POST.get('pass1')
        user=Register.objects.get(email=email)
        if user:
            if user.password==password:
                request.session['name']=user.name
                return redirect('index')
            else:
                return redirect('login')
        return render(request,'login.html')

class Logout(View):
    def get(self,request):
        request.session.clear()
        return redirect('login')