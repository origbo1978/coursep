
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),
    path('signup',views.signup_view,name='signup'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('courses',views.courses,name='courses'),
    path('course_description/<int:course_id>/',views.course_description,name='course_description'),
    path('profile',views.profile_view,name='profile_view'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
]
