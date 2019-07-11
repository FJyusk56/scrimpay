from django.db import models

# Create your models here.
class User(models.Model):
    # ユーザーID : int型 主キー
    userid = models.IntegerField(primary_key=True)
    # ユーザー名 : char型
    username = models.CharField(max_length=30)
    # パスワード : char型
    password = models.CharField(max_length=16)

class Service(models.Model):
    # サービスID : int型 主キー
    serviceid = models.IntegerField(primary_key=True)
    # サービスの名称 : char型
    servicename = models.CharField(max_length=30)
    # 契約期間単位の費用 : int型
    price = models.IntegerField()
    # 解約金 : int型
    cancelfee = models.IntegerField()
    # 未使用分の返金 : int型
    refund = models.IntegerField()rim
    # 備考(解約時の補償など) : char型
    note = models.CharField(max_length=200)