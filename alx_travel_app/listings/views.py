from rest_framework import viewsets
from alx_travel_app.listings.models import Listing, Booking, Review
from alx_travel_app.listings.serializers import ListingSerializer, BookingSerializer, ReviewSerializer
import os
import requests
from django.http import JsonResponse
from .models import Payment
from django.views.decorators.csrf import csrf_exempt

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



CHAPA_URL = "https://api.chapa.co/v1/transaction/initialize"
CHAPA_VERIFY_URL = "https://api.chapa.co/v1/transaction/verify"

@csrf_exempt
def initiate_payment(request):
    if request.method == "POST":
        data = request.POST
        booking_reference = data.get("booking_reference")
        amount = data.get("amount")

        payload = {
            "amount": amount,
            "currency": "ETB",
            "email": "user@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "tx_ref": f"txn_{booking_reference}",
            "callback_url": "http://localhost:8000/verify-payment/",
        }

        headers = {
            "Authorization": f"Bearer {os.getenv('CHAPA_SECRET_KEY')}",
            "Content-Type": "application/json",
        }

        response = requests.post(CHAPA_URL, json=payload, headers=headers)
        res_data = response.json()

        if res_data.get("status") == "success":
            tx_ref = res_data["data"]["tx_ref"]
            Payment.objects.create(
                booking_reference=booking_reference,
                amount=amount,
                chapa_tx_ref=tx_ref,
                status="Pending",
            )
            return JsonResponse({"checkout_url": res_data["data"]["checkout_url"]})
        return JsonResponse(res_data, status=400)

@csrf_exempt
def verify_payment(request):
    if request.method == "GET":
        tx_ref = request.GET.get("tx_ref")
        headers = {
            "Authorization": f"Bearer {os.getenv('CHAPA_SECRET_KEY')}",
        }
        response = requests.get(f"{CHAPA_VERIFY_URL}/{tx_ref}", headers=headers)
        res_data = response.json()

        payment = Payment.objects.filter(chapa_tx_ref=tx_ref).first()
        if payment:
            payment.status = "Completed" if res_data["data"]["status"] == "success" else "Failed"
            payment.save()
        return JsonResponse(res_data)
