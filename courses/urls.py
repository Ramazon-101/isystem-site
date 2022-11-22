from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', about),
    # path('contact/', contact),
    path('courses/', courses_view),
    path('courses/<slug:slug>', courses_detail_view),
    # path('add/<int:a>/<int:b>', add_view),

]
