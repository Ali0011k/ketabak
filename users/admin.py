from django.contrib import admin
from django.contrib.auth.models import User , Group
from django.contrib.auth.admin import UserAdmin , GroupAdmin

from import_export.admin import ImportExportModelAdmin , ImportExportMixinBase


class ImportExportMixin(ImportExportMixinBase):
    from_encoding = "utf-8-sig"


admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(ImportExportModelAdmin,ImportExportMixin,UserAdmin):
    pass

admin.site.unregister(Group)

@admin.register(Group)
class CustomUserAdmin(ImportExportModelAdmin,ImportExportMixin,GroupAdmin):
    pass