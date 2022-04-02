
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.homePage,name="homepage"),
    path("registerpage/",views.registerPage,name="registerpage"),
    path('register/',views.Register,name="register"),
    path('loginpage/',views.LoginPage,name="loginpage"),
    path('patientindex/',views.PatientIndex,name="patientindex"),
    
    path('login/',views.Login,name="login"),

    ###################### DOCTOR SITE ########################

    path('doctorindex/',views.DoctorIndex,name="doctorindex"),
    path('doctorprofile/<int:pk>',views.DoctorProfile,name="doctorprofile"),
    path('updatedoctorprofile/<int:pk>',views.UpdateDoctorProfile,name="updatedoctorprofile"),
    path('updatedoctor/<int:pk>',views.UpdateDoctor,name="updatedoctor"),
    path('schedulepage/',views.SchedulePage,name="schedulepage"),
    path('addschudulepage/',views.AddSchedulePage,name="addschudulepage"),
    path('addschedule/<int:pk>',views.AddSchedule,name="addschedule"),
    path('schedulelist/',views.ScheduleList,name='schedulelist'),
    path('doctorlogout/',views.DoctorLogout,name='doctorlogout'),
    path('appointmentlistpage/',views.AppointmentListPage,name='appointmentlistpage'),
    path('appointmentlist/',views.AppointmentList,name='appointmentlist'),
    path('editschedulepage/<int:pk>',views.EditSchedulePage,name='editschedulepage'),
    path('editschedule/<int:pk>',views.EditSchedule,name='editschedule'),
    path('scheduledelete/<int:pk>',views.ScheduleDelete,name='scheduledelete'),

    ###################### Patient SITE ########################
    path('patientlogout/',views.PatientLogout,name='patientlogout'),
    
    path('bookappointmentpage/',views.BookAppointmentpage,name='bookappointmentpage'),
    path('applypage/<int:pk>',views.ApplyPage,name='applypage'),
    path('applyappointment/<int:pk>',views.ApplyAppointment,name='applyappointment'),
    path('myappointmentpage/',views.MyAppointmentpage,name='myappointmentpage'),
    #######Patient Profile
    path('patientprofile/<int:pk>',views.PatientProfile,name='patientprofile'),
    path('patientupdateprofile/<int:pk>',views.UpdatePatientProfile,name='updatepatientprofile'),
    path('updatepatient/<int:pk>',views.UpdatePatient,name='updatepatient'),


    ################### ADMIN SITE #############################
    path('dashboardpage/',views.DashboardPage,name='dashboardpage'),
    path('adminindexpage/',views.AdminIndexPage,name='adminindexpage'),
    path('adminloginpage/',views.AdminLoginpage,name='adminloginpage'),
    path('adminlogin/',views.AdminLogin,name='adminlogin'),
    path('adminpatientlist/',views.AdminPatientList,name='adminpatientlist'),
    path('patientdelete/<int:pk>',views.PatintDelete,name='patientdelete'),
    path('admindoctorlist/',views.AdminDoctorList,name='admindoctorlist'),
    path('doctordelete/<int:pk>',views.DoctorDelete,name='doctordelete'),
    path('verifydoctorpage/<int:pk>',views.VerifyDoctorPage,name='verifydoctorpage'),
    path('adminupdatedoctorprofile/<int:pk>',views.adminUpdateDoctorProfile,name='adminupdatedoctorprofile'),
    path('adminlogout/',views.AdminLogout,name='adminlogout'),
    path('patientcount/<int:pk>',views.PatientCount,name='patientcount'),
    



    

    
]