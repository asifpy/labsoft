from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django_tables2 import SingleTableView

from labsoft.core.models import Equipment, EquipmentSample
from labsoft.lab.equipment.forms import EquipmentForm
from labsoft.lab.sample.forms import EquipmentSampleForm
from labsoft.lab.equipment.tables import EquipmentTable
from labsoft.lab.sample.tables import EquipmentSampleTable

class EquipmentListView(SingleTableView):
    template_name = 'lab/equipment/equipment_list.html'
    model = Equipment
    context_object_name = 'equipments'
    table_class = EquipmentTable
    context_table_name = 'equipments_table'
    table_pagination={ "per_page":15 }
    
    def get_queryset(self):
        objs = self.model.objects.all()
        search = self.request.GET.get('search')
        
        if search:
            objs = objs.filter(serial_no__icontains=search)
        return objs

class EquipmentCreateView(generic.CreateView):
    template_name = 'lab/equipment/equipment_create.html'
    form_class = EquipmentForm
    model = Equipment
    success_url = reverse_lazy('labsoft-lab-equipment-list')
    
class EquipmentUpdateView(generic.UpdateView):
    template_name = 'lab/equipment/equipment_update.html'
    form_class = EquipmentForm
    model = Equipment
    context_object_name = 'equipment'
    success_url = reverse_lazy('labsoft-lab-equipment-list')
    
class EquipmentDetailView(generic.DetailView):
    template_name = 'lab/equipment/equipment_detail.html'
    model = Equipment

class EquipmentSampleCreateView(generic.CreateView):
    template_name = 'lab/equipment/sample/sample_create.html'
    form_class = EquipmentSampleForm
    model = EquipmentSample
    
    def get_form_kwargs(self):
        kwargs = super(EquipmentSampleCreateView, self).get_form_kwargs()
        kwargs['equipment_id'] = self.kwargs['pk']
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(EquipmentSampleCreateView, self).get_context_data(**kwargs)
        context['equipment'] = Equipment.objects.get(id=self.kwargs['pk'])
        return context
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.equipment = Equipment.objects.get(id=self.kwargs['pk'])
        no_samples = self.model.objects.count()
        if no_samples == 0:
            self.object.sample_no = 1000
        else:
            self.object.sample_no = 1000 + no_samples
        self.object.save()
        return HttpResponseRedirect(reverse('labsoft-lab-equipment-detail', args=[self.kwargs['pk']]))

class EquipmentSampleListView(SingleTableView):
    template_name = 'lab/equipment/sample/sample_list.html'
    model = EquipmentSample
    context_object_name = 'samples'
    table_class = EquipmentSampleTable
    context_table_name = 'sample_table'
    table_pagination={ "per_page":15 }
    
    def get_queryset(self):
        objs = self.model.objects.filter(equipment__id=self.kwargs['pk'])
        search = self.request.GET.get('search')
        
        if search:
            objs = objs.filter(sample_no__icontains=search)
        return objs
    
    def get_context_data(self, **kwargs):
        context = super(EquipmentSampleListView, self).get_context_data(**kwargs)
        context['equipment'] = Equipment.objects.get(id=self.kwargs['pk'])
        return context