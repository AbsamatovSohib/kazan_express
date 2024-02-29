from django.contrib.auth import get_user_model
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(get_user_model(), related_name="role")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Roles"


class Shop(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=256)
    imageurl = models.CharField(max_length=127)

    objects = models.Manager

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Shops"


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product")

    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_main:
            self.product.image = self.image
            self.product.save()
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=256)

    amount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    active = models.BooleanField(default=False)
    main_photo = models.ImageField(upload_to='images/', blank=True, null=True,
                                   editable=False)

    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="categories")

    objects = models.Manager

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Products"


class Category(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=256)

    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shops")


    objects = models.Manager

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"
