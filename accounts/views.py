from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class RegisterFormView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class LogoutLogoutView(LogoutView):
    next_page = reverse_lazy('login')
