"""jobproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from jobapp import views
urlpatterns = [

    path('',views.home),

    path('login/',views.joblogin),
    path('jobpost/',views.post_job),
    path('register/',views.regis),
    path('success/',views.emailsuccess),
    path('verify/',views.emailverify),
    path('verify/<auth_token>',views.verify),
    path('error/',views.error),
    path('jobpro/',views.jobpro),
    path('edit_comp/<str:mail>/<str:token>',views.edit_comp),
    path('regcomp/',views.regcomp),
    path('userregister/',views.userregister),
    path('userlogin/',views.userlogin),
    path('jobshow/',views.jobshow),
    path('jobshow1/<int:id>',views.jobshow1),
    path('applyjob/',views.apply_job),
    path('user_profile/',views.user_profile),
    path('view_profile/',views.view_profile),
    path('useredit/<int:id>',views.user_edit)

]
