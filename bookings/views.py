from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import timedelta
from .forms import BookingForm
from .models import Booking, UnavailableDate
from blog.models import Car
from django.urls import reverse
from django.utils import timezone
from django.utils.dateparse import parse_date
import requests
from .models import BusyDate
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            car = form.cleaned_data['car']
            start_time = form.cleaned_data['period_start']
            end_time = form.cleaned_data['period_end']
            booking = form.save(commit=False)
            booking.save()

            # Store the unavailable date range
            UnavailableDate.objects.create(
                car=car,
                start_date=start_time,
                end_date=end_time
            )

            # Send email with form data
            subject = 'New Booking Submission'
            message = f'''
                A new booking has been submitted:
                Car: {car}
                Start Time: {start_time}
                End Time: {end_time}
                '''
            recipient_list = [settings.EMAIL_HOST_USER]  # Add your email address here
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

            messages.success(request, "Your booking has been successfully submitted.")
            return redirect(reverse('booking_confirmation'))  # Redirect to confirmation page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        # Set default values for period_start and period_end
        start_time = timezone.now()
        end_time = start_time + timedelta(days=1)
        initial_data = {'period_start': start_time, 'period_end': end_time}
        form = BookingForm(initial=initial_data)
        
        # Retrieve unavailable dates for selected car
        car_id = request.GET.get('car_id')  # Assuming the car_id is passed in the request
        if car_id:
            try:
                car = Car.objects.get(id=car_id)
                start_date = timezone.now().date()
                end_date = start_date + timedelta(days=30)  # Adjust this as needed
                response = requests.get(
                    reverse('get_unavailable_dates', args=[car_id]),
                    params={'start_date': start_date, 'end_date': end_date}
                )
                if response.status_code == 200:
                    unavailable_dates_str = response.text.split('\n')
                    unavailable_dates = [parse_date(date_str) for date_str in unavailable_dates_str]
                    form.fields['period_start'].unavailable_dates = unavailable_dates
                    form.fields['period_end'].unavailable_dates = unavailable_dates
                else:
                    messages.error(request, "Failed to retrieve unavailable dates.")
            except Car.DoesNotExist:
                messages.error(request, "Car not found.")
    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_confirmation(request):
    try:
        latest_booking = Booking.objects.latest('id')
    except Booking.DoesNotExist:
        latest_booking = None
        messages.error(request, "No bookings found.")
        return redirect('booking_form')  # Redirect back to booking form if no bookings found
    return render(request, 'bookings/booking_confirmation.html', {'booking': latest_booking})

def get_unavailable_dates(request, car_id):
    try:
        busy_dates = BusyDate.objects.filter(car_id=car_id)
        busy_dates_json = [{'title': 'Busy', 'start': str(busy.start_date), 'end': str(busy.end_date)} for busy in busy_dates]
        return JsonResponse(busy_dates_json, safe=False)
    except BusyDate.DoesNotExist:
        return JsonResponse([], safe=False)

def submit_booking(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Save the busy date to the database
        busy_date = BusyDate(car_id=car_id, start_date=start_date, end_date=end_date)
        busy_date.save()
        
        return redirect('booking_success')  # Redirect to success page after submission
    else:
        # Handle GET request
        # Render your booking form template
        return render(request, 'booking_confirmation.html')

def render_calendar(request):
    busy_dates = BusyDate.objects.all()
    busy_dates_json = [{'title': 'Unavailable', 'start': str(busy.start_date), 'end': str(busy.end_date)} for busy in busy_dates]
    return JsonResponse(busy_dates_json, safe=False)

def save_busy_dates(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        busy_dates = request.POST.getlist('busy_dates[]')  # Assuming busy_dates is sent as a list
        
        # Iterate over busy_dates list and create BusyDate instances
        for date_str in busy_dates:
            busy_date = BusyDate(car_id=car_id, start_date=date_str, end_date=date_str)
            busy_date.save()  # Save the instance to the database
        
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)