from django.db import models

# Create your models here.

class JobApplication(models.Model):
    status_choice=[
        ('applied','Applied'),
        ('interviewing','Interviewing'),
        ('rejected','Rejected'),
        ('offered','Offered')
    ]
    company=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    status=models.CharField(max_length=100,choices=status_choice,default='applied')
    applied_date=models.DateTimeField(auto_now_add=True)
    notes=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.company} - {self.role}"