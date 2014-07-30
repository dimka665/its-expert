from django.forms import ModelForm

from its_expert.models import ObjectX


class ObjectXModelForm(ModelForm):
    model = ObjectX
