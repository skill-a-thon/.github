from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group
from .models import User, Course, UserCourses, UserMentor, Mentor
# Create your views here.
def index(request):
  return render(request, "careerpath/index.html")

def login_view(request):
  if request.user.is_authenticated:
    return HttpResponseRedirect(reverse('index'))
  if request.method == "POST":
    username = request.POST.get("username").strip()
    print("🚀 ~ file: views.py:17 ~ username:",username)
    password = request.POST.get("password").strip()
    print("🚀 ~ file: views.py:19 ~ password:",password)
    user = authenticate(request, username=username, password=password)
    print("🚀 ~ file: views.py:19 ~ user:", user)

    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'careerpath/login.html',{
            "error_msg":"Invalid Username or Password",
            "username":username,
            "password":password
        })
  return render(request, "careerpath/login.html")

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))

def signup_view(request): 
  print("In signup")
  #if user is authenticated add/signup user in database
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    repassword = request.POST.get("re_password")

    if password != repassword:
      return render(request, "careerpath/signup.html", {
          "pwd_not_match": "Passwords must match."
      })
    try:
      user = User.objects.create_user(username, "", password, is_student=False)
      user.save()
      print(user)
      login(request, user)
    #if user is already exist show error
    except IntegrityError:
      print("error")
      return render(request, "careerpath/signup.html",{
          "existing_user":"Username already exist!",
          "username":username,
          "password":password,
          "re_password":repassword
      })
    
    return HttpResponseRedirect(reverse("index"))

  else:
    return render(request, "careerpath/signup.html")

def explore_career_path(request):
  if request.method == "POST":
    selected_course = request.POST.get("selected_course")

    userCourse , created= UserCourses.objects.get_or_create(user=request.user)
    course = Course.objects.get(id=selected_course)

    userCourse.courses.add(course)
  courses = Course.objects.all().order_by('id')
  print("🚀 ~ file: views.py:72 ~ courses:", courses)
  return render(request, "careerpath/explore_career_path.html",
  {
    "courses": courses
  })


def explore_mentor(request):
  if request.method == "POST":
    selected_mentor = request.POST.get("selected_mentor")

    userMentor , created= UserMentor.objects.get_or_create(user=request.user)
    mentor = Mentor.objects.get(id=selected_mentor)

    userMentor.mentor.add(mentor)
  mentors = Mentor.objects.all().order_by('id')
  print("🚀 ~ file: views.py:72 ~ courses:", mentors)
  return render(request, "careerpath/explore_mentor.html",
  {
    "mentors": mentors
  })

def getCourse(request):
  try:
    userCourse = UserCourses.objects.get(user=request.user)
    courses =  userCourse.courses.all()
    return courses
  except ObjectDoesNotExist:
    return ""

def getMentor(request):
  try:
    userMentor = UserMentor.objects.get(user=request.user)
    mentors =  userMentor.mentor.all()
    return mentors
  except ObjectDoesNotExist:
    return ""

def profile(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('index'))

  profile = User.objects.filter(id= request.user.id)
  print("🚀 ~ file: views.py:87 ~ profile:", profile)

  courses = getCourse(request)
  mentors = getMentor(request)
  

  print("🚀 ~ file: views.py:101 ~ courses:", courses)
  return render(request, "careerpath/profile.html",
  {
    "profile": profile,
    "courses": courses,
    "mentors": mentors,
  })