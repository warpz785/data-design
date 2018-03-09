from django.urls import path, include

from . import views

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name = 'blog'),
         ]