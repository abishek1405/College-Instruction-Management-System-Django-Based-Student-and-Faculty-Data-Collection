
from django.contrib import admin
from django.urls import path, include
from authentication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authentication.urls')),
    path('work/',views.create_view),
    path('dddd/',views.fen),
    path('',views.come),

]
