from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views import View
from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import redirect, render, redirect
from .forms import CustomUserCreationForm

User = get_user_model()

# Create your views here.

class SignUpView(FormView):
    template_name = 'sign_up.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['no_header'] = True
        return context


class SignInView(View):
    def get(self, request):
        return render(request, 'sign_in.html', {'no_header': True})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid username or password."
            return render(request, 'sign_in.html', {'error': error_message, 'no_header': True})
