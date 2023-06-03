from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls', namespace='task')),
    path('category/', include('category.urls', namespace='category')),
]
