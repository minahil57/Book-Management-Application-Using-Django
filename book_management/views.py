import os
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.pagination import PageNumberPagination

from users.utils import JWTAuthentication
from .serializers import AddBookSerializer, GetBookSerializer, UpdateBookSerializer
from .models import Book
from users.models import User
# from .utils import CustomJWTAuthentication


class AddBookView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
          # Check if 'bookImage' is in the request (uploaded file)
        if 'bookImage' in request.FILES:
            book_image = request.FILES['bookImage']
            data['bookImage'] = book_image

        # Set the authenticated user as the owner of the book
        data['user'] = request.user.id
        serializer = AddBookSerializer(data=data)
      
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Book added successfully"
            })
        else:
            return Response({
                "status": False,
                "message": serializer.errors
            })


class GetBookList(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    def list(self, request):
        books = Book.objects.filter(user=request.user)
        # Set up the pagination class
        paginator = PageNumberPagination()
        paginator.page_size = 5  # Set the page size (you can adjust as needed)

        # Paginate the queryset
        paginated_books = paginator.paginate_queryset(books, request)

        serializer = GetBookSerializer(paginated_books, many=True)
        return Response({
            "status": True,
            "data": serializer.data
        })

class UpdateBookView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    def update(self, request, pk=None):
        try:
            # Fetch the book by its ID
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            # If the book is not found, raise a 404 error
            raise NotFound("Book not found.")

        # Check if the authenticated user is the owner of the book
        if book.user != request.user:
            # If not the owner, raise a PermissionDenied exception
            raise PermissionDenied("You do not have permission to update this book.")

        # Proceed with updating the book using the provided data
        serializer = UpdateBookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Book updated successfully"
            }, status=status.HTTP_200_OK)
        else:
            # Return errors if the serializer is invalid
            return Response({
                "status": False,
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        return self.update(request, pk)


class DeleteBookView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]

    def destroy(self, request, pk=None):
        try:
            # Get the book by its ID
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            # If the book is not found, return a 404 error
            raise NotFound("Book not found.")

        # Check if the requesting user is the owner of the book
        if book.user != request.user:
            # If the user does not own the book, raise a PermissionDenied exception
            raise PermissionDenied("You do not have permission to delete this book.")

        # If ownership is verified, delete the book
        book.delete()

        # Return success response
        return Response({
            "status": True,
            "message": "Book deleted successfully"
        }, status=status.HTTP_200_OK)



class GetBookView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    def retrieve(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = GetBookSerializer(book)
        return Response({
            "status": True,
            "data": serializer.data
        })