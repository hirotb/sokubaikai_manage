"""sokubaikai_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'sokubaikai'
urlpatterns = [
    # path('', views.top(), name='home'),
    # path('', views.top(), name='home'),
    # path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    # 以下のフォルダはアプリケーショーンに飛ぶ
    # path('', views.BlogDetailView.as_view(), name='sokubaikai'),
    path('', views.IndexView.as_view(), name='home'),
    path('sokubaikai-list/', views.SokubaikaiListView.as_view(), name='list'),
    # path('sokubaikai-detail/', views.SokubaikaiDetailView.as_view(), name='detail2'),
    path('sokubaikai-detail/<int:pk>/', views.SokubaikaiDetailView.as_view(), name='detail'),
    path('sokubaikai-detail/new/', views.SokubaikaiCreateView.as_view(), name='new'),
    # サンプル
    path('aaa/', views.MyView.as_view(), name='home2'),

]
