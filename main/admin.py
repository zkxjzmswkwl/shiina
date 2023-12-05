from django.contrib import admin
from .models import *

admin.site.register(Character)
admin.site.register(Element)
admin.site.register(Region)
admin.site.register(Rarity)
admin.site.register(WeaponType)