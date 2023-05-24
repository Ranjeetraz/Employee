from django.shortcuts import render,HttpResponseRedirect
# from app.forms import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import View
from .forms import UserRegisterForm, EmployeeForm 
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app.models import EmployeeDetail 
AuthenticationForm

class SignupView(View):
    template_name = "app/signup.html"

    def get(self, request):
        if not request.user.is_authenticated:
            context = {}
            form = UserRegisterForm()
            context["form"] = form
            return render(self.request, self.template_name, context)
    
    def post(self, request):
        context = {}
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            print(password1)
            print(password2)
            if password1 == password2:
                form.save()
                messages.success(request, "Account created Successfully!")
                return HttpResponseRedirect(reverse("login"))
            else:
                messages.error(request, "Confirm Password didn't match!!")
            context['form'] = form
            return render(request, self.template_name, context)
        else:
            context['form'] = form
            messages.error(request, "Form data is not valid Please try again!!")
            return render(request, self.template_name, context)

# @method_decorator(login_required, name="dispatch")
class HomeView(View):
    template_name = "app/home.html"
    def get(self, request):
        context = {}
        context["data"] = EmployeeDetail.objects.all()
        return render(self.request, self.template_name, context)
        
    def post(self, request):
        pass    


class LoginView(View):
    template_name = "app/login.html"

    def get(self, request):
        if not request.user.is_authenticated:
            context = {}
            form = AuthenticationForm()
            context["form"] = form
            return render(self.request, self.template_name, context)
    
    def post(self, request):
        email = request.POST['username']
        password =request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"login successful")
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, "email or passord wrong")    
            return HttpResponseRedirect(reverse('login'))
        
class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request) 
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('add_employee'))  
    def post(self, request):
        pass   

class AddEmployeeDetailView(View):
    template_name = "app/add_emp.html"
    
    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            context['emp_form'] = EmployeeForm()
            return render(request, self.template_name, context) 

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee detail save successfully!")
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, "Employee detail do not save please try again!!")  
        return HttpResponseRedirect(reverse('add_employee')) 
    
class EmpUpdateView(View):
    template_name = "app/emp_update.html"
    
    def get(self, request, id):
        context = {}
        if request.user.is_authenticated:
            context['emp_update'] = EmployeeDetail.objects.get(id=id)
            return render(self.request, self.template_name, context)
    def post(self, request, id):
        obj = EmployeeDetail.objects.get(id=id)
        a=EmployeeForm(request.POST,instance=obj)
        emp_name = request.POST.get('emp_name', None)
        emp_role = request.POST.get('emp_role', None)
        salary = request.POST.get('salary', None)
        emp_code = request.POST.get('emp_code', None)
        if emp_name and emp_code:
            obj.emp_name = emp_name
            obj.emp_role = emp_role
            obj.salary = salary
            obj.emp_code = emp_code
            obj.save()
            messages.success(request, 'Profile updated successfully.')
            
        else:
            messages.error(request, 'Error updating profile.')
        return HttpResponseRedirect(reverse('home'))

def EmpDelete(request, id): 
    delete = EmployeeDetail.objects.get(id=id)
    delete.delete()
    return HttpResponseRedirect(reverse('home'))    

        
            
        
        
            

     
