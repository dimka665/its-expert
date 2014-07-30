
from django.db.models import Model
from django.db.models import PositiveIntegerField


class ObjectX(Model):
    height = PositiveIntegerField()
    width = PositiveIntegerField()

    def __unicode__(self):
        attrs = {
            'height': self.height,
            'width': self.width,
        }
        attrs_str = ', '.join('{}={}'.format(*attr_item) for attr_item in attrs.items())
        return 'Object X ({attrs})'.format(attrs=attrs_str)
