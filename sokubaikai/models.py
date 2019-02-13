from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import datetime
# Create your models here.
# 同人即売会マスター


class DoujinMarketsM(models.Model):
    """"""

    now = datetime.datetime.now()
    today = '%Y-%m-%d'.format(now)
    now_time = '%H:%M'
    print(now_time)
    print(today)
    # 自動生成主キー
    # market_id = models.IntegerField
    market_name = models.CharField(max_length=255)
    market_version = models.IntegerField()
    market_place = models.CharField(max_length=255)
    market_date = models.CharField(max_length=255, default=today)
    market_start_time = models.CharField(max_length=255, default=now_time)
    market_memo = models.TextField()

    #日付型のバグ？
    # category = models.ManyToManyField(Category)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.market_name

