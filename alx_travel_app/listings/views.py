from rest_framework import viewsets
from alx_travel_app.listings.models import Listing, Booking, Review
from alx_travel_app.listings.serializers import ListingSerializer, BookingSerializer, ReviewSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """CRUD API for Listings"""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """CRUD API for Bookings"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """CRUD API for Reviews"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
