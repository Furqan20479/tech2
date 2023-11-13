
from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "Buy & Sell Admin"
admin.site.site_title = "Buy & Sell Admin Portal"
admin.site.index_title = "Wellcome To Buy & Sell"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('techtwo.urls'))
    

]
