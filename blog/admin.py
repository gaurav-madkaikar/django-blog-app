from django.contrib import admin
from .models import Post

# Add, edit, delete the posts we have made
# Register your models here.

# Include Post on the Django Admin page
admin.site.register(Post)