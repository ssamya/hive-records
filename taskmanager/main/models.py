from django.db import models
from django.utils import timezone
from datetime import timedelta

class Equipment(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  availability = models.BooleanField(default=True)


class Recording(models.Model):
  name = models.CharField(max_length=100, default="Recording")
  timeslot = models.DateTimeField() 
  price_morning = models.DecimalField(max_digits=5, decimal_places=2)
  price_afternoon = models.DecimalField(max_digits=5, decimal_places=2)
  price_evening = models.DecimalField(max_digits=5, decimal_places=2)
  duration = models.DurationField() 
  details = models.TextField()

  def __str__(self):
      return f"{self.name} ({self.timeslot.strftime('%Y-%m-%d %H:%M')})"
  
  @staticmethod
  def get_available_timeslots(start_date=None, days=7):
      """
      Возвращает список доступных таймслотов на определённый период.
      """
      if start_date is None:
          start_date = timezone.now()
      
      # Таймслоты, например, с 9:00 до 18:00 с интервалом в 1 час
      slots = []
      for day in range(days):
        current_date = start_date + timedelta(days=day)
        for hour in range(9, 18):  # Таймслоты с 9:00 до 18:00
            slot = current_date.replace(hour=hour, minute=0, second=0, microsecond=0)
            if slot > timezone.now():
                slots.append(slot)
      return slots


class Mastering(models.Model):
  name = models.CharField(max_length=100, default="Mastering")
  price = models.DecimalField(max_digits=5, decimal_places=2, default=50)
  details = models.TextField()

class Mixing(models.Model):
  name = models.CharField(max_length=100, default="Mixing")  
  price = models.DecimalField(max_digits=5, decimal_places=2, default=70)  
  details = models.TextField()  


class MMA(models.Model):
  name = models.CharField(max_length=100, default="Mixing & Mastering")
  price = models.DecimalField(max_digits=10, decimal_places=2, default=100)
  details = models.TextField()

class Beat(models.Model):
  name = models.CharField(max_length=100, default="Beats")
  price_mp3 = models.DecimalField(max_digits=5, decimal_places=2, default=15)
  price_wav = models.DecimalField(max_digits=5, decimal_places=2, default=30)
  price_trackout = models.DecimalField(max_digits=5, decimal_places=2, default=50)
  price_exclusive = models.DecimalField(max_digits=5, decimal_places=2, default=100)
  details = models.TextField()