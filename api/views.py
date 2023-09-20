from api.serializers import BookSerializer
from api.permissions import IsSuperUser
from books.models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated , IsSuperUser])
def book_list_and_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(instance=books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsSuperUser])
def book_update(request):
    try:
    
        id = request.GET.get('id')
        book = Book.objects.get(id = id)
        
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(instance=book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
