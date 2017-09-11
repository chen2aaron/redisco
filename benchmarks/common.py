from __future__ import absolute_import
from redisco import models


class Event(models.Model):
    name = models.Attribute()
    location = models.Attribute()

