from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from agenda import views as agenda_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas públicas para agendar
    path('', agenda_views.index, name='home'),  # 👈 CAMBIADO a 'home'
    path('barrasa/', agenda_views.barrasa, name='barrasa'),
    path('beauty/', agenda_views.beauty, name='beauty'),
    path('gracias/', agenda_views.gracias, name='gracias'),

    # Login y Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    # Vista protegida
    path('citas/', agenda_views.lista_citas, name='lista_citas'),
    path('eliminar-cita/<int:cita_id>/', agenda_views.eliminar_cita, name='eliminar_cita'),
    path('galeria/', agenda_views.galeria, name='galeria'),
]
