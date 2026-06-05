from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    roles=models.CharField(max_length=100) # user roles , client roles 
    address=models.CharField(max_length=100) # address
    contactNo=models.CharField(max_length=100) # user roles , client roles 
    profileImage=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.username} - {self.id}"

class ServiceType(models.Model):
    userId=models.CharField(max_length=100)
    serviceType=models.CharField(max_length=100)
    def __str__(self):
        return self.serviceType
    
class ServiceDetails(models.Model):
    userId=models.CharField(max_length=100)
    serviceTypeId=models.CharField(max_length=100)
    serviceMainCategories=models.CharField(max_length=100)
    serviceDescriptions=models.CharField(max_length=100)
    serviceAboutsUs=models.CharField(max_length=100)  
    def __str__(self):
        return self.serviceMainCategories
    
    
class ServiceImagesOrVideos(models.Model):
    userId=models.CharField(max_length=100)
    serviceTypeId=models.CharField(max_length=100)
    serviceMainImages=models.CharField(max_length=100) 
    serviceMainVideos=models.CharField(max_length=100) 
    def __str__(self):
        return self.userId
    
class BookNowLocations(models.Model):
    userId=models.CharField(max_length=100)
    mainLocations=models.CharField(max_length=100) 
    def __str__(self):
        return self.mainLocations
    
class BookNowScreenType(models.Model):
    userId=models.CharField(max_length=100)
    mainLocationsId=models.CharField(max_length=100) 
    image=models.CharField(max_length=100) 
    title=models.CharField(max_length=100) 
    priceTitle=models.CharField(max_length=100) 
    price=models.CharField(max_length=100) 
    priceDescriptions=models.CharField(max_length=100) 
    def __str__(self):
        return f"{self.title} - {self.id}"
    
    
class BookNowSelectionsType(models.Model):
    userId=models.CharField(max_length=100)
    bookNowScreenTypeId=models.CharField(max_length=100)  
    time_slot=models.CharField(max_length=100) 
    status=models.CharField(max_length=100) 
     
    def __str__(self):
        return self.time_slot

class BookNowSelectionsPeoples(models.Model):  
    no_of_people=models.CharField(max_length=100) 
    price=models.CharField(max_length=100) 
    priceDescriptions=models.CharField(max_length=100) 
    def __str__(self):
        return self.no_of_people
    
class BookNowOverviews(models.Model):
    userId=models.CharField(max_length=100)
    bookNowSelectionsTypeId=models.CharField(max_length=100) 
    booking_name=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100) 
    emailId=models.CharField(max_length=100)  
    def __str__(self):
        return self.booking_name

class BookNowOccasions(models.Model):
    userId=models.CharField(max_length=100)
    BookNowOverviewsId=models.CharField(max_length=100) 
    occasionTitle=models.CharField(max_length=100) 
    image=models.CharField(max_length=100)  
    occasionPersonName=models.CharField(max_length=100) 
    def __str__(self):
        return self.occasionTitle
    
class BookNowCakeType(models.Model):
    userId=models.CharField(max_length=100) 
    bookNowOccasionsId=models.CharField(max_length=100) 
    title=models.CharField(max_length=100) 
    price=models.CharField(max_length=100)  
    quantity=models.CharField(max_length=100) 
    def __str__(self):
        return self.title

class BookNowAddons(models.Model):
    userId=models.CharField(max_length=100)
    bookNowCakeTypeId=models.CharField(max_length=100) 
    image=models.CharField(max_length=100) 
    title=models.CharField(max_length=100) 
    price=models.CharField(max_length=100) 
    def __str__(self):
        return self.title

class UserBookDetails(models.Model):
    adminId=models.CharField(max_length=100)
    userId=models.CharField(max_length=100)
    mainLocationsId=models.CharField(max_length=100) 
    bookNowScreenTypeId=models.CharField(max_length=100)
    # ***** time slots start ***
    bookNowSelectionsTypeId=models.CharField(max_length=100) 
    bookNowSelectionsDate=models.CharField(max_length=100) 
    bookNowSelectionsTimeSlots=models.CharField(max_length=100) 
    bookNowSelectionsStatus=models.CharField(max_length=100) 
    no_of_people=models.CharField(max_length=100) 
    price=models.CharField(max_length=100) 
    priceDescriptions=models.CharField(max_length=100)
    # ***** time slots end *** 
    BookNowOverviewsId=models.CharField(max_length=100) 
    bookNowOccasionsId=models.CharField(max_length=100) 
    bookNowCakeTypeId=models.CharField(max_length=100)  
    def __str__(self):
        return self.userId
    
    
    
class BookNowTermsandConditions(models.Model):
    userId=models.CharField(max_length=100)
    bookNowAddonsId=models.CharField(max_length=100) 
    tc=models.CharField(max_length=100) 
    tcDescriptions=models.CharField(max_length=650) 
    tc1Title=models.CharField(max_length=100) 
    tc1Descriptions=models.CharField(max_length=800) 
    tc2Title=models.CharField(max_length=100) 
    tc2Descriptions=models.CharField(max_length=100) 
    tc3Title=models.CharField(max_length=100) 
    tc3Descriptions=models.CharField(max_length=800) 
    def __str__(self):
        return self.tc