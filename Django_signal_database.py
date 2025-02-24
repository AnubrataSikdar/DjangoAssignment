#Yes, by default, Django signals run in the same database transaction as the caller.

#Here's a code snippet that demonstrates this:



from django.db import models, transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    failed = models.BooleanField(default=False)

@receiver(pre_save, sender=MyModel)
def signal_receiver(sender, instance, **kwargs):
    if instance.name == "Fail":
        instance.failed = True
        raise Exception("Signal Failed")

def caller_function():
    try:
        with transaction.atomic():
            m = MyModel(name="Fail")
            m.save()
            print("Save completed")

    except Exception as e:
        print(f"Transaction rolled back: {e}")

# Test in a Django shell (python manage.py shell)
from your_app.models import MyModel, caller_function
caller_function()
print(MyModel.objects.all())

def caller_function_success():
    try:
        with transaction.atomic():
            m = MyModel(name="Success")
            m.save()
            print("Save completed")

    except Exception as e:
        print(f"Transaction rolled back: {e}")

# Test in a Django shell (python manage.py shell)
from your_app.models import MyModel, caller_function_success
caller_function_success()
print(MyModel.objects.all())