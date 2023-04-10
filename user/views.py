from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def user_register(request):

    form = UserCreationForm()
    message = ''

    if request.method == 'GET':
        print('GET')
    elif request.method == 'POST':
        print('POST')
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(password1) < 8:
            message = '密碼少於8個字元'
        elif password1 != password2:
            message = '兩次密碼不同'
        else:
            if User.objects.filter(username=username).exists():
                message = '帳號重複，請換其他帳號'
            else:
                print('開始註冊')

        # 註冊功能
        # 兩次密碼是否相同
        # 密碼不可少於8個字元
        # 使用者名稱不能重複

    return render(request, './user/register.html', {'form': form, 'message': message})