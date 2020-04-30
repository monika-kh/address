from django.contrib import admin

from .models import State, Block, District, Ward

# Register your models here.
admin.site.register(State)
admin.site.register(District)
admin.site.register(Block)
admin.site.register(Ward)
