import django_tables2 as tables
from django_tables2.utils import A

from labsoft.core.models import EquipmentSample

class EquipmentSampleTable(tables.Table):
    sample_no = tables.LinkColumn('labsoft-lab-sample-detail', args=[A('pk')])
    serial_no = tables.Column(verbose_name="Equipment", accessor='equipment.serial_no')
    contact_person = tables.Column(verbose_name="Contact Person ", accessor='equipment.contact_person.name')
    client = tables.Column(verbose_name="Client", accessor='equipment.contact_person.company.name')
    
    class Meta:
        model = EquipmentSample
        empty_text = "Sample doesn't exists"
        fields = ("sample_no", 'serial_no', 'contact_person', 'client')
        attrs = {"class": "table table-bordered table-condensed"}