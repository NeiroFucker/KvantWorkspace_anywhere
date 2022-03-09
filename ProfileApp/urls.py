from . import views
from django.urls import path

urlpatterns = [
    path('', views.SettingsPageTemplateView.as_view(), name='settings_page'),
    path('logout/', views.LogoutKvantUserView.as_view(), name='logout_user'),
    path('portfolio/', views.PortfolioPageListView.as_view(), name='portfolio_page'),
    path('statistics/', views.StaticsPageTemplateView.as_view(), name='statistics_page'),
]
