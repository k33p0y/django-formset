from django.db import models

class Profile(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.fname, self.lname)

class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name