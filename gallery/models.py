from django.db import models

class Images(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Desc = models.CharField(max_length=200, null=True)
    Category = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.Name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




