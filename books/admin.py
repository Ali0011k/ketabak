from .models import *
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name' , 'author']
    search_fields = ['name', 'author']
    fieldsets = (
        (_('Book Info'), 
        {
        "fields" : (
            "name",
            "author",
            "number_of_pages",
            "description", 
            "create_time",
            "cover" 
        )
        }),
    )
    
    add_fieldsets = (
        (
            _('Book Info'),
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "author",
                    "number_of_pages",
                    "description", 
                    "create_time",
                    "cover" 
                ),
            },
        ),
    )
   