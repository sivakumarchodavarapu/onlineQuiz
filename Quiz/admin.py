from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(UserDetail)
admin.site.register(QuizResult)
admin.site.register(FinalResult)
