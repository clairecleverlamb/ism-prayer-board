from django.db import models
from django.contrib.auth.models import User

class PrayerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    ministry_group = models.CharField(max_length=100, blank=True, null=True)  
    status = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()  # The actual prayer request
    date_posted = models.DateTimeField(auto_now_add=True)
    prayed_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.student_name} - {self.content[:30]}"
