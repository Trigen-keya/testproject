from django.urls import path
from .views import signupview, loginview, listview, detailview, creatclass, logoutview, evaluationview, passwordview

urlpatterns = [
   path('signup/', signupview,name='signup'),
   path('login/',loginview,name='login'),
   path('list/',listview,name='list'),
   path('detail/<int:pk>/',detailview,name='detail'),
   path('create/',creatclass.as_view(),name='create'),
   path('logout/',logoutview.as_view(),name='logout'),
   path('evaluation/<int:pk>/',evaluationview,name='evaluation'),
   path('passwordchange/',passwordview.as_view(),name='passwordchange')

]
