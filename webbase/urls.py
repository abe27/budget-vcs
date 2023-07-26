"""
URL configuration for webbase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

admin.site.site_header = 'Budget Admin Site'
admin.site.index_title = 'Web Management System'
admin.site.site_title = 'Web Management System'

urlpatterns = [
    # path("vcst/", include("budgetapp.urls"), name="budget_vcst"),
    # path("aaa/", include("budgetaaa.urls"), name="budget_aaa"),
    # path("bvs/", include("budgetbvs.urls"), name="budget_bvs"),
    # path("budget/", include("budgetapp.urls"), name="budget"),
    # path("accounts/", include("accounts.urls"), name="accounts"),
    path('', admin.site.urls),
    # path('', include('admin_volt.urls')),
    #  path('', include('jet.urls', 'jet')),  # Django JET URLS
]
