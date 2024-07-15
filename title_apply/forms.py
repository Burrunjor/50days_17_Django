from django import forms

# so this is the schema for the form, not the dbase, which is already done, but it looks the same, so it was copy and paste
# but the models class needs to be replaced by "forms"


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    current_titles = forms.CharField(max_length=80)