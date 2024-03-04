from django.contrib import admin

# Register your models here.
from .models  import bookdetail,bookdetailAdmin
admin.site.register(bookdetail,bookdetailAdmin)
