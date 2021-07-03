from django.db import models


class ListItem(models.Model):
    name = models.CharField(max_length=255, null=False)
    date_added = models.DateField(auto_created=True)