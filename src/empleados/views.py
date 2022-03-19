from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from empleados.form import EmpleadoForm
from .models import *
def home(request):
    return render(request, 'index.html')

class EmpleadosListView(ListView):
    model = Empleado
    template_name = 'empleados/list.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de empleados'
        context['list_url'] = reverse_lazy('EmpleadosCreateView')
        return context

class EmpleadosCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/create.html'
    success_url = reverse_lazy('EmpleadosListView')
    
    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear empleado'
        return context
    
class EmpleadosUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/create.html'
    success_url = reverse_lazy('EmpleadosListView')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Registro'
        return context
    
class EmpleadosDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('EmpleadosListView')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Registro'
        context['list_url'] = reverse_lazy('EmpleadosListView')
        return context

class EmpleadosDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Informacion de '
        context['list_url'] = reverse_lazy('EmpleadosListView')
        return context