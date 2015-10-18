from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django_tables2 import SingleTableView

from labsoft.core.models import EquipmentSample
from labsoft.lab.sample.forms import EquipmentSampleForm
from labsoft.lab.sample.tables import EquipmentSampleTable
from labsoft.core.helpers import make_preparation

class EquipmentSampleListView(SingleTableView):
    template_name = 'lab/sample/sample_list.html'
    model = EquipmentSample
    context_object_name = 'samples'
    table_class = EquipmentSampleTable
    context_table_name = 'samples_table'
    table_pagination={ "per_page":15 }
    
    def get_queryset(self):
        objs = self.model.objects.all()
        search = self.request.GET.get('search')
        
        if search:
            objs = objs.filter(sample_no__icontains=search)
        return objs

class EquipmentSampleCreateView(generic.CreateView):
    template_name = 'lab/sample/sample_create.html'
    form_class = EquipmentSampleForm
    model = EquipmentSample
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        no_samples = self.model.objects.count()
        if no_samples == 0:
            self.object.sample_no = 1000
        else:
            self.object.sample_no = 1000 + no_samples
        self.object.save()
        make_preparation(self.object, self.request.user)
        return HttpResponseRedirect(reverse('labsoft-lab-sample-list'))

    
class EquipmentSampleUpdateView(generic.UpdateView):
    template_name = 'lab/sample/sample_update.html'
    form_class = EquipmentSampleForm
    model = EquipmentSample
    context_object_name = 'sample'
    success_url = reverse_lazy('labsoft-lab-sample-list')
    
class EquipmentSampleDetailView(generic.DetailView):
    template_name = 'lab/sample/sample_detail.html'
    model = EquipmentSample
