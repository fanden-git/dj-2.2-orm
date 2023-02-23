from django.urls import path
from school.views import lists, Lists


urlpatterns = [
    path('', lists, name='lists'),
    path('lists/', Lists.as_view(), name='lists1'),
]
