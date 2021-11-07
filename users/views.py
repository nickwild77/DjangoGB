from django.conf import settings
from django.core.mail import send_mail, message
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from baskets.models import Basket
from django.contrib.auth.decorators import login_required
from django.db import transaction

# Create your views here.
from .models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.add_message(request, messages.SUCCESS, 'Письмо направленно на почту. Для подтверждения'
                                                                'регистрации перейдите по ссылке из письма')
                return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form
    }

    return render(request, 'users/register.html', context)


@transaction.atomic
def profile(request):
    title = 'Профиль'

    if request.method == 'POST':
        edit_form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)

        profile_form = UserProfileEditForm(request.POST, instance=request.user.userprofile)

        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        edit_form = UserProfileForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)

    context = {
        'title': title,
        'edit_form': edit_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждение учетной записи {user.username} на портале {settings.DOMAIN_NAME}' \
              f' перейдите по ссылке: {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    context = {
        'title': 'GeekShop - Подтверждение регистрации',
    }

    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users/verification.html', context)
        else:
            print(f'error activation user: {user}')
            return render(request, 'users/verification.html')
    except Exception as e:
        print(f'error activation user: {e.args}')
        return HttpResponseRedirect(reverse('index'))
