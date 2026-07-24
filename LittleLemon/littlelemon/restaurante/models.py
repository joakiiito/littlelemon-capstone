from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    class Meta:
        # No two bookings on the same date and slot
        unique_together = ('reservation_date', 'reservation_slot')

    def __str__(self):
        return f'{self.first_name} - {self.reservation_date} @ {self.reservation_slot}:00'
