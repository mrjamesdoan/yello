from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'questionnaire'


router = DefaultRouter()
router.register(r'', views.QuestionnaireViewSet, base_name='user')
urlpatterns = router.urls
