from django.db import models
from datetime import datetime

class EmailAppModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    timestamp = models.DateTimeField(default=datetime.now())

    def __repr__(self):
        return "<Email: {}".format(self.first_name)
