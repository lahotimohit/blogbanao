from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from . import models
from . import forms


# Create your views here.
def signup(request):
    form = forms.MyUserCreationForm
    if request.method == "POST":
        form = forms.MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'appbanao/signup.html', {'form': form})


def posts(request):
    posts = models.Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'appbanao/posts.html', {'posts': posts,})


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(models.Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'appbanao/post_detail.html', {'post': post})


def user_blog(request, user_id):
    if request.user.is_authenticated and request.user.role == 'Doctor':
        posts_req = models.Post.objects.filter(author__exact=request.user.id)
        return render(request, 'appbanao/adminblog.html', {'posts': posts_req})
    return render(request, 'appbanao/adminblog.html')


def blog_add(request):
    form = forms.BlogForm
    if request.method == "POST":
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'appbanao/addblog.html', {'form': form})


def doctor_list(request):
    doctors = models.User.objects.filter(role='Doctor')
    return render(request, 'appbanao/doctors.html', {'doctors': doctors})


def appointment(request):
    form = forms.AppointmentForm()
    if request.method == "POST":
        form = forms.AppointmentForm(request.POST)
        if form.is_valid():
            request.session['doctor'] = form.cleaned_data['Doctor']
            request.session['speciality'] = form.cleaned_data['speciality']
            request.session['appointment_date'] = form.cleaned_data['appointment_date'].isoformat()
            request.session['appointment_time'] = form.cleaned_data['appointment_time'].isoformat()
            return redirect('details')
    return render(request, 'appbanao/appointment.html', {'form':form})


def details(request):
    speciality = request.session.get('speciality')
    doctor = request.session.get('doctor')
    mail = request.user.email
    adate = request.session.get('appointment_date')
    atime = request.session.get('appointment_time')
    send_mail("Appointment of Doctor",
              f"Congratulations your appointment with {doctor} is booked....\n"
              f"Here are your details...\n"
              f"Appointment Date: {adate}\n"
              f"Appointment Time: {atime}",
              'Mohit', [mail], fail_silently=False)
    return render(request, 'appbanao/details.html', {'doctor': doctor,'speciality': speciality, 'adate': adate, 'atime': atime})

