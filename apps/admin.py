from django.contrib import admin
from  .models import BookNowSelectionsPeoples, Register,BookNowLocations,BookNowScreenType,BookNowSelectionsType,BookNowOverviews,ServiceType,ServiceDetails,ServiceImagesOrVideos, UserBookDetails
# Register your models here.
admin.site.register(Register)
admin.site.register(BookNowLocations)
admin.site.register(BookNowScreenType)
admin.site.register(BookNowSelectionsType)
admin.site.register(BookNowOverviews)
admin.site.register(ServiceType)
admin.site.register(ServiceDetails)
admin.site.register(ServiceImagesOrVideos)
admin.site.register(UserBookDetails)
admin.site.register(BookNowSelectionsPeoples)