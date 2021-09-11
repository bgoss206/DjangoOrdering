from django import forms
from django.utils.timezone import now
from .models import Jobsite


class CreateNewOrder(forms.Form):
    name = forms.CharField(label="Employee Name", max_length = 200, required = True)
    jobsite = forms.ChoiceField(label="Jobsite", choices=[("", "-------------Select Jobsite------------")] + [(i, i) for i in Jobsite.objects.all()], required = True)
    date_needed = forms.DateField(label="Date Needed", widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")), initial = now, required = True)
    def __init__(self, *args, **kwargs):
        sundries = kwargs.pop('sundries')
        equipment = kwargs.pop('equipment')

        super(CreateNewOrder, self).__init__(*args, **kwargs)

        for sundry in sundries:
            quantity_list = [(i, i) for i in range(sundry.quantity_available + 1)]
            self.fields[sundry.name] = forms.ChoiceField(label="Sundry", widget=forms.Select(attrs={'class': 'w-25'}), choices=quantity_list)
            if sundry.quantity_available == 0:
                self.fields[sundry.name + "- OUT OF STOCK"] = self.fields.pop(sundry.name)

        for equipment in equipment:
            self.fields["EQUIPMENT: " + equipment.name] = forms.IntegerField(label="Equipment", required=False, initial=0)