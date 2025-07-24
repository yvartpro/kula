from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth import login,authenticate

# Create your views here.
def home(request):
    post = Post.objects.all().order_by('?')
    return render(request,'booking/index.html',{"posts":post})
def register(request):
    if request.method =='POST':
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       adress=request.POST.get('address')
       password=request.POST.get('password1')
       password2=request.POST.get('password2')
       full_name = request.POST.get('fullname')
       print(password2)
       if password != password2:
          context={
                   "sapor":"password not the same"
          }
          return render(request,'booking/register.html',context)
       else:
          user=User.objects.create_user(username=email,email=email,password=password)
          user.first_name= full_name
          user.phone=phone
          user.adress=adress
          user.save()
          return redirect('login')
    return render(request,'booking/register.html')
def signin(request):
    if request.method == 'POST':
       email=request.POST.get('email')
       password=request.POST.get('password')
       user=authenticate(username=email,password=password)
       if user is not None:
          login(request,user)
          return redirect('dashboard')
       else:
           context={
           "sapor":"user is not none"
           }
       return render(request,'booking/login.html',context)
    return render(request,'booking/login.html')
def booking(request):
    if request.method =='POST':
       full_name=request.POST.get('full_name')
       special=request.POST.get('special')
       phone=request.POST.get('phone')
       email=request.POST.get('email')
       people=request.POST.get('people')
       time=request.POST.get('time')
       date=request.POST.get('date')
       type=request.POST.get('type')
       company=request.POST.get('company')
       account=request.POST.get('account')
    return render(request,'booking/booking.html')
def book(request,user_id):
    print(user_id)
    return render(request,'booking/booking.html')
def post(request):
    if request.method =='POST':
       photo=request.FILES.get('photo')
       title=request.POST.get('title')
       description=request.POST.get('description')
       post=Post(user=request.user,photo=photo,title=title,description=description)
       post.save()
       return redirect('dashboard')
    return render(request,'booking/dashboard.html')
def profile(request):
    if request.method =='POST':
       photo=request.FILES.get('photo')
       try:
          profile = Profile.objects.get(user=request.user)
          print(profile)
          print("################################")
          if profile:
             profile.photo = photo
             profile.save()
          else:
             profile=Profile(user=request.user,photo=photo)
             profile.save()

       except:
             profile=Profile(user=request.user,photo=photo)
             profile.save()
       return redirect('dashboard')
def add_category(request):
    if request.method =='POST':
       category=request.POST.get('category')
       profile = Profile.objects.get(user=request.user)
       category=Category(user=request.user,profile=profile,category=category)
       category.save()
       return redirect('dashboard')
    return render(request,'booking/dashboard.html')
def dashboard(request):
    user = request.user
    post = Post.objects.filter(user=request.user.id)
    print(post)
    print('##################')
    profile = Profile.objects.get(user=request.user.id)
    context = {
      'user':user,
      'post':post,
      'profile':profile
    }
    return render(request,'booking/dashboard.html',context)
def view_restorent(request,user_id):
    user = User.objects.get(id=user_id)
    context = {
      'user':user
    }
    return render(request,'booking/dashboard.html',context)
def date(request):
    date =  Category.objects.filter(category='date').order_by('?')
    return render(request,'booking/index.html',{'types':date})

def occasion(request):
    occasion=Category.objects.filter(category='occasion').order_by('?')
    return render(request,'booking/index.html',{'types':occasion})
def celebration(request):
    celebration=Category.objects.filter(category='celebration').order_by('?')
    return render(request,'booking/index.html',{'types':celebration})
def business(request):
    business=Category.objects.filter(category='business').order_by('?')
    return render(request,'booking/index.html',{'types':business})

