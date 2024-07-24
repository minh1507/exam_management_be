from django.urls import path
from ..views.ethnic import EthnicView

ethnicRouter = [
    path('', EthnicView.find_all, name='get_ethnics'),
    path('<int:pk>/', EthnicView.find_one, name='get_ethnic'),
]
