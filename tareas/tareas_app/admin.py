from django.contrib import admin

# Register your models here.

from .models import Proyecto
from .models import Usuario
from .models import Tarea
# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Usuario)
admin.site.register(Tarea)
