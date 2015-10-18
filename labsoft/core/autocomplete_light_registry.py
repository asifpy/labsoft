import autocomplete_light.shortcuts as autocomplete_light

from labsoft.core.models import(
    ClientCompany,
    Equipment,
    SampleRequestor
)


class ClientCompanyAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name']
    model = ClientCompany
    attrs = {
        'placeholder': 'Type company name',
        'data-autocomplete-minimum-character': 3
    }

autocomplete_light.register(ClientCompanyAutocomplete)


class EquipmentAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['serial_no']
    model = Equipment
    attrs = {
        'placeholder': 'Type Serial No.',
        'data-autocomplete-minimum-character': 3
    }

autocomplete_light.register(EquipmentAutocomplete)


class SampleRequestorAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name', 'company__name']
    model = SampleRequestor
    attrs = {
        'placeholder': 'Type Sample Requestor name',
        'data-autocomplete-minimum-character': 3
    }

autocomplete_light.register(SampleRequestorAutocomplete)
