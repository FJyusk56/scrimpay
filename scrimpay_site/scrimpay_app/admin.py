from django.contrib import admin

from .models import User
from .models import Service

admin.site.register(User)
admin.site.register(Service)
# Register your models here.
