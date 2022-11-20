from django.urls import path
from main.view import UpdateResumeView, AddEducationView, CreateResumeView,UpdateResumeView, \
    ResumesIndexView, ResumeUpdateDateView, ResumePublicView, EditEducationView, DeleteEducationView, \
    AddExperienceView, EditExperienceView, DeleteExperienceView



urlpatterns = [
    path('resume/create/', CreateResumeView.as_view(), name='create_resume'),
    path('resume/<int:pk>/edit', UpdateResumeView.as_view(), name='edit_resume'),
    path('resume/<int:pk>/update/date/', ResumeUpdateDateView.as_view(), name='resume_update_date'),
    path('resume/<int:pk>/public/', ResumePublicView.as_view(), name='resume_public'),
    path('resume/<int:pk>/add/education/', AddEducationView.as_view(), name='add_education'),
    path('resume/<int:pk>/education/edit', EditEducationView.as_view(), name='edit_education'),
    path('resume/<int:pk>/education/delete', DeleteEducationView.as_view(), name='delete_education'),
    path('resume/<int:pk>/add/experience/', AddExperienceView.as_view(), name='add_experience'),
    path('resume/<int:pk>/experience/edit', EditExperienceView.as_view(), name='edit_experience'),
    path('resume/<int:pk>/experience/delete', DeleteExperienceView.as_view(), name='delete_experience'),
]