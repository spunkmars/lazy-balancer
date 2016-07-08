from __future__ import unicode_literals

from django.db import models

# Create your models here.
class main_config(models.Model):
    worker_processes = models.IntegerField(null=False)
    worker_connections = models.IntegerField(null=False)
    keepalive_timeout = models.IntegerField(null=False)
    client_max_body_size = models.CharField(max_length=16,null=False)
    access_log = models.CharField(max_length=128,null=True)
    error_log = models.CharField(max_length=128,null=True)
    update_time = models.FloatField(null=False)




