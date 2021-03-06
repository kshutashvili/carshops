from django.contrib import admin

from content import models


class ProductImageAdmin(admin.ModelAdmin):
    fields = ['image_tag','image']
    readonly_fields = ['image_tag']


admin.site.register(models.MenuHeaderItem)
admin.site.register(models.MenuMainItem)
admin.site.register(models.DealerSection)
admin.site.register(models.SocialNetwork)
admin.site.register(models.LandingProductBlock)
admin.site.register(models.Blog)
admin.site.register(models.Information)
admin.site.register(models.Product)
admin.site.register(models.DiscountProduct)
admin.site.register(models.PopularProduct)
admin.site.register(models.ProductImage, ProductImageAdmin)
admin.site.register(models.Banner)
admin.site.register(models.TogetherCheaper)
admin.site.register(models.YearCar)
admin.site.register(models.StampCar)
admin.site.register(models.ModelCar)
admin.site.register(models.ChipBasket)
admin.site.register(models.BasketProduct)
admin.site.register(models.DeliveryData)
admin.site.register(models.Delivery)
admin.site.register(models.DeliveryWay)
admin.site.register(models.Order)
admin.site.register(models.PersonalAccount)
admin.site.register(models.Rait)
admin.site.register(models.InformationType)
admin.site.register(models.ExchangeRate)
admin.site.register(models.Comment)

