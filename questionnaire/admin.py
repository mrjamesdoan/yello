from django.contrib import admin
from .models import ResponseOption, Question, Questionnaire, UserResponse, UserQuestionnaire
# Register your models here.
admin.site.register(Question)
admin.site.register(Questionnaire)
admin.site.register(UserResponse)
admin.site.register(UserQuestionnaire)
admin.site.register(ResponseOption)
