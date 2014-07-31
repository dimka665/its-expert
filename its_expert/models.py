from django.contrib.contenttypes import generic
from django.db.models import PositiveIntegerField, ForeignKey

from eav.models import BaseSchema, BaseEntity, BaseAttribute, BaseChoice


class Schema(BaseSchema):
    pass


class Choice(BaseChoice):
    schema = ForeignKey(Schema, related_name='choices')


class Attribute(BaseAttribute):
    schema = ForeignKey(Schema, related_name='attrs')
    choice = ForeignKey(Choice, blank=True, null=True)


class Object(BaseEntity):
    height = PositiveIntegerField(default=0)
    width = PositiveIntegerField(default=0)

    attrs = generic.GenericRelation(Attribute, object_id_field='entity_id', content_type_field='entity_type')

    @classmethod
    def get_schemata_for_model(self):
        return Schema.objects.all()

    def __unicode__(self):
        attrs = {
            'height': self.height,
            'width': self.width,
        }
        extra_attrs = {attr.schema.name: attr.value for attr in self.attrs.all()}
        attrs.update(extra_attrs)
        return 'Object {}'.format(attrs)
