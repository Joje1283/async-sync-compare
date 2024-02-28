from django.db import models


class Item(models.Model):
    class Meta:
        db_table = "item"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
