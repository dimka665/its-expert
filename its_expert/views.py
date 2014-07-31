
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from its_expert.models import Object
from its_expert.forms import AttributeFormSet, ObjectModelForm


class CreateObjectView(FormView):

    template_name = 'its_expert/create-object.html'

    form_class = ObjectModelForm
    attrs_formset_class = AttributeFormSet

    object_form_prefix = 'object'
    attrs_formset_prefix = 'attrs'

    success_url = reverse_lazy('create-object')

    def get_form_kwargs(self):
        form_kwargs = super(CreateObjectView, self).get_form_kwargs()
        form_kwargs.pop('prefix', None)  # remove prefix cause it depends on form
        return form_kwargs

    def get(self, request, *args, **kwargs):
        form_kwargs = self.get_form_kwargs()

        object_form = self.form_class(prefix=self.object_form_prefix, **form_kwargs)
        attrs_formset = self.attrs_formset_class(prefix=self.attrs_formset_prefix, **form_kwargs)

        return self.render_to_response(self.get_context_data(form=object_form, attrs_formset=attrs_formset))

    def post(self, request, *args, **kwargs):
        form_kwargs = self.get_form_kwargs()

        object_form = self.form_class(prefix=self.object_form_prefix, **form_kwargs)
        attrs_formset = self.attrs_formset_class(prefix=self.attrs_formset_prefix, **form_kwargs)

        if object_form.is_valid() and attrs_formset.is_valid():
            return self.form_valid(object_form, attrs_formset)
        else:
            return self.form_invalid(object_form, attrs_formset)

    def form_valid(self, object_form, attrs_formset):
        extra_attrs = {}

        for attrs_form in attrs_formset:
            if attrs_form.cleaned_data:
                attribute = attrs_form.save()
                extra_attrs[attribute.name] = attrs_form.cleaned_data['value']

        Object.objects.create(**object_form.cleaned_data)

        return super(CreateObjectView, self).form_valid(object_form)

    def form_invalid(self, object_form, attrs_formset):
        return self.render_to_response(self.get_context_data(object_form=object_form, attrs_formset=attrs_formset))

    def get_context_data(self, **kwargs):
        context = {
            'object_list': Object.objects.order_by('-id'),
        }
        context.update(kwargs)
        return super(CreateObjectView, self).get_context_data(**context)
