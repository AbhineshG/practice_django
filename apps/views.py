import email
from multiprocessing import context

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import BookNowLocations, BookNowSelectionsType, Register ,BookNowScreenType,UserBookDetails,BookNowSelectionsPeoples
from django.contrib.auth.hashers import make_password, check_password
import json



def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email') 
        password=request.POST.get('pswd')
        roles=request.POST.get('roles')
        print(username,email,password)
        
        if Register.objects.filter(email=email).exists():
            return render(request,'register.html',{'error':'Email already exists'})
        hasedPassword=make_password(password)
        Register.objects.create(username=username,email=email,password=hasedPassword,roles=roles)
        return redirect('login')
    return render(request,'register.html')


@csrf_exempt
def profileUpdate(request):
    if request.method == 'POST':
        username=request.POST.get('username')  
        email=request.POST.get('email') 
        contactNo=request.POST.get('contactNo')
        address=request.POST.get('address')
        
        print(username)
        
        if Register.objects.filter(email=email).exists():
            user=Register.objects.get(email=email)
            user.address=address
            user.contactNo=contactNo
            user.save()
            
            user=list(Register.objects.filter(email=email).values())
            return JsonResponse({'message':'Update successful','userData':user})
        else:
            print(email,"====line no 322222")
            return JsonResponse({'message':'User Data Was not found','error':'Invalid email or user data'})
         
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def userProfiles(request):
    return render(request,'user/userDashboard.html')

@csrf_exempt
def loginPosts(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        print(email,password)
        
        if Register.objects.filter(email=email).exists():
             
            user=list(Register.objects.filter(email=email).values())
            print(user,"====line no 30")
            if check_password(password,user[0]['password']):
                return JsonResponse({'message':'Login successful','userData':user})
        else:
            print(email,password,"====line no 322222")
            return JsonResponse({'message':'Login failed','error':'Invalid email or password'})
    return render(request,'login.html')

def dashboard(request):
    return render(request,'admin/dashboard.html')
def aboutus(request):
    return render(request,'admin/aboutus.html')
def service(request):
    return render(request,'admin/service.html')
def policy(request):
    return render(request,'admin/policy.html')
def faq(request):
    return render(request,'admin/faq.html')
def contact(request):
    return render(request,'admin/contact.html')
def booknow(request):
    return render(request,'admin/booknow.html') 
def profileUpdateMainPageLoading(request):
    return render(request,'admin/profileUpdate.html') 


 
def useraboutus(request):
    return render(request,'user/aboutus.html')
def userservice(request):
    return render(request,'user/service.html')
def userpolicy(request):
    return render(request,'user/policy.html')
def userfaq(request):
    return render(request,'user/faq.html')
def usercontact(request):
    return render(request,'user/contact.html')
def userbooknow(request):
    bookNow=list(BookNowLocations.objects.all().values())
    print(bookNow,"====line no 322222")
    context = {
        'locations': list(BookNowLocations.objects.all().values())
    }
    return render(request,'user/booknow.html',context) 

def userprofileUpdateMainPageLoading(request):
    return render(request,'user/profileUpdate.html') 

@csrf_exempt
def userprofileUpdate(request):
    if request.method == 'POST':
        username=request.POST.get('username')  
        email=request.POST.get('email') 
        contactNo=request.POST.get('contactNo')
        address=request.POST.get('address')
        
        print(username)
        
        if Register.objects.filter(email=email).exists():
            user=Register.objects.get(email=email)
            user.address=address
            user.contactNo=contactNo
            user.save()
            
            user=list(Register.objects.filter(email=email).values())
            return JsonResponse({'message':'Update successful','userData':user})
        else:
            print(email,"====line no 322222")
            return JsonResponse({'message':'User Data Was not found','error':'Invalid email or user data'})
         
    return render(request,'register.html')




@csrf_exempt
def booknowUpdate(request):
    if request.method == 'POST':
        userId=request.POST.get('userId')  
        bookNowIds=request.POST.get('bookNowId')  
        bookNowlocations=request.POST.get('locations')  
        
        print(userId,bookNowIds,bookNowlocations)
        
        if UserBookDetails.objects.filter(userId=userId).exists():
            user=UserBookDetails.objects.get(userId=userId)
            theaterType=BookNowScreenType.objects.filter(id=bookNowIds).exists()
            if bookNowlocations == "Hanamkonda , Warangal":
                user.mainLocationsId=bookNowIds 
                user.save()
            elif bookNowlocations == theaterType.title:
                user.bookNowScreenTypeId=bookNowIds 
                user.save()
            return JsonResponse({'message':'Update successful'})
        else:
            UserBookDetails.objects.create(adminId=4,userId=userId,mainLocationsId=bookNowIds)
            return JsonResponse({'message':'Update successful'})
         
    return render(request,'register.html')


def fileTesting(request):
    return render(request,'upload.html') 





def theater(request):
    bookNow=list(BookNowScreenType.objects.all().values())
    print(bookNow,"====line no 322222")
    context = {
        'bookNow': bookNow}
    
    return render(request,'user/selectTheaterPage.html',context) 


@csrf_exempt
def fileTestingUpload(request):
    
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            with open(f'static/{uploaded_file.name}', 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
    return JsonResponse({'message':'File uploaded successfully'})


def slotbooking_theatre(request):
    bookNow=list(BookNowSelectionsType.objects.all().values())
    no_of_peoples=list(BookNowSelectionsPeoples.objects.all().values())
    print(bookNow,"====line no 322222")
    context = {
        'bookNow': bookNow,
        'no_of_peoples': no_of_peoples
    }
    return render(request,'user/slotbooking_theatre.html',context) 


@csrf_exempt
def slotbooking_select_Date(request):
    if request.method == 'POST':
        userId=request.POST.get('userId')  
        date=request.POST.get('date') 
        print(userId,date)
        
        userData=UserBookDetails.objects.filter(bookNowSelectionsDate=date,userId=userId)
        print(userData,"====line no 21000000")
        
        if userData is not None:
            userData=list(UserBookDetails.objects.filter(bookNowSelectionsDate=date).values())
             
            adminbookNow=list(BookNowSelectionsType.objects.all().values())
            for items in adminbookNow:
                for user in userData:
                    if items["time_slot"] == user["bookNowSelectionsTimeSlots"] and user["bookNowSelectionsDate"] == date:
                        print(items ,"====line no 21999999")
                        print(user ,"====line no 220")
                        items["status"] = "Unavailable"
                    else:
                        print( items["time_slot"]," is available for booking")
                        
            
            
            return JsonResponse({'message':'Data received successfully','bookNow':adminbookNow}) 
        else:
            bookNow=list(BookNowSelectionsType.objects.all().values())
            print(bookNow,"====line no 322222")
            context = {
                'bookNow': bookNow}
            return JsonResponse({'message':'Data received successfully','bookNow':context}) 
    
    return JsonResponse({'message':'Data received successfully','bookNow':context})

@csrf_exempt
def slotbooking_final(request):
    if request.method == 'POST':
        userId=request.POST.get('userId')  
        date_global=request.POST.get('date_global') 
        timeSlotId=request.POST.get('timeSlotId') 
        counting_peoplesId=request.POST.get('counting_peoplesId') 
        try:
            user=UserBookDetails.objects.get(userId=userId)
            selectionType=BookNowSelectionsType.objects.get(id=timeSlotId)
            BookNowelectionsPeoples=BookNowSelectionsPeoples.objects.get(id=counting_peoplesId)
            print(selectionType.time_slot,"=======********* line no 2522222")
            user.bookNowSelectionsDate=date_global 
            user.bookNowSelectionsTypeId=timeSlotId 
            user.bookNowSelectionsTimeSlots=selectionType.time_slot
            user.bookNowSelectionsStatus=selectionType.status
            user.no_of_people=BookNowelectionsPeoples.no_of_people
            user.price=BookNowelectionsPeoples.price
            user.priceDescriptions=BookNowelectionsPeoples.priceDescriptions  
            user.save()
        except Exception as e:
            print(e,"=======********* line no 2522222")
        return JsonResponse({'message':'Data received successfully','bookNow':"context"})


data=list(BookNowScreenType.objects.filter(id=1).values())
print(data,"====line no 270000")
@csrf_exempt
def slotbooking_fetchUsers(request):
    final_data = []
    user=UserBookDetails.objects.all().values()
    for items in user:
        screenId=(int(items['bookNowScreenTypeId']))
        print(items['bookNowScreenTypeId'],type(items['bookNowScreenTypeId']),"====line no 276")
        user_register=Register.objects.filter(id=items['userId']).values()
       
        bookingScreen=list(BookNowScreenType.objects.filter(id=screenId).values()),
        # bookingScreen=list(BookNowScreenType.objects.filter(id=1).values()),
        print(bookingScreen,"=======********* line no 280")
        data={
            "userdata":list(user_register),
            "mainLocations":list(BookNowLocations.objects.filter(id=items['mainLocationsId']).values()),
            "bookNowScreenType":bookingScreen,
            "booking_details":{
                "date":items['bookNowSelectionsDate'],
                "timeslot":items['bookNowSelectionsTimeSlots'],
                "timeslot":items['bookNowSelectionsTimeSlots'],
                "status":items['bookNowSelectionsStatus'],
                "no_of_people":items['no_of_people'],
                "price":items['price'],
                "priceDescriptions":items['priceDescriptions']
                               } 
            
              }
        final_data.append(data)
    context = {"users": final_data}
    return JsonResponse({'message':'Update successful','context':context})
        # final_data.append(list(user_register))