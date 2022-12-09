from ast import Return
from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import News
from .serializer import NewsSerializer
from rest_framework import status


class NewsAPI(APIView):
    permission_classes=(AllowAny,)
    def get(self,request):
        try:
            if 'id' in request.data:
                id = request.data['id']
                obj = News.objects.get(id=id)
                serializer = NewsSerializer(obj, many=False).data 
            else:
                obj = News.objects.all()
                print(obj)
                serializer = NewsSerializer(obj, many=True).data 
            return Response({'error':False, 'data':serializer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':True,'data':str(e)},status=status.HTTP_400_BAD_REQUEST)
        
            
                
        
    def post(self,request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error':False, 'data':'News post successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':True, 'data':'Error unable to post'}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request):
        try:
            id = request.data['id']
            obj = News.objects.get(id=id)
            serializer = NewsSerializer(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'error':False, 'data':'News post successfully edit'}, status=status.HTTP_202_ACCEPTED)
            return Response({'error':True,'data':'Unsucess news edit'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':True,'data':str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):
        try:
            id = request.data['id']
            obj = News.objects.get(id=id)
            obj.delete()
            return Response({'error':False, 'data':'News post successfully delete'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':True,'data':str(e)},status=status.HTTP_400_BAD_REQUEST)
    

    
