
from django.urls import path
from .views import MessageViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register('messages', MessageViewSet)
urlpatterns = router.urls