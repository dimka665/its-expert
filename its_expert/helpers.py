
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML


class BootstrapFormHelper(FormHelper):
    form_tag = False
    label_class = 'col-lg-2'
    field_class = 'col-lg-2'


class RowBootstrapFormHelper(FormHelper):
    form_tag = False
    disable_csrf = True
    form_show_labels = False

    field_template = 'bootstrap3/layout/row_field.html'
    field_class = 'col-lg-2'

    layout = Layout(
        'title',
        'value',
        'datatype',
        # Remove button
        HTML('<div class="col-lg-1"><a class="btn btn-danger delete-row" href="javascript:avoid(0)">Remove</a></div>'),
    )
