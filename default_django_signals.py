#By default, Django signals are executed synchronously.

#Here's a code snippet that demonstrates this:

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(pre_save, sender=MyModel)
def slow_receiver(sender, instance, **kwargs):
    print("Slow receiver started")
    time.sleep(3)  # Simulate a slow operation
    print("Slow receiver finished")

@receiver(pre_save, sender=MyModel)
def fast_receiver(sender, instance, **kwargs):
    print("Fast receiver executed")

def test_signal_synchronous():
    obj = MyModel(name="Test")
    obj.save()
    print("Save operation completed")

test_signal_synchronous()


#Expected Output:
#Slow receiver started
#Slow receiver finished
#Fast receiver executed
#Save operation completed