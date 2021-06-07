from django.contrib import admin
from .models import *

class PollAdmin(admin.ModelAdmin):
    list_display = ['title',]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['poll','text','answer']


class UserToPollAdmin(admin.ModelAdmin):
    list_display = ['user','poll','points']
admin.site.register(Poll,PollAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(UserToPoll,UserToPollAdmin)