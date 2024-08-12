from django.urls import path

from apps.api.adv import views as adv_views

urlpatterns = [
    path('advert-list', adv_views.AdvertListAPIView.as_view(), name='advert-list'),
    path('advert/<int:advert_id>', adv_views.AdvertDetailAPIView.as_view(), name='advert-detail'),
]