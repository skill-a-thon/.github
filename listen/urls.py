from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', login_page, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_func, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
