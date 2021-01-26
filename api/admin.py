from django.contrib import admin
from .models import Profile, Tags, Question, Answers, AnsComment, QuesComment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(QuesComment)
admin.site.register(AnsComment)
