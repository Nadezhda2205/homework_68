from django.urls import path
from main.view import UpdateResumeView, AddEducationView, CreateResumeView,UpdateResumeView, \
    ResumesIndexView, ResumeUpdateDateView, ResumePublicView, EditEducationView, DeleteEducationView, \
    AddExperienceView, EditExperienceView, DeleteExperienceView, DeleteResumeView, ResumeListView, ResumeDetailView



urlpatterns = [
    path('resume/create/', CreateResumeView.as_view(), name='create_resume'),
    path('resume/<int:pk>/edit', UpdateResumeView.as_view(), name='edit_resume'),
    path('resume/<int:pk>/delete', DeleteResumeView.as_view(), name='delete_resume'),
    path('resume/<int:pk>/update/date/', ResumeUpdateDateView.as_view(), name='resume_update_date'),
    path('resume/<int:pk>/public/', ResumePublicView.as_view(), name='resume_public'),
    path('resume/<int:pk>/add/education/', AddEducationView.as_view(), name='add_education'),
    path('resume/<int:pk>/education/edit', EditEducationView.as_view(), name='edit_education'),
    path('resume/<int:pk>/education/delete', DeleteEducationView.as_view(), name='delete_education'),
    path('resume/<int:pk>/add/experience/', AddExperienceView.as_view(), name='add_experience'),
    path('resume/<int:pk>/experience/edit', EditExperienceView.as_view(), name='edit_experience'),
    path('resume/<int:pk>/experience/delete', DeleteExperienceView.as_view(), name='delete_experience'),
    path('resume/<int:pk>/detail/', ResumeDetailView.as_view(), name='detail_resume'),
    path('resume/list', ResumeListView.as_view(), name='resume_list'),
]