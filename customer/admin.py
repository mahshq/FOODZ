from django.contrib import admin

from customer.models import *


admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Offer)
admin.site.register(CartBill)
admin.site.register(Address)



