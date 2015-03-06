from django.contrib import admin

from gjobs.models import *

# __all__ = ["Article","Category",'Tag',"ArticleTag",'Author',"Comment"]                                                                          
# Register your models here.

# admin.site.register(Article)
admin.site.register(Job)
admin.site.register(Jobhis)
admin.site.register(Group)
admin.site.register(Project)

