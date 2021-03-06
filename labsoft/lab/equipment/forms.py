from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import autocomplete_light.shortcuts as autocomplete_light

from labsoft.core.models import Equipment
from labsoft.core.helpers import common_form_excludes


class EquipmentForm(autocomplete_light.ModelForm):
    class Meta:
        model = Equipment
        exclude = common_form_excludes()
        autocomplete_fields = ['company']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-3'
        self.helper.add_input(Submit('submit', 'Submit',
                                     css_class="col-sm-offset-2 btn-primary"))
        super(EquipmentForm, self).__init__(*args, **kwargs)
