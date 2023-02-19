from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import studentRegisterForm
from .forms import teacherRegisterForm
from django.views.generic import TemplateView


class registerView(TemplateView):
    template_name = 'users/register.html'


def studentRegister(request):
    if request.method == 'POST':
        form = studentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            # return redirect('blog-home')
            messages.success(request, f'Your account has been created!')
            return redirect('login')

    else:
        form = studentRegisterForm()
    return render(request, 'users/registerForm.html', {'form':form})


def teacherRegister(request):
    if request.method == 'POST':
        form = teacherRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            # return redirect('blog-home')
            messages.success(request, f'Your account has been created!')
            return redirect('login')

    else:
        form = teacherRegisterForm()
    return render(request, 'users/registerForm.html', {'form':form})

