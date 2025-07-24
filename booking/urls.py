from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home,name='home'),
  path('register',views.register,name='register'),
  path('booking',views.booking,name='booking'),
  path('post',views.post,name='post'),
  path('profile',views.profile,name='profile'),
  path('add_category',views.add_category,name='add_category'),
  path('date',views.date,name='date'),
  path('occasion',views.occasion,name='occasion'),
  path('celebration',views.celebration,name='celebration'),
  path('business',views.business,name='business'),
  path('login',views.signin,name='login'),
  path('dashboard',views.dashboard,name='dashboard'),
  path('book/<int:user_id>',views.book,name='book'),
  path('view_restorent/<int:user_id>',views.view_restorent,name='view_restorent'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
