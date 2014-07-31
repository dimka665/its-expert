
from django.forms import ModelForm, CharField, ChoiceField
from django.forms.formsets import formset_factory
from django.forms.widgets import Select, TextInput

from eav.models import BaseSchema

from its_expert.models import Object, Schema
from its_expert.helpers import BootstrapFormHelper, RowBootstrapFormHelper


class ObjectModelForm(ModelForm):
    class Meta():
        model = Object

    @property
    def helper(self):
        return BootstrapFormHelper()


class AttributeModelForm(ModelForm):

    DATATYPE_CHOICES = (
        ('', '-------'),
        (BaseSchema.TYPE_TEXT, 'Text'),
        (BaseSchema.TYPE_FLOAT, 'Numeric'),
    )

    value = CharField(max_length=250, widget=TextInput(attrs={'class': 'form-control'}))
    datatype = ChoiceField(choices=DATATYPE_CHOICES, widget=Select(attrs={'class': 'form-control'}))

    class Meta():
        model = Schema
        fields = ('title', 'datatype')

        widgets = {
            'title': TextInput(attrs={'class': 'form-control text-right', 'placeholder': 'Attribute name'}),
        }

        help_texts = {
            'title': '',
        }

    def save(self, commit=True):
        # Schema default values
        self.instance.required = False
        self.instance.searched = False
        self.instance.filtered = False
        self.instance.sortable = False
        return super(AttributeModelForm, self).save(commit=commit)

    @property
    def helper(self):
        return RowBootstrapFormHelper()

AttributeFormSet = formset_factory(AttributeModelForm)
