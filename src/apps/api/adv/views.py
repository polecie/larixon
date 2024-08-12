from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adv.models import Advert
from apps.api.adv.serializers import AdvertSerializer


class AdvertListAPIView(generics.ListAPIView):
    queryset = Advert.objects.select_related("city", "category").all()
    serializer_class = AdvertSerializer


class AdvertDetailAPIView(APIView):
    def get(self, request, advert_id: int):
        try:
            advert = Advert.objects.filter(id=advert_id).update(views=F("views") + 1)
            if advert == 0:
                return Response(status=404)
            advert = Advert.objects.select_related("city", "category").get(id=advert_id)
            serializer = AdvertSerializer(advert)
            return Response(serializer.data)
        except Advert.DoesNotExist:
            return Response(status=404)
