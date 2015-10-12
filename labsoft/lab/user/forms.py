from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.contrib.auth.models import User
from labsoft.core.models import SampleRequestor

class UserForm(forms.ModelForm):
    requestor = forms.ModelChoiceField(queryset=None)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-4'
        self.helper.add_input(Submit('submit', 'Submit',
                                     css_class="col-sm-offset-2 btn-primary"))
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['requestor'].queryset = SampleRequestor.objects.filter(profile=None)
