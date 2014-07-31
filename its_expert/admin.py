from django.contrib import admin

from eav.admin import BaseEntityAdmin, BaseSchemaAdmin

from its_expert.models import Object, Schema, Choice, Attribute


admin.site.register(Object, BaseEntityAdmin)
admin.site.register(Schema, BaseSchemaAdmin)
admin.site.register(Attribute)
admin.site.register(Choice)
