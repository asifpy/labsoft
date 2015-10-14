from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django_tables2 import SingleTableView

from labsoft.core.helpers import make_preparation
from labsoft.core.models import ClientCompany, SampleRequestor
from labsoft.lab.client.forms import ClientCompanyForm
from labsoft.lab.client.tables import ClientCompanyTable


class ClientCompanyListView(SingleTableView):
    template_name = 'lab/client/clientcompany_list.html'
    model = ClientCompany
    context_object_name = 'clients'
    table_class = ClientCompanyTable
    context_table_name = 'company_table'
    table_pagination = {"per_page": 15}

    def get_queryset(self):
        objs = self.model.objects.all()
        search = self.request.GET.get('search')

        if search:
            objs = objs.filter(name__icontains=search)
        return objs


class ClientCompanyCreateView(generic.CreateView):
    template_name = 'lab/client/clientcompany_create.html'
    form_class = ClientCompanyForm
    model = ClientCompany
    success_url = reverse_lazy('labsoft-lab-client-list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(
            ClientCompanyCreateView, self
            ).get_context_data(**kwargs)
        ClientEmployeeFormSet = inlineformset_factory(
            ClientCompany,
            SampleRequestor,
            extra=2,
            exclude=('company',))

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
            company = form.save(commit=False)
            make_preparation(company, self.request.user)

            clientemployee_form.instance = company
            client_employees = clientemployee_form.save(commit=False)
            update_prepared_by(client_employees, self.request.user)

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
        context = super(
            ClientCompanyUpdateView, self
            ).get_context_data(**kwargs)
        ClientEmployeeFormSet = inlineformset_factory(
            ClientCompany,
            SampleRequestor,
            exclude=('company',),
            extra=2, can_delete=True)

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
            company = form.save()
            clientemployee_form.instance = company
            clientemployees = clientemployee_form.save(commit=False)
            update_prepared_by(clientemployees, self.request.user)

            return HttpResponseRedirect(reverse('labsoft-lab-client-list'))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ClientCompanyDetailView(generic.DetailView):
    template_name = 'lab/client/clientcompany_detail.html'
    model = ClientCompany


def update_prepared_by(client_employees, user):
    for employee in client_employees:
        make_preparation(employee, user)
