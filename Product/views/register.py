from django.shortcuts import redirect,render
from django.views import View
from Product.model.register import Register



class Register_user (View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        name=request.POST.get('name')
        address= request.POST.get('address')
        number= request.POST.get('number')
        email=request.POST.get('email')
        password = request.POST.get('password')
        print(name,email,password)
        reg=Register(name=name,address=address,number=number,email=email,password=password)
        print('database',name)
        reg.save()

        return render(request,'register.html')
