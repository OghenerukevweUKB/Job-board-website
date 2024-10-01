from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.


class Company(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Website = models.URLField(max_length=200)

    def __str__(self):
        return self.Name


class Job(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Location = models.CharField(max_length=255)
    Salary = models.DecimalField(max_digits=9,decimal_places=2)
    Open_date = models.DateTimeField(auto_now_add=True)
    Last_date_to_apply = models.DateTimeField(auto_now=True)
    Is_active = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.Title


class Application(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),

    ]

    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)
    Email = models.EmailField()
    Location = models.CharField(max_length=255)
    Years_of_experience = models.DecimalField(max_digits=9, decimal_places=2)
    Why_you_are_fit_for_the_job = models.TextField()
    Position_applying_to = models.CharField(max_length=255)
    Resume = models.FileField(upload_to='resume')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.User.username} applied for {self.Job.Title}'

    def Send_email(self, subject, message):
        send_mail(
            subject,
            message,
            company_name,
            [self.user.email],
            fail_silently=False
        )


class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Is_company = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.User.username} Profile'
