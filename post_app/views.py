from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer
from .models import Category, Post, PostStatus
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.timezone import now as djnow


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)
    
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):            
            category = serializer.save()
            category.create_by = request.user
            return JsonResponse(serializer.data, status=201)
        

class CategoryDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)
    
    
    def get(self, request, id):
        category = self.get_object(pk=id)
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data, status=200)


    def put(self, request, id):
        category = self.get_object(pk=id)
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)

        if serializer.is_valid(raise_exception=True):
            category = serializer.save()
            category.save()
            return JsonResponse(serializer.data, status=201)
        
    
    def delete(self, request, id):
        category = self.get_object(pk=id)
        category.delete()
        return JsonResponse({"msg": "Category removed"}, status=204)
        


