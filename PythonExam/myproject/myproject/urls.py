from django.urls import path, include

urlpatterns = [
    path('health_monitoring/', include('health_monitoring.urls')),
]