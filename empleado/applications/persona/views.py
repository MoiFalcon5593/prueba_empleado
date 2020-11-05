from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
# models
from .models import Empleado
# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 2
    ordering = 'first_name'
    model = Empleado
    #context_object_name = 'lista'

class ListByAreaEmpleado(ListView):
    """ lista empleado de un area  """
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista
class ListEmpleadoByKword(ListView):
    """ Lista de empleado por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('***************')
        palabra_clave =self.request.GET.get("kword", '')
        print('============',palabra_clave)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('lista resultado:', lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        # print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #toot un proceso
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = 'persona/success.html'

class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    fields = ['first_name','last_name','job','departamento','habilidades',]
    #fields = ('__all__')
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        #logica del codigo
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        print(empleado)
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', ]
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*****Metodo post*****')
        print('*********************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #logica del proceso
        print('*****Metodo form valid*****')
        print('*********************')
        return  super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:correcto')