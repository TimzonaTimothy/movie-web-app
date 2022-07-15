from django.db import models
from accounts.models import Account
# Create your models here.
class Payment(models.Model):
    STATUS = {
        ('Free', 'Free'),
        ('Month', 'Month'),
        ('Quarter', 'Quarter'),
        ('Bi-annual', 'Bi-annual'),
        ('Annual', 'Annual'),
    }

    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    plan = models.CharField(max_length=10, choices=STATUS, default='Free')
    ref = models.CharField(max_length=100,unique=True, null=True, blank=False)
    amount_paid = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.ref