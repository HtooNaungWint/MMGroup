from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = 'login.html'

class LogoutView(TemplateView):
    template_name = 'logout.html'