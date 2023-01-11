from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate, PerfilVer, PasswordChangeView 

#app_name = 'Usuarios'

urlpatterns = [
    #path('', view, name='')
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/form.html'
    ), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='sair'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizar_dados/', PerfilUpdate.as_view(), name='atualizarDados'),
    path('meu_perfil/', PerfilVer.as_view(), name='verPerfil'),

    #Senhas

    path('alterar_senha/', PasswordChangeView.as_view(), name='alterarSenha'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password_reset.html',
             subject_template_name='commons/password_reset_subject.txt',
             email_template_name='commons/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
