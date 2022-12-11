from django import forms

TECHNOLOGY_TAGS = [('django', 'Django'), ('flask', 'Flask'),
                   ('bootstrap', 'Bootstrap'),('sql','SQL'),('mongodb','MongoDB')]
 

class NewProjectForm(forms.Form):
    title = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
        attrs={"class": "form-control mb-3"}))
    image_url = forms.URLField(required=False, max_length=200, widget=forms.TextInput(
        attrs={"class": "form-control mb-3"}))
    # image = forms.ImageField(upload_to='img/portfolio/')
    description = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(
        attrs={"class": "form-control mb-3", "rows": 4}))
    
    # tags = forms.CharField(required=False,max_length=100, widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    github_url = forms.URLField(required=True, max_length=500, widget=forms.TextInput(
        attrs={"class": "form-control mb-3"}))
    tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TECHNOLOGY_TAGS,
    )
