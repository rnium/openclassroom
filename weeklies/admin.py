from django.contrib import admin
from weeklies.models import Weekly, PreClassFile, PreClassTutorial, InClassTutorial, PostClassTutorial
# Register your models here.

admin.site.register(Weekly)
admin.site.register(PreClassFile)
admin.site.register(PreClassTutorial)
admin.site.register(InClassTutorial)
admin.site.register(PostClassTutorial)