# from django.conf.urls import url, re_path
# from django.views.generic import TemplateView
# from django.urls import path
# from .api import ListViewSet, CardViewSet
#
# urlpatterns = [
#     re_path(r'^lists/$', ListViewSet.as_view()),
#     url(r'^cards/$', CardViewSet.as_view()),
#     url(r'^home', TemplateView.as_view(template_name="scrumboard/home.html"))
# ]


from .api import ListViewSet, CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = router.urls
