from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

import re
from .models import Student

from .forms import StudentForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Password validation
        if (not re.search(r'[A-Z]', password) or
            not re.search(r'[a-z]', password) or
            not re.search(r'[0-9]', password) or
            not re.search(r'[^A-Za-z0-9]', password)):
            messages.error(request, "Password must include uppercase, lowercase, digit, and special character.")
            return redirect('register')

        # Name validation
        if not firstname.isalpha() or not lastname.isalpha() or not username.isalpha():
            messages.error(request, 'Names must contain only letters.')
            return redirect('register')


        # Save user securely
        User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname
        )

        messages.success(request, 'Registration successful!')
        return redirect('login')

    # For GET request, render the registration form
    return render(request, 'register.html')

def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('student')  # Reloads the same form
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'display.html', {'students': students})

def student_update(request, pk):
    messages.success(request, "Student update successfully.")
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    messages.success(request, "Student Delete successfully.")
    print("----->", pk)
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('show')
    # return render(request, 'display.html', {'student': student})


