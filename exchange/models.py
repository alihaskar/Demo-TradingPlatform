from django.db import models
from django.conf import settings
# from django.conf import DEFAULT_CONTENT_TYPE_DEPRECATED_MSG


class TradeHistory(models.Model):
	usr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
	id = models.AutoField(primary_key=True)
	type = models.CharField(max_length=4)
	pair = models.CharField(max_length=10, default=None)
	histAmount = models.JSONField(default=None)
	amount = models.CharField(max_length=20)
	price = models.FloatField()
	time = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Trade histories'


class Portfolio(models.Model):
	usr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
	cryptoName = models.CharField(max_length=10, default=None)
	amount = models.FloatField(default=0, null=True)
	equivalentAmount = models.FloatField(default=0, null=True)



