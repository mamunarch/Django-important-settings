
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # custom url
    url(r'^home/$', views.TestPage.as_view(), name='home'),
    url(r'^login/$', views.login_page, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # if not using the CDN



# very very Important
# following process is used in the production stage
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
