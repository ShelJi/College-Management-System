from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls')),
    path('accounts/', include('accounts.urls')),
    path('staff/', include('staff_dashboard.urls')),
    path('student/', include('student_dashboard.urls')),
    path('exam/', include('exam.urls')),
    path('review/', include('review.urls')),
    path('invalid/', include("core.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)