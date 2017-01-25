urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^rango/',include('rango.urls')),
    url(r'^admin/', admin.site.urls),
]