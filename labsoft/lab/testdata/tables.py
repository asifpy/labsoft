import django_tables2 as tables
from django_tables2.utils import A

from labsoft.core.models import AnalysisTestData


class TestDataTable(tables.Table):
    testname = tables.LinkColumn('labsoft-lab-sample-detail', args=[A('pk')])

    class Meta:
        model = AnalysisTestData
        empty_text = "Test data doesn't exists"
        fields = ('testname', 'type')
        attrs = {"class": "table table-bordered table-condensed"}
