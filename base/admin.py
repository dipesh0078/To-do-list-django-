from django.contrib import admin
from .models import Task  #importing for registering our model/database table i.e Task
# Register your models here.

admin.site.register(Task) # regestring our Task table/model