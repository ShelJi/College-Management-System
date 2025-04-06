from django.views.generic import (TemplateView)


class IndexView(TemplateView):
    template_name = 'landing_page/index.html'


class ArtsView(TemplateView):
    template_name = 'course_details/arts.html'


class GalleryView(TemplateView):
    template_name = 'landing_page/gallery.html'

