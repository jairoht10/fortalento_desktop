from django.shortcuts import render
from .models import Estudiante
from .forms import EstudianteForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView

# Create your views here.

class EstudianteCreate(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = "estudiante.registro.template.html"
    success_url = reverse_lazy('estudiante_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.nombre = form.cleaned_data['nombre']
        self.object.apellido = form.cleaned_data['apellido']
        user = self.request.user
        self.object.user = user
        self.object.save()

        return super(EstudianteCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(EstudianteCreate, self).form_invalid(form)

class EstudianteList(ListView):
    model = Estudiante
    template_name = "estudiante.lista.template.html"

    def get_queryset(self):
        queryset = Estudiante.objects.filter(user=self.request.user)
        return queryset
