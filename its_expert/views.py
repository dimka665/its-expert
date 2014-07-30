from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from its_expert.models import ObjectX


class CreateObjectXView(CreateView):
    model = ObjectX
    success_url = reverse_lazy('create-object-x')
