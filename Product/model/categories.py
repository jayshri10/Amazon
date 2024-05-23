from django.db import models

from django.db import models

class Categories(models.Model):
    categories = models.CharField(max_length=25)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        if self.parent:
            return f"{self.parent.categories} - {self.categories}"
        return self.categories