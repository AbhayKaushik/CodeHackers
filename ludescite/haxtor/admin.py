from django.contrib import admin

# Register your models here.
from haxtor.models import Answers,Questions,Topic,User,UserProg

admin.site.register(Answers)
admin.site.register(Questions)
admin.site.register(Topic)
admin.site.register(User)
admin.site.register(UserProg)