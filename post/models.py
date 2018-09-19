import uuid
from django.db import models
from django.utils import timezone
from user.models import User

class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField("カテゴリ名", max_length=10)

    def __str__(self):
        return self.category_name


class Tinps(models.Model):
    tinps_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.ForeignKey(
        User, on_delete=models.PROTECT,
    )
    title = models.CharField('タイトル', max_length=100)
    tinps_body = models.CharField('本文', max_length=1000)
    slashed_cnt = models.IntegerField("パイスラ回数", default=0)
    wached_cnt = models.IntegerField("閲覧回数", default=0)
    category = models.ManyToManyField(Category, blank=True)
    updated_at = models.DateTimeField('更新日', default=timezone.now)
    created_at = models.DateTimeField('登録日', default=timezone.now)

    def __str__(self):
        return self.title
