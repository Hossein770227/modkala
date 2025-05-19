from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator



class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=255)
    description = models.TextField()
    brief_description = models.CharField(max_length=200, null=True, blank=True)
    inventory = models.IntegerField(_("inventory"), default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(_("image"), upload_to='cover/',)
    price_main = models.PositiveIntegerField(_("price main"))
    price_with_discount = models.PositiveIntegerField(_('price with discount'),blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        verbose_name = _("Product")  
        verbose_name_plural = _("Product")
        
    def __str__(self):
        return self.title
    
    def percent_discount(self):
        if self.price_with_discount:
            return (self.price_main - self.price_with_discount) / self.price_main * 100
        return 0
    
    
class ProductImageModel(models.Model):
    product = models.ForeignKey(Product ,on_delete=models.CASCADE, related_name="product_images")
    file = models.ImageField(upload_to='cover/')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]
        verbose_name = _("Product Image")  
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return f'images for {self.product.title}'
    
