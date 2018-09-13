from django.shortcuts import render
from rest_framework import status, viewsets, serializers, response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Questionnaire, ResponseOption, UserQuestionnaire, UserResponse
from rest_framework.response import Response
# Create your views here.

class ResponseOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseOption
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):

    response_options = ResponseOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ('prompt', 'response_types', 'response_options')

class QuestionnaireSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Questionnaire
        fields = ('name', 'questions')

class QuestionnaireViewSet(viewsets.ModelViewSet):



    def list(self, request):
        queryset = Questionnaire.objects.all()
        serializer = QuestionnaireSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        return HttpResponse("hi")

    def retrieve(self, request, pk=None):
        queryset = Questionnaire.objects.filter(name=pk)
        serializer = QuestionnaireSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        return HttpResponse("hi")

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
