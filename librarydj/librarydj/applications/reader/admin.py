from django.contrib import admin

# Models
from .models import Loan,Reader
# Register your models here.
admin.site.register(Reader)
admin.site.register(Loan)
