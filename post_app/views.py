from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer, PostStatusSerializer
from .models import Category, Post, PostStatus
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class PostStatusList(APIView):
    def get(self, request):
        status = PostStatus.objects.all()
        return Response(PostStatusSerializer(status, many=True).data)
    
    
    def post(self, request):
        serializer = PostStatusSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            status = serializer.save()
            return JsonResponse(serializer.data, status=201)
        

class PostStatusDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(PostStatus, pk=pk)
    

    def get(self, request, id):
        status = self.get_object(pk=id)
        serializer = PostStatusSerializer(status)
        return JsonResponse(serializer.data, status=200)
    

    def put(self, request, id):
        status = self.get_object(pk=id)
        data = JSONParser().parse(request)
        serializer = PostStatusSerializer(status, data=data)

        if serializer.is_valid(raise_exception=True):
            status = serializer.save()
            return JsonResponse(serializer.data, status=201)
    

    def delete(self, request, id):
        status = self.get_object(pk=id)
        status.delete()
        return JsonResponse({"msg": "Status removed"}, status=204)



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
        


