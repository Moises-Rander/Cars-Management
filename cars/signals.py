from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


@receiver(post_delete, sender=Car)
def delete_car_image_on_delete(sender, instance, **kwargs):
    if instance.photo:
        instance.photo.delete(save=False)


@receiver(pre_save, sender=Car)
def delete_car_image_on_update(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            old_file = old_instance.photo

            if (old_file and old_file.name != instance.photo.name) or not instance.photo:
                old_file.delete(save=False)

        except sender.DoesNotExist:
            pass


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    if cars_value:
        CarInventory.objects.create(
            cars_count=cars_count,
            cars_value=cars_value,
        )
    else:
        CarInventory.objects.create(
            cars_count=cars_count,
            cars_value=0,
        )


@receiver(post_save, sender=Car)
def increment_car_count_on_create(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def decrement_car_count_on_delete(sender, instance, **kwargs):
    car_inventory_update()


@receiver(pre_save, sender=Car)
def default_bio_generator(sender, instance, **kwargs):
    if not instance.bio and not instance.pk:
        instance.bio = 'Texto default'
