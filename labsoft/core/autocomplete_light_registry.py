import autocomplete_light.shortcuts as autocomplete_light

from labsoft.core.models import ClientCompany


class ClientCompanyAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name']
    model = ClientCompany
    attrs = {
        'placeholder': 'Type company name',
        'data-autocomplete-minimum-character': 3
    }

autocomplete_light.register(ClientCompanyAutocomplete)
