from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

from .forms import SignupForm
from .models import Student, Course


def home_view(request):
    """Home page – shows all courses and the logged-in student."""
    p = Course.objects.all()

    student = None
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            student = None  # if user has no Student profile (rare, but safe)

    context = {
        'p': p,
        'student': student,
    }
    return render(request, 'home.html', context)

def logout_view(request):
    messages.success(request, 'You have been logged out successfully!')
    logout(request)
    return redirect('login')

def login_view(request):
    """Handle login form submission."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}')
            return redirect('home')
        # Invalid → re-render with errors
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def signup_view(request):
    """Create a new user + associated Student record."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})



def courses(request):
    p = Course.objects.all()

    # ONLY get student if user is logged in
    student = None
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            student = None

    context = {
        'p': p,
        'student': student,
    }
    return render(request, 'courses.html', context)


def course_description(request, course_id):
    """Show details of a single course."""
    course = get_object_or_404(Course, id=course_id)

    student = None
    if request.user.is_authenticated:
        student = Student.objects.filter(user=request.user).first()

    context = {
        'course': course,
        'student': student,
    }
    return render(request, 'course_description.html', context)



@login_required
def profile_view(request):
    user = request.user

    # Try to get Student profile
    try:
        student = user.student  # OneToOneField from Student to User
    except AttributeError:
        messages.error(request, "No student profile linked to this account.")
        return redirect('home')  # or login page

    context = {
        'student': student,
        'user': user,  # safe fallback
        'enrollments': []  # empty list so template doesn't break
    }
    return render(request, 'profile.html', context)


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = get_object_or_404(Student, user=request.user)
    student.courses.add(course)   
    return redirect('courses')
