from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from characters.views import characters_page
from votings import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/', characters_page),
    path('votings/', views.votings_page),
    path('votings/add_vote/<int:pk>/<str:character>', views.add_vote, name='add_vote'),
    path('api/', include('votings.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
