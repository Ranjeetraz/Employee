from django.urls import path
from app import views

urlpatterns = [
    path('',views.HomeView.as_view(), name="home"),
    path('register/',views.SignupView.as_view(), name="signup"),
    path('login/',views.LoginView.as_view(), name="login"),
    path('logout/',views.LogoutView.as_view(), name="logout"),
    path('add-employee-details/', views.AddEmployeeDetailView.as_view(), name="add_employee"),
    path('update/<int:id>',views.EmpUpdateView.as_view(), name="update"),
    path('delete/<int:id>',views.EmpDelete, name="dalete")
    
    
]
