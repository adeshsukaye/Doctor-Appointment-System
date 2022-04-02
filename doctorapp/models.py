from django.db import models

# Create your models here.
class UserMaster(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)
    is_active = models.BooleanField(default = True)
    is_verified = models.BooleanField(default = False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)    
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    DateOfBirth = models.DateField(auto_now_add=False,default='1999-08-15')
    Gender = models.CharField(max_length = 50)
    Contact = models.CharField(max_length = 50)   
    Address = models.CharField(max_length = 150)    
    Maritial_Status = models.CharField(max_length=50)

class Doctor(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)    
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    DateOfBirth = models.DateField(auto_now_add=False,default='1999-08-15')
    Gender = models.CharField(max_length = 50)
    Contact = models.CharField(max_length = 50)   
    Address = models.CharField(max_length = 150)    
    Maritial_Status = models.CharField(max_length=50)
    Degree = models.CharField(max_length=50)
    ExpertIn = models.CharField(max_length=50)
    Experience = models.CharField(max_length=50)
    Doctor_Status = models.CharField(max_length=50)

class Schedule(models.Model):
    Doctor_Id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Doctor_Schedule_Date = models.DateField(auto_now_add=False)
    Doctor_Schedule_Start_Time = models.TimeField(auto_now_add=False)
    Doctor_Schedule_End_Time = models.TimeField(auto_now_add=False)
    Average_Consulting_Time = models.CharField(max_length=50)
    Doctor_Schedule_Status = models.BooleanField(default=False)

class Appointment(models.Model):
    Patient_Id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Schedule_Id = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    Appointment_Number = models.CharField(max_length=50)
    Reason = models.CharField(max_length=100)
    Appointment_Date = models.CharField(max_length=100) 
    Appointment_Start_Time = models.CharField(max_length=100)
    Appointment_End_Time = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Patient_Come = models.CharField(max_length=100)
    Doctor_Comment = models.CharField(max_length=100)


   