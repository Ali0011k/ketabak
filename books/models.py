from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField 
from django.utils.timezone import now

class Book(models.Model):
    name = models.CharField(max_length=200,verbose_name=_('book name'))
    author = models.CharField(max_length=200 , verbose_name=_('author'))
    number_of_pages = models.PositiveBigIntegerField(verbose_name=_('number of pages') )
    description = RichTextField(verbose_name=_('description') )
    create_time = models.DateField(verbose_name=_('Books publish time') , default=now)
    cover = models.PositiveIntegerField(verbose_name=_('Cover') , default=1)
    
    class Meta:
        db_table = 'Books'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
    
    def __str__(self):
        return self.name