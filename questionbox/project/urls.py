"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from questions import views
from templates import questions, answers

#IT HAS TO TAKE A REQUEST AND RETURN A RESPONSE! (AS_VIEW())

urlpatterns = [
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls), 
    path('questions/view_question<int:pk>/', views.view_question.as_view(), name="view_question"),
    path('list_question/', views.list_question.as_view(), name="list_question"),
    path('questions/create_question/', views.create_question.as_view(), name="create_question"),
    path('questions/edit_question<int:pk>/', views.edit_question.as_view(), name="edit_question.html"),
    path('', views.HomeView.as_view(), name="home"),
    
    #path('templates/')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
