from django.db import models

from django.urls import reverse

class Product(models.Model):
  CATEGORY_CHOICES = [
    ("home", "Home"),
    ("tech", "Technology"),
    ("fashion", "Fashion"),
    ("wellness", "Wellness"),
  ]
  name_en = models.CharField(max_length=120)
  name_hy = models.CharField(max_length=120) 
  name_ru = models.CharField(max_length=120) 
  description_en = models.TextField()
  description_hy = models.TextField()
  description_ru = models.TextField()
  category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  stock = models.PositiveIntegerField(default=0)#qanak
  rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
  image = models.ImageField(upload_to="products/", null=True, blank=True)
  emoji = models.CharField(max_length=12, default="✨", null=True,blank=True)#default
  color = models.CharField(max_length=20, default="#f1eadf")
  is_featured = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ["-is_featured", "name_en"]
  def __str__(self):
    return self.name_en

  def get_absolute_url(self):
    return reverse("product_detail", args=[self.id])

  def localized_name(self, language): #en,ru,hy
    return getattr(self, f"name_{language}", self.name_en)
  
  def localized_description(self, language):
    return getattr(self, f"description_{language}", self.description_en)

  @property
  def in_stock(self):
    return self.stock > 0

      
