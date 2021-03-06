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
from django.urls import path, include
from pages.views import task_views, task_sorted_by_date, home_view, task_sorted_by_done, task_detail, \
    dynamic_view, logd_view, DevlopHome_views, SubTasksPerTask_view, SubTaskComment_view, MessagePage_view, \
    manager_views, ClientHome_views, work_done, manager_views_projects, manager_views_sprints, manager_task_view, \
    manager_subtask_view, logout_view, ClientSprint_view,Client_Task_per_Sprint
from django.contrib.auth.views import LoginView, LogoutView
from work.views import add_comment, update_comment, update_task, add_task, add_sprint, update_sprint, add_project, \
    add_sprint_task, add_subtask, update_subtask, subtask_delete, task_delete, delete_sprint, send_message, \
    delete_comment, delete_project, update_project, work_done_sub, read_bool, delete_sprint_task
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
'manager_views_sprints'
urlpatterns = [
    path('<int:id>', work_done, name='work_done'),
    path('', home_view, name='home_view'),

    path('manager/', manager_views, name='manager'),
    path('manager/<int:project_id>', manager_views_projects, name='manager_views_projects'),
    path('manager/sprint/<int:sprint_id>', manager_views_sprints, name='manager_views_sprints'),
    path('manager/sprint/<int:sprint_id>/<int:tid>/<int:need_to_delete>', manager_views_sprints,
         name='manager_views_sprints'),
    path('manager/task/<int:task_id>', manager_task_view, name='manager_task_view'),
    path('manager/sub_task/<int:sub_task_id>', manager_subtask_view, name='manager_subtask_view'),

    # ------------------------------------------------------
    # path('login/',LoginView.as_view(template_name='admin/login.html'),),
    #
    path('login/', LoginView.as_view(template_name='admin/login.html',), name='login'),
    path('logout/', logout_view, name='logout'),

    # ------------------------------------------------------

    path('tasks/', task_views, name='tasks_views'),
    path('admin/', admin.site.urls),
    path('sort_date/', task_sorted_by_date),
    path('sort_done/', task_sorted_by_done),
    path('tasks/<int:id>/', dynamic_view, name="task_detail"),

    path('accounts/profile/', logd_view, name='logd_view'),
    path('accounts/profile/client/<int:id>/', ClientSprint_view, name="ClientSprint_view"),
    path('accounts/profile/client/', ClientHome_views, name="ClientHome_views"),
    path('Devlop/', DevlopHome_views, name='DevlopHome_views'),
    path('Devlop/<int:id>/', SubTasksPerTask_view, name='SubTasksPerTask_view'),
    path('accounts/profile/client/<int:id>/<int:sprint_id>/', Client_Task_per_Sprint, name="Client_Task_per_Sprint"),

    path('comment/<int:pk>/new/', add_comment.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', update_comment.as_view(), name='comment-update'),

    path('subtask/<int:pk>/new/', add_subtask.as_view(), name='subtask-create'),
    path('subtask/<int:pk>/update/', update_subtask.as_view(), name='subtask-update'),
    path('subtask/<int:task_id>/<int:pk>/delete/', subtask_delete.as_view(), name='subtask-delete'),

    path('task/<int:pk>/<str:route>/new/', add_task.as_view(), name='task-create'),
    path('task/<int:pk>/update/', update_task.as_view(), name='task-update'),
    path('task/<str:route>/<int:r_id>/<int:pk>/delete/', task_delete.as_view(), name='task-delete'),

    path('sprint_task/<int:sprint>/<int:p>/new/', add_sprint_task.as_view(), name='sprint_task-create'),

    path('sprint/<int:pk>/new/', add_sprint.as_view(), name='sprint-create'),
    path('sprint/<int:pk>/update/', update_sprint.as_view(), name='sprint-update'),
    path('sprint/<int:project_id>/<int:pk>/delete/', delete_sprint.as_view(), name='sprint-delete'),

    path('project/new/', add_project.as_view(), name='project-create'),
    path('project/<int:pk>/update/', update_project.as_view(), name='project-update'),

    path('Devlop/Messages/', MessagePage_view, name='MessagePage_view'),
    path('send_message/<int:project_id>', send_message, name='send-message'),

    # ------------------------------------------------------------------------------

    path('comment/<int:subtask_id>/<int:pk>/delete/', delete_comment.as_view(), name='comment-delete'),
    path('project/<int:pk>/delete/', delete_project.as_view(), name='project-delete'),
    path('project/<int:pk>/update/', update_project.as_view(), name='project-update'),
    path('<int:my_id>/', work_done_sub, name='work_done_sub'),
    path('mmm/<int:my_id>/', read_bool, name='read-bool'),
    path('Devlop/Devlop/<int:my_id>/', SubTaskComment_view, name='SubTaskComment_view'),
    path('accounts/profile/Messages/', MessagePage_view, 'messages'),
    path('sprint_task/<int:pk>/<int:sprint>/<int:taskid>delete/', delete_sprint_task.as_view(), name='sprint_task-delete'),
]

urlpatterns += staticfiles_urlpatterns()
