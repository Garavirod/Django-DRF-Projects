from django.contrib import admin

from .models import (
    Person,
    Hobie,
    Meeting,
)

# Models are registered here, remeber alwayas to make migratins afeter registering a model
admin.site.register(Person)
admin.site.register(Hobie)
admin.site.register(Meeting)
