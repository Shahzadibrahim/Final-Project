from django.contrib import admin
from .models import Home, Concepts

admin.site.site_header = 'MS DENIM'
# Home
admin.site.register(Home)

# Concepts
admin.site.register(Concepts)

