from django.urls import path
from ..views.ethnic import EthnicView

ethnicRouter = [
    path('', EthnicView.get_ethnics, name='get_ethnics'),  # Remove the leading slash
]
