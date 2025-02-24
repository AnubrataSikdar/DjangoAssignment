#Yes, Django signals run in the same thread as the caller.

#Here's a code snippet that demonstrates this

import threading
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)

@receiver(pre_save, sender=MyModel)
def my_signal(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

def my_view(request):
    print(f"View thread: {threading.current_thread().name}")
    my_model = MyModel(name="Test")
    my_model.save()
    return HttpResponse("OK")
	
#When you run this code and access the my_view view, 
#you'll see that both the view and the signal print the same thread name,
# which indicates that they're running in the same thread.