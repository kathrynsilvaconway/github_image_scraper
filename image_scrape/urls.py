from django.urls import path, include

urlpatterns = [
    path('', include('scrape_app.urls')),
]
