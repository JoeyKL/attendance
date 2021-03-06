from django.db import models

# Create your models here.

class Subteam(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class HoursWorked(models.Model): #This model should probably be renamed
    timeIn = models.DateTimeField() #Attribute that displays the time the student clocked in
    timeOut = models.DateTimeField(blank=True, null=True) #Attribute that displays the time the student clocked out
    totalTime = models.FloatField(default=0) #Attribute that...wait...this could be restructured a little bit, or at the very least renamed
    autoLogout = models.BooleanField(default=False) #Boolean attribute that tells us if the entry was generated by our autoLogout script. In the future this will allow us to flag entries that were generated automatically and display them properly to our users

class Student(models.Model):
    name = models.CharField(max_length=50) #The student's name
    studentID = models.IntegerField() #The student's ID#. In the future this may end up being a robotics ID#, if we decide to make custom ID cards
    subteam = models.ForeignKey(Subteam) #What subteam the student is associated with. There are a few fringe cases (most notably the team captain), we should decide how we want to handle those.
    hoursWorked = models.ManyToManyField(HoursWorked, blank=True)
    lastLoggedIn = models.DateTimeField(null=True, blank=True) #Attribute that displays the last time this student logged in.
    atLab = models.BooleanField(default=False) #Boolean attribute that tells us if the student is at the lab.
    totalTime = models.FloatField(default=0)  #Attribute that...again, we need clarity on this one

    def __str__(self):
        return self.name
