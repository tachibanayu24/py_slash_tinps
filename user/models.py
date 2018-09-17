import uuid
from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField('ユーザ名', max_length=20)
    mail = models.EmailField('メールアドレス', max_length=128)
    pwd = models.CharField('パスワード', max_length=256)
    #icon_url
    created_at = models.DateTimeField('登録日', default=timezone.now)

    def __str__(self):
        return self.user_name
