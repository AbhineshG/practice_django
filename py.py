admin=[{"userId":1,  
"date":"03-06-2026", 
"time_slot":"06:00 pm - 09:00 pm",
"status":"available" ,
"no_of_people":4, 
"price":1800 ,
"priceDescriptions":"some description about the price and the booking details"},
    {"userId":2,  
"date":"04-06-2026", 
"time_slot":"09:00 am - 11:00 am",
"status":"available" ,
"no_of_people":4, 
"price":1800 ,
"priceDescriptions":"some description about the price and the booking details"},
    {"userId":3,  
"date":"04-06-2026", 
"time_slot":"12:00 pm - 03:00 pm",
"status":"available" ,
"no_of_people":4, 
"price":1800 ,
"priceDescriptions":"some description about the price and the booking details"},
    
    {"userId":4,  
"date":"04-06-2026", 
"time_slot":"04:00 pm - 06:00 pm",
"status":"available" ,
"no_of_people":4, 
"price":1800 ,
"priceDescriptions":"some description about the price and the booking details"}
      ]

users=[{"userId":1,  
"date":"03-06-2026", 
"time_slot":"06:00 pm - 09:00 pm",
"status":"available" ,
"no_of_people":4, 
"price":1800 ,
"priceDescriptions":"some description about the price and the booking details"},
      {"userId":1,  
"date":"03-06-2026", 
"time_slot":"04:00 pm - 06:00 pm",
"status":"available" ,
"no_of_people":4, 
"price":1800 ,
"priceDescriptions":"some description about the price and the booking details"}
      ]

for items in admin:
    for user in users:
        if items["time_slot"] == user["time_slot"]:
            print(user["date"]," ",user["time_slot"]," is unavailable for booking")
            items["status"] = "unavailable"
            break
    else:
        print(items["date"]," ",items["time_slot"]," is available for booking")
        
         
print(admin,"====line no 322222")




 