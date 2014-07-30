from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from its_expert.models import ObjectX


class CreateObjectXView(CreateView):
    model = ObjectX
    success_url = reverse_lazy('create-object-x')

    def get_context_data(self, **kwargs):
        object_list = ObjectX.objects.all()
        context = {'object_list': object_list}
        context.update(kwargs)
        return super(CreateObjectXView, self).get_context_data(**context)
