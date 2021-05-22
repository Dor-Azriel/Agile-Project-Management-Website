"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from pages.views import task_views,add_comment, task_sorted_by_date, home_view, task_sorted_by_done, task_detail,dynamic_view,logd_view,DevlopHome_views,SubTasksPerTask_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home_view,name='home_view'),
    path('create_sub_task', create_sub_task, name='create_sub_task'),
    path('login/',LoginView.as_view(template_name='admin/login.html')),
    path('tasks/', task_views,name='tasks_views'),
    path('admin/', admin.site.urls),
    path('sort_date/', task_sorted_by_date),
    path('sort_done/', task_sorted_by_done),
    path('tasks/<int:id>/', dynamic_view, name="task_detail"),
    path('add-commento<int:id>', add_comment, name="add_comment"),
    path('accounts/profile/',logd_view),
    path('Devlop/',DevlopHome_views,name='DevlopHome_views'),
    path('Devlop/<int:id>/',SubTasksPerTask_view,name='SubTasksPerTask_view'),
   # path('', home_view),
   # path('accounts/', include('django.contrib.auth.urls')),
    # url(r'^(?P<id>[-\w]+)/comment/$', add_comment, name="add_comment"),
    # re_path(r'^(?P<id>[-\w]+)/$', dynamic_view, name='task_detail'),

    # url
]
