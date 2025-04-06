from django.urls import path
from landing_page.views import (IndexView,
                                ArtsView,
                                GalleryView)

app_name = 'landing_page'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('arts/', ArtsView.as_view(), name='arts'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
]