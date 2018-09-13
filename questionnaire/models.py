
from django.db import models
from django.conf import settings

class ResponseOption(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Question(models.Model):

    prompt = models.CharField(max_length=255)
	# A question can have many response options.
	# A response option can be part of many questions.

    RADIO = 'RA'
    CHECKLIST = 'CH'
    TEXT = 'TE'
    RESPONSE_TYPE_CHOICES = (
        ('RADIO', 'Radio'),
        ('CHECKLIST', 'Checklist'),
        ('TEXT', 'Text'),
    )
    response_types = models.CharField(max_length=200, choices=RESPONSE_TYPE_CHOICES, default=TEXT)
    response_options = models.ManyToManyField(ResponseOption, blank=True)

    def __str__(self):
        return self.prompt


# Create your models here.
class Questionnaire(models.Model):
    name = models.CharField(max_length=255)
	# A questionnaire can have many questions.
	# A question can be part of many questionnaires.
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name

class UserQuestionnaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.questionnaire.name

class UserResponse(models.Model):
    user_Questionnaire = models.ForeignKey(UserQuestionnaire, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_option = models.ForeignKey(ResponseOption, on_delete=models.CASCADE)
    def __str__(self):
        return self.response_option
