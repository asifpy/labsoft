import django_tables2 as tables
from django_tables2.utils import A

from labsoft.core.models import Equipment

class EquipmentTable(tables.Table):
    serial_no = tables.LinkColumn('labsoft-lab-equipment-detail', args=[A('pk')])
    contact_person = tables.Column(verbose_name="Contact Person ", accessor='contact_person.name')
    client = tables.Column(verbose_name="Client", accessor='contact_person.company.name')
    
    class Meta:
        model = Equipment
        empty_text = "Equipment doesn't exists"
        fields = ("serial_no", "id_no", "equipment_type", 'contact_person', 'client')
        attrs = {"class": "table table-bordered table-condensed"}