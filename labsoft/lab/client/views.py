from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory

from labsoft.core.models import ClientCompany, ClientEmployee
from labsoft.lab.client.forms import ClientCompanyForm

class ClientCompanyListView(generic.ListView):
    template_name = 'lab/client/clientcompany_list.html'
    model = ClientCompany
    context_object_name = 'clients'

class ClientCompanyCreateView(generic.CreateView):
    template_name = 'lab/client/clientcompany_create.html'
    form_class = ClientCompanyForm
    model = ClientCompany
    success_url = reverse_lazy('labsoft-lab-client-list')
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super(ClientCompanyCreateView, self).get_context_data(**kwargs)
        ClientEmployeeFormSet = inlineformset_factory(ClientCompany, ClientEmployee, extra=2)
        if self.request.POST:
            context['clientemployee_formset'] = ClientEmployeeFormSet(self.request.POST)
        else:
            context['clientemployee_formset'] = ClientEmployeeFormSet()
        context['view_type'] = 'Create'
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        clientemployee_form = context['clientemployee_formset']
        
        if clientemployee_form.is_valid():
            self.object = form.save()
            clientemployee_form.instance = self.object
            clientemployee_form.save()
            return HttpResponseRedirect(reverse('labsoft-lab-client-list'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
    
class ClientCompanyUpdateView(generic.UpdateView):
    template_name = 'lab/client/clientcompany_update.html'
    form_class = ClientCompanyForm
    model = ClientCompany
    context_object_name = 'client'
    success_url = reverse_lazy('labsoft-lab-client-list')
    
    def get_context_data(self, **kwargs):
        context = super(ClientCompanyUpdateView, self).get_context_data(**kwargs)
        ClientEmployeeFormSet = inlineformset_factory(ClientCompany, ClientEmployee, extra=2, can_delete=True)
        
        if self.request.POST:
            context['clientemployee_formset'] = ClientEmployeeFormSet(
                self.request.POST,
                instance=self.object
            )
        else:
            context['clientemployee_formset'] = ClientEmployeeFormSet(
                instance=self.object
            )
            
        context['view_type'] = 'Update'
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        clientemployee_form = context['clientemployee_formset']
        
        if clientemployee_form.is_valid():
            self.object = form.save()
            clientemployee_form.instance = self.object
            clientemployee_form.save()
            return HttpResponseRedirect(reverse('labsoft-lab-client-list'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
    

class ClientCompanyDetailView(generic.DetailView):
    template_name = 'lab/client/clientcompany_detail.html'
    model = ClientCompany


