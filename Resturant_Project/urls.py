
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name="Home"),
    path('book_table', BookTableView, name="Book_Table"), # slash thapa
    path('menu/', MenuView, name="Menu"),                 # slash thapa
    path('about', AboutView, name="About"),               # slash thapa
    path('feedback', FeedbackView, name="Feedback"),     # slash thapa
]
if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
