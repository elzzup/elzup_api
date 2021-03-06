from django.db import models


class Log(models.Model):
    """ログ"""
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    type = models.SmallIntegerField()
    # NOTE: 必要によって増やす
    value = models.CharField(max_length=256)
    timestamp = models.DateTimeField()
