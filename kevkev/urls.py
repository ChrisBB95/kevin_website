from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# app urls
from home.views import home_view
from gallery.views import gallery_view
from shop.views import shop_view, add_to_cart, view_cart, remove_from_cart, add_one, sub_one

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('gallery/', gallery_view, name='gallery'),
    path('shop/', shop_view, name='shop'),
    path('shop/add/<int:item_id>/', add_to_cart, name='add'),
    path('shop/cart/remove/<int:item_id>/', remove_from_cart, name='remove'),
    path('shop/cart/add/<int:item_id>/', add_one, name='addone'),
    path('shop/cart/sub/<int:item_id>/', sub_one, name='sub'),
    path('shop/cart/', view_cart, name='cart'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATICFILES_DIRS[0])
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
