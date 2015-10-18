from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django_tables2 import SingleTableView

from labsoft.lab.testdata.forms import TestDataForm
from labsoft.lab.testdata.tables import TestDataTable
from labsoft.core.models import AnalysisTestData
from labsoft.core.helpers import make_preparation


class TestDataListView(SingleTableView):
    template_name = 'lab/testdata/testdata_list.html'
    model = AnalysisTestData
    context_object_name = 'testdatas'
    table_class = TestDataTable
    context_table_name = 'testdata_table'
    table_pagination = {"per_page": 15}

    def get_queryset(self):
        objs = self.model.objects.all()
        search = self.request.GET.get('search')

        if search:
            objs = objs.filter(testname__icontains=search)
        return objs


class TestDataCreateView(generic.CreateView):
    template_name = 'lab/testdata/testdata_create.html'
    form_class = TestDataForm
    model = AnalysisTestData

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        self.object = form.save()
        make_preparation(self.object, self.request.user)
        return HttpResponseRedirect(reverse('labsoft-lab-testdata-list'))


class TestDataUpdateView(generic.UpdateView):
    template_name = 'lab/testdata/testdata_update.html'
    form_class = TestDataForm
    model = AnalysisTestData
    context_object_name = 'testdata'
    success_url = reverse_lazy('labsoft-lab-testdata-list')


class TestDataDetailView(generic.DetailView):
    template_name = 'lab/testdata/testdata_detail.html'
    model = AnalysisTestData
