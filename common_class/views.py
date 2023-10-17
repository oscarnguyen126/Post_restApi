from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CountrySerializer, LanguageSerializer
from .models import Country, Language
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q


class CountryList(APIView):
    def get(self, request):
        return Response(CountrySerializer(Country.objects.all(), many=True).data)


    def post(self, request):
        serializer = CountrySerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)


class CountryDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Country, pk=id)
    

    def get(self, request, id):
        country = self.get_object(id=id)
        serializer = CountrySerializer(country)
        return JsonResponse(serializer.data, status=200)
    

    def put(self, request, id):
        country = self.get_object(id=id)
        data = JSONParser().parse(request)
        serializer = CountrySerializer(country, data=data)

        if serializer.is_valid(raise_exception=True):
            country = serializer.save()
            country.update_by = request.user
            country.save()
            return JsonResponse(serializer.data, status=201)
        

    def delete(self, request, id):
        country = self.get_object(id=id)
        country.delete()
        return JsonResponse({"msg": "Country removed"}, status=204)


class LanguageList(APIView):
    def get(self, request):
        return Response(LanguageSerializer(Language.objects.all(), many=True).data)
    

    def post(self, request):
        serializer = LanguageSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)


class LanguageDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Language, pk=id)
    

    def get(self, request, id):
        language = self.get_object(id=id)
        serializer = LanguageSerializer(language)
        return JsonResponse(serializer.data, status=200)
    

    def put(self, request, id):
        language = self.get_object(id=id)
        data = JSONParser().parse(request)
        serializer = LanguageSerializer(language, data=data)

        if serializer.is_valid(raise_exception=True):
            language = serializer.save()
            language.update_by = request.user
            language.save()
            return JsonResponse(serializer.data, status=201)


    def delete(self, request, id):
        language = self.get_object(id=id)
        language.delete()
        return JsonResponse({"msg": "Language removed"}, status=204)
