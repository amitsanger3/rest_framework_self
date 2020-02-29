from django.urls import path, include  # include for viewsets
from . import views, views1, views2, views3, views4, views5, views6

from rest_framework.routers import DefaultRouter

# Routers
rout = DefaultRouter()
rout.register('viewset', views5.StudentViewSet, basename='student')
rout.register('modelviewset', views6.StudentModelViewSet, basename='student_model')

urlpatterns = [
    path('', views.index, name='index'),
    path('stlist', views.student_list),  # Function Base Serialization
    path('student/<int:pk>', views.edit_student),  # Function Base Serialization
    path('api', views1.student_list),  # Api View
    path('student_api/<int:pk>', views1.edit_student),  # Api View
    path('st1', views2.StudentApiView.as_view()), # Api View
    path('st1_edit/<int:pk>', views2.EditStudentApiView.as_view()),  # Class base view
    path('st2', views3.StudentGenericView.as_view()),  # Class base view
    path('st2_edit/<int:pk>', views3.EditStudentGenericView.as_view()), # Class base view
    path('st3/<int:pk>', views4.StudentGenericView.as_view()),  # For all in one class (Authentication & Permission)
    path('st4/', include(rout.urls)),  # Viewset & Routers
    path('st4/<int:pk>/', include(rout.urls)),  # Viewset & Routers
]