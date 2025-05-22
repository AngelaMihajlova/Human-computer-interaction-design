from django.contrib import admin
from Travel_Application.models import Travel, TouristGuide
from django.db.models import Count

class TravelAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj = None):
        return obj and obj.touristGuide.user==request.user

    # def has_add_permission(self, request):
    #     return TouristGuide.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        touristGuide = TouristGuide.objects.filter(user=request.user).first()
        touristGuide_travels = Travel.objects.filter(touristGuide=touristGuide).all()

        if not change and touristGuide_travels.count() == 5:
            return

        sum = 0
        for travel in touristGuide_travels:
            sum += travel.price

        old_travel_obj = touristGuide_travels.filter(id=obj.id).first()

        if not change and sum+obj.price > 50000:
            return

        if change and sum+obj.price-old_travel_obj.price > 50000:
            return

        if Travel.objects.filter(place=obj.place).exists():
            return

        super(TravelAdmin, self).save_model(request, obj, form, change)




class TouristGuideAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TouristGuideAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(touristGuide_travels=Count('guides')).filter(touristGuide_travels__lt=3)
        return qs

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser


# Register your models here.
admin.site.register(Travel, TravelAdmin)
admin.site.register(TouristGuide , TouristGuideAdmin)