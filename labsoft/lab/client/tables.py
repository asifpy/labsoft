import django_tables2 as tables
from django_tables2.utils import A

from labsoft.core.models import ClientCompany

class ClientCompanyTable(tables.Table):
    name = tables.LinkColumn('labsoft-lab-client-detail', args=[A('pk')])
    
    class Meta:
        model = ClientCompany
        empty_text = "Company doesn't exists"
        fields = ("name", 'id', 'prepared_by', 'prepared_on')
        attrs = {"class": "table table-bordered table-condensed"}