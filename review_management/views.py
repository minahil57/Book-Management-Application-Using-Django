from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from users.utils import JWTAuthentication
from book_management.models import Book
from .models import Review
from .serializers import AddReviewSerializer, GetReviewSerializer, UpdateReviewSerializer, DeleteReviewSerializer


class AddReviewView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self, request):
        data = request.data
        user = request.user
        print(user)

        
        # Assuming the book ID is passed in the review data
        book_id = data.get('book')
        
        # Fetch the book the review is being added for
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": False,
                "message": "Book not found."
            }, status=status.HTTP_404_NOT_FOUND)
        print(book.user)
        # Check if the user is trying to add a review to their own book
        if book.user == user:
            raise PermissionDenied("You cannot add a review for your own book.")
        
        # Proceed to create the review if the ownership check passes
        serializer = AddReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Pass the user and book to the serializer
            return Response({
                "status": True,
                "message": "Review added successfully"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": False,
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)



class GetSpecificBookReviews(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request, pk):
        pass

    def retrieve(self, request, pk):
        try:
            reviews = Review.objects.filter(book=pk)
        except Review.DoesNotExist:
            raise NotFound("Book not found.")
        # Set up the pagination class
        paginator = PageNumberPagination()
        paginator.page_size = 5  # Set the page size (you can adjust as needed)

        # Paginate the queryset
        paginated_reviews = paginator.paginate_queryset(reviews, request)
        serializer = GetReviewSerializer (paginated_reviews, many=True)
        return Response({
            "status": True,
            "data": serializer.data
        })


class EditReviewView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def update(self, request, pk):
        try: 
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            raise NotFound("Review not found.")

        if review.reviewer != request.user:
            raise PermissionDenied("You do not have permission to update this review.")

        serializer = UpdateReviewSerializer(instance=review, data=request.data, )
        if serializer.is_valid():
            serializer.update(review, request.data)
            return Response({
                "status": True,
                "message": "Review updated successfully"
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": False,
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    
    def partial_update(self, request, pk):
        return self.update(request, pk)



class DeleteReviewView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def destroy(self, request, pk):
        try: 
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            raise NotFound("Review not found.")

        if review.reviewer != request.user:
            raise PermissionDenied("You do not have permission to delete this review.")

        review.delete()
        return Response({
            "status": True,
            "message": "Review deleted successfully"
        }, status=status.HTTP_200_OK)
