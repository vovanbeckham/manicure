from django.db import models
from PIL import Image

class Album(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=255, default='')
    content =models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='context/%Y/%m/%d/', max_length=500, null=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    def save(self):
        super().save()

        imgage = Image.open(self.img.path)

        if imgage.height > 300 or imgage.width > 300:
            output_size = (300, 300)
            imgage.thumbnail(output_size)
            imgage.save(self.img.path)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self) -> str:
        return self.name

