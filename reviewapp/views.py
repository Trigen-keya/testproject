from audioop import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import ReviewModel
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail


def signupview(request):
    
    if request.method == 'POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        try:
            user=User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            return render(request, 'signup.html',{'error':'このユーザーは既に登録されています。'})
    else:
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def loginview(request):
    if request.method=='POST':
        username_data=request.POST.get('username_data')
        password_data=request.POST.get('password_data')
        user = authenticate(username=username_data, password=password_data)
        print(user)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('list'))
        else:
            return HttpResponse("アカウント作ってないでしょ!!")
    else:
        return render(request,'login.html')

@login_required
def listview(request):
    object_list=ReviewModel.objects.all()
    return render(request,'list.html',{'object_list':object_list})
@login_required
def detailview(request,pk):
    object=ReviewModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})
@login_required
class creatclass(CreateView):
    template_name='create.html'
    model=ReviewModel
    fields=('title','content','author','evaluations')
    success_url=reverse_lazy('list')

class logoutview(LogoutView):
    template_name='logout.html'
    
def evaluationview(request, pk):
    post=ReviewModel.objects.get(pk=pk)
    author_name=request.user.get_username()+str(request.user.id)
    if author_name in post.useful_review_record:
        return redirect('list')
    else:
        post.useful_review=post.useful_review+1
        post.useful_review_record=post.useful_review+author_name
        post.save()
        return redirect('list')

class passwordview(PasswordChangeView):
    template_name='changepassword.html'
    success_url=reverse_lazy('login')

def emailfunc(request):
    send_mail(
        'タイトル',
        '本文',
        '送信元のメールアドレス',
        ['送信先のメールアドレス'],
        fail_silently=False,
    )
    return HttpResponse('')