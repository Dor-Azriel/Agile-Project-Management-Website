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
from pages.views import task_views, task_sorted_by_date, home_view, task_sorted_by_done, task_detail, \
    dynamic_view, logd_view, DevlopHome_views, SubTasksPerTask_view, SubTaskComment_view, MessagePage_view, \
    manager_views, ClientHome_views, work_done, manager_views_projects, manager_views_sprints, manager_task_view
from django.contrib.auth.views import LoginView
from work.views import add_comment, update_comment, update_task, add_task, add_sprint, update_sprint, add_project, \
    add_sprint_task, add_subtask, update_subtask, subtask_delete

'manager_views_sprints'
urlpatterns = [
    path('<int:id>', work_done,name='work_done'),
    path('', home_view,name='home_view'),
    path('manager/', manager_views, name='manager'),
    path('manager/<int:project_id>', manager_views_projects, name='manager_views_projects'),
    path('manager/sprint/<int:sprint_id>', manager_views_sprints, name='manager_views_sprints'),
    path('manager/task/<int:task_id>', manager_task_view, name='manager_task_view'),

    path('login/',LoginView.as_view(template_name='admin/login.html'),),
    path('tasks/', task_views,name='tasks_views'),
    path('admin/', admin.site.urls),
    path('sort_date/', task_sorted_by_date),
    path('sort_done/', task_sorted_by_done),
    path('tasks/<int:id>/', dynamic_view, name="task_detail"),

    path('accounts/profile/',logd_view),
    path('accounts/profile/client/',ClientHome_views,name="ClientHome_views"),
    path('accounts/profile/Messages/',MessagePage_view),
    path('Devlop/',DevlopHome_views,name='DevlopHome_views'),
    path('Devlop/<int:id>/',SubTasksPerTask_view,name='SubTasksPerTask_view'),
    path('Devlop/<int:id>/<int:my_id>/', SubTaskComment_view, name='SubTaskComment_view'),


    path('comment/<int:pk>/new/', add_comment.as_view() ,name='comment-create'),
    path('comment/<int:pk>/update/', update_comment.as_view() ,name='comment-update'),

    path('subtask/<int:pk>/new/', add_subtask.as_view(), name='subtask-create'),
    path('subtask/<int:pk>/update/', update_subtask.as_view(), name='subtask-update'),
    path('subtask/<int:task_id>/<int:pk>/delete/', subtask_delete.as_view(), name='subtask-delete'),


    path('task/<int:pk>/new/', add_task.as_view(), name='task-create'),
    path('task/<int:pk>/update/', update_task.as_view(), name='task-update'),


    path('sprint_task/<int:sprint>/<int:p>/new/', add_sprint_task.as_view(), name='sprint_task-create'),


    path('sprint/new/', add_sprint.as_view(), name='sprint-create'),
    path('sprint/<int:pk>/update/', update_sprint.as_view(), name='sprint-update'),


    path('project/new/', add_project.as_view(), name='project-create'),
    path('project/<int:pk>/update/', add_project.as_view(), name='project-update'),


    path('Devlop/Messages/', MessagePage_view, name='MessagePage_view'),
]
