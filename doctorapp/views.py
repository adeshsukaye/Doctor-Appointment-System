from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.
# def index(request):
#     return HttpResponse("Hello Adesh")
def homePage(request):
    return render(request,'doctorapp/home.html')

def registerPage(request):
    return render(request,'doctorapp/register.html')

def Register(request):
    if request.POST['role']=="Patient":
        # storing the data which is come from html signup page
        role = request.POST['role'] 
        fname = request.POST['firstname']
        lname= request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        address = request.POST['address']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        #Checking email is already available in the database
        user = UserMaster.objects.filter(Email=email)

        if user:
            message = "Patient already exiested"
            return render(request,'doctorapp/register.html',{'err':message})
        else:
            if password == cpassword:
                
                # store information in table
                newuser = UserMaster.objects.create(
                    Role=role,
                    Email=email,
                    Password=password
                    )
                #Store information in patient table and here use foreign key 
                newPatient = Patient.objects.create(
                    user_id=newuser,
                    FirstName=fname,
                    LastName=lname,
                    Contact=contact,
                    Gender=gender,
                    Address=address

                )
                message = "Register Successfully!!!"
                
                return render(request,'doctorapp/login.html',{'err':message})
            else:
                error = "password and confirm password does not Matched!!!"
                return render(request, 'doctorapp/register.html',{'err': error})
    else:
        if request.POST['role'] == "Doctor":
            role = request.POST['role'] 
            fname = request.POST['firstname']
            lname= request.POST['lastname']
            email = request.POST['email']
            contact = request.POST['contact']
            gender = request.POST['gender']
            address = request.POST['address']
            password = request.POST['password']
            cpassword = request.POST['cpassword']

            user = UserMaster.objects.filter(Email=email)

            if user:
                message = "Doctor email is already in use."
                return render(request,'doctorapp/register.html',{'msg':message})
            else:
                if password == cpassword:
                    
                    newuser = UserMaster.objects.create(
                        Role=role,
                        Email=email,
                        Password=password
                        )
                    newdoc = Doctor.objects.create(
                        user_id=newuser,
                        FirstName=fname,
                        LastName=lname,
                        Contact=contact,
                        Gender=gender,
                        Address=address
                    )
                    return render(request, 'doctorapp/login.html')

def LoginPage(request):
    return render(request,'doctorapp/login.html')

def PatientIndex(request):
    return render(request,'doctorapp/patientindex.html')





def Login(request):
    if request.POST['role'] == 'Patient' :
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(Email=email)
        if user:
            if user.Password == password and user.Role == "Patient":
                patient = Patient.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['Role'] = user.Role
                request.session['FirstName'] = patient.FirstName
                request.session['LastName'] = patient.LastName
                request.session['Email'] = user.Email
                request.session['Password'] = user.Password
                return redirect('bookappointmentpage')
            else:
                message = "Password does not matched"
                return render(request,'doctorapp/login.html',{'msg':message})
        else:
            message = "User does not exiest"
            return render(request,'doctorapp/login.html',{'msg':message})
    else:
        if request.POST['role'] == 'Doctor':
            email = request.POST['email']
            password = request.POST['password']

            user = UserMaster.objects.get(Email=email)
            if user:
                if user.Password == password and user.Role == 'Doctor':
                    doctor=Doctor.objects.get(user_id = user)
                    request.session['id'] = user.id
                    request.session['Role'] = user.Role
                    request.session['FirstName'] = doctor.FirstName
                    request.session['LastName'] = doctor.LastName
                    request.session['Email'] = user.Email
                    request.session['Password'] = user.Password
                    return redirect('doctorindex')
                else:
                    message="password does not matched"
                    return render(request,'doctorapp/login.html',{'msg':message})
            else:
                message = "User does not Exiest"
                return render(request,'doctorapp/login.html',{'msg':message})




######################Doctor site#########################

def DoctorIndex(request):
    return render(request,'doctorapp/doctor/doctorindex.html')

def DoctorProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    doctor = Doctor.objects.get(user_id=user)
    return render(request, 'doctorapp/doctor/profile.html',{'user':user,'doctor':doctor})
def UpdateDoctorProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    doctor = Doctor.objects.get(user_id=user)
    return render(request, 'doctorapp/doctor/doctorprofileupdate.html',{'user':user,'doctor':doctor})

def UpdateDoctor(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.Role =="Doctor":
        doc = Doctor.objects.get(user_id=user)
        doc.FirstName = request.POST['firstname']
        doc.LastName = request.POST['lastname']
        user.Email = request.POST['email']
        doc.Contact = request.POST['contact'] 
        doc.Gender = request.POST['gender']
        doc.DateOfBirth = request.POST['dob']
        doc.Maritial_Status = request.POST['maritialstatus']
        doc.Degree = request.POST['degree']
        doc.ExpertIn = request.POST['expertin']
        doc.Address = request.POST['address']
        user.Password = request.POST['password']
        
        doc.save()
        user.save()
        url = f'/doctorprofile/{pk}'
        return redirect(url)

def SchedulePage(request):
    return render(request,"doctorapp/doctor/doctorindex.html")


def AddSchedulePage(request):
    return render(request,"doctorapp/doctor/addschedule.html")

def AddSchedule(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.Role == "Doctor":
        doc = Doctor.objects.get(user_id=user)
        doctor_schedule_date = request.POST['doctor_schedule_date']
        doctor_schedule_start_time = request.POST['doctor_schedule_start_time']
        doctor_schedule_end_time = request.POST['doctor_schedule_end_time']
        average_consulting_time = request.POST['average_consulting_time']
        
        newSchedule = Schedule.objects.create(
            Doctor_Id = doc,
            Doctor_Schedule_Date = doctor_schedule_date,
            Doctor_Schedule_Start_Time = doctor_schedule_start_time,
            Doctor_Schedule_End_Time = doctor_schedule_end_time,
            Average_Consulting_Time = average_consulting_time
        )
        print(newSchedule)
        message = " Add Schedule Successfully"
        # return render(request,'doctorapp/doctor/doctorindex.html',{'msg':message})
        return redirect('schedulelist')
        

def ScheduleList(request):
    
    all_list = Schedule.objects.all()

    return render(request,"doctorapp/doctor/doctorindex.html",{'all_list':all_list})

def AppointmentListPage(request):
    return render(request,'doctorapp/doctor/doctorappointment.html')

def AppointmentList(request):
    all_list = Appointment.objects.all()
    return render(request,'doctorapp/doctor/doctorappointment.html',{'all_list':all_list})

def EditSchedulePage(request,pk):
    schedule = Schedule.objects.get(pk=pk)
    return render(request,'doctorapp/doctor/editschedule.html',{'schedule':schedule})

def ScheduleDelete(request,pk):
    schedule = Schedule.objects.get(pk=pk)
    schedule.delete()
    return redirect('schedulelist')

# def EditSchedule(request,pk):
#     user = UserMaster.objects.get(pk=pk)
#     if user.Role == 'Doctor':
#         doctor = Doctor.objects.get(user_id=user)
#         schedule = Schedule.objects.get(Doctor_Id=doctor)
#         schedule.Doctor_Schedule_Date = request.POST['doctor_schedule_date']
#         schedule.Doctor_Schedule_Start_Time = request.POST['doctor_schedule_start_time']
#         schedule.Doctor_Schedule_End_Time = request.POST['doctor_schedule_end_time']
#         schedule.Average_Consulting_Time = request.POST['average_consulting_time']
#         schedule.save()
#         url = f'/schedulelist/{pk}'
#         return redirect(url)
def EditSchedule(request,pk):
        
    doctor = Doctor.objects.get(pk=pk)
    schedule = Schedule.objects.get(Doctor_Id=doctor)
    schedule.Doctor_Schedule_Date = request.POST['doctor_schedule_date']
    schedule.Doctor_Schedule_Start_Time = request.POST['doctor_schedule_start_time']
    schedule.Doctor_Schedule_End_Time = request.POST['doctor_schedule_end_time']
    schedule.Average_Consulting_Time = request.POST['average_consulting_time']
    schedule.save()
    url = f'/schedulelist/{pk}'
    return redirect(url)
    





#### Doctor Logout View

def DoctorLogout(request):
    # del request.session['Patient_Email_Address']
    # return redirect('home')
    try: 
        del request.session['Email']
        del request.session['Password']
    except:
        pass
    return redirect('homepage')


#################### Patient VIEWS ##########################
######Patient Profile
def PatientProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    patient = Patient.objects.get(user_id=user)
    return render(request, 'doctorapp/profile.html',{'user':user,'patient':patient})

def UpdatePatientProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    patient = Patient.objects.get(user_id=user)
    return render(request, 'doctorapp/profileupdate.html',{'user':user,'patient':patient})

def UpdatePatient(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.Role =="Patient":
        patient = Patient.objects.get(user_id=user)
        patient.FirstName = request.POST['firstname']
        patient.LastName = request.POST['lastname']
        user.Email = request.POST['email']
        patient.Contact = request.POST['contact']
        patient.Gender = request.POST['gender']
        patient.DateOfBirth = request.POST['dob']
        patient.Maritial_Status = request.POST['maritialstatus']        
        patient.Address = request.POST['address']
        user.Password = request.POST['password']
        
        patient.save()
        user.save()
        url = f'/patientprofile/{pk}'
        return redirect(url)


#### Patient Logout View

def PatientLogout(request):
    # del request.session['Patient_Email_Address']
    # return redirect('home')
    try:  
        del request.session['Patient_Email_Address']
        del request.session['Patient_Password']
    except:
        pass
    return redirect('homepage')

#Display Appointment details
def BookAppointmentpage(request):
    doc = Doctor.objects.all()
    all_list = Schedule.objects.all()
    return render(request,"doctorapp/bookappointment.html",{'all_list':all_list,'doc':doc})

def ApplyPage(request,pk):
    user = request.session['id']
    if user:
        patient = Patient.objects.get(user_id=user)
        schedule = Schedule.objects.get(id=pk)
        
    return render(request,'doctorapp/applyappointment.html',{'user':user,'patient':patient,'schedule':schedule})

def ApplyAppointment(request,pk):
    user = request.session['id']

    if user:
        patient = Patient.objects.get(user_id=user)
        schedule = Schedule.objects.get(id=pk)
        reason = request.POST['reason']
        appointment_date = request.POST['appointment_date']
        appointment_start_time = request.POST['appointment_start_time']
        appointment_end_time = request.POST['appointment_end_time']
        pcih = request.POST['pcih']
        newApply = Appointment.objects.create(
            Patient_Id = patient,
            Schedule_Id = schedule,
            Reason = reason,
            Appointment_Date = appointment_date,
            Appointment_Start_Time = appointment_start_time,
            Appointment_End_Time = appointment_end_time,
            Patient_Come = pcih            
            )
        message = "Apply Successfully!!!"
        return render(request,'doctorapp/applyappointment.html',{'msg':message})

def MyAppointmentpage(request):
    myappointment = Appointment.objects.all()
    return render(request,'doctorapp/myappointment.html',{'myapp':myappointment})




################### ADMIN SITE #############################

def DashboardPage(request):
    return render(request,"doctorapp/admin/admindashboard.html")


def AdminIndexPage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"doctorapp/admin/admindashboard.html")
    else:
        return redirect('adminloginpage')

def AdminLoginpage(request):
    return render(request,"doctorapp/admin/adminlogin.html")

def AdminLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == "admin" and password == "password":
        request.session['username'] = username
        request.session['password'] = password
        return redirect('dashboardpage')
    else:
        message = "Username and Password does not exiest"
        return render(request,"doctorapp/admin/adminlogin.html",{'err':message})

def AdminPatientList(request):
    all_user = UserMaster.objects.filter(Role="Patient")
   
    return render(request,"doctorapp/admin/adminpatientlist.html",{'all_user':all_user})

def PatintDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('adminpatientlist')


def AdminDoctorList(request):
    all_doctor = UserMaster.objects.filter(Role="Doctor")
   
    return render(request,"doctorapp/admin/admindoctorlist.html",{'all_doctor':all_doctor})

def DoctorDelete(request,pk):
    doctor = UserMaster.objects.get(pk=pk)
    doctor.delete()
    return redirect('admindoctorlist')

def VerifyDoctorPage(request,pk):
    # doctor = UserMaster.objects.get(pk=pk)
    doctor = UserMaster.objects.get(pk=pk)
    if doctor:
        return render(request,"doctorapp/admin/verifydoctor.html",{'doctor':doctor})

def adminUpdateDoctorProfile(request,pk):
    doctor = UserMaster.objects.get(pk=pk)
    if doctor:
        doctor.is_verified = request.POST['verify']
        doctor.save()
        return redirect('admindoctorlist')

def AdminLogout(request):
    # del request.session['Patient_Email_Address']
    # return redirect('home')
    try:  
        del request.session['username']
        del request.session['password']
    except:
        pass
    return redirect('homepage')

def PatientCount(request,pk):
    patient = UserMaster.objects.get(pk=pk)
    if patient:
        return render(request,'doctorapp/admin/admindashboard/html',{'patient':patient})










    
 




