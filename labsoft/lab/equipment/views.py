from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django_tables2 import SingleTableView

from labsoft.core.models import Equipment
from labsoft.lab.equipment.forms import EquipmentForm
from labsoft.lab.equipment.tables import EquipmentTable 

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
    