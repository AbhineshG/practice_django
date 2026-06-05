
from django.urls import path
from .views import register,login,dashboard,loginPosts,userProfiles,aboutus,service,policy,faq,contact,booknow,profileUpdateMainPageLoading,profileUpdate,fileTesting,fileTestingUpload,useraboutus,userservice,userpolicy,userfaq,usercontact,userbooknow,userprofileUpdate,userprofileUpdateMainPageLoading,theater,booknowUpdate,slotbooking_theatre,slotbooking_select_Date,slotbooking_final,slotbooking_fetchUsers



urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('loginPosts/',loginPosts,name='loginPosts'),
    path('dashboard/',dashboard,name='dashboard'),
    path('aboutus/',aboutus,name='aboutus'),
    path('service/',service,name='service'),
    path('policy/',policy,name='policy'),
    path('faq/',faq,name='faq'),
    path('contact/',contact,name='contact'),
    path('booknow/',booknow,name='booknow'),
    
    path('fileTesting/',fileTesting,name='fileTesting'),
    path('fileTestingUpload/',fileTestingUpload,name='fileTestingUpload'),
    
    path('userDashboard/',userProfiles,name='userProfiles'),
    path('profileUpdate/',profileUpdate,name='profileUpdate'),
    path('profileUpdateMainPageLoading/',profileUpdateMainPageLoading,name='profileUpdateMainPageLoading'), 
    path('user/aboutus/',useraboutus,name='useraboutus'),
    path('user/service/',userservice,name='userservice'),
    path('user/policy/',userpolicy,name='userpolicy'),
    path('user/faq/',userfaq,name='userfaq'),
    path('user/contact/',usercontact,name='usercontact'),
    path('user/booknow/',userbooknow,name='userbooknow'),
    
  
    path('user/profileUpdate/',userprofileUpdate,name='userprofileUpdate'),
    path('user/theater/',theater,name='theater'),
    
    path('user/profileUpdateMainPageLoading/',userprofileUpdateMainPageLoading,name='userprofileUpdateMainPageLoading'),
    
    path('user/booknowUpdate/',booknowUpdate,name='booknowUpdate'),
    path('user/slotbooking_theatre/',slotbooking_theatre,name='slotbooking_theatre'),
    
    path('user/slotbooking_select_Date/',slotbooking_select_Date,name='slotbooking_select_Date'),
    path('user/slotbooking_final/',slotbooking_final,name='slotbooking_final'),
    
    path('slotbooking_fetchUsers/',slotbooking_fetchUsers,name='slotbooking_fetchUsers'),
    
]