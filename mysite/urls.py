from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
3333333333333333333333333333
#from django.conf.urls import *
#from addr_book.views import hello, current_time
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_book/','addr_book.views.add_book'),
    url(r'^add_author/','addr_book.views.add_author'),
    url(r'^all_book/','addr_book.views.all_book'),
    url(r'^delete/','addr_book.views.delete'),
    url(r'^update/','addr_book.views.update'),
    url(r'^book_detail/','addr_book.views.book_detail'),
    url(r'^search/','addr_book.views.search'), 
    url(r'^login/','addr_book.views.login_ok'),
    url(r'^Error/','addr_book.views.Error'),
    url(r'^logout/','addr_book.views.logout_ok'),
    url(r'^creat_user/','addr_book.views.creat_user'),
    url(r'^creat_user_ok/','addr_book.views.creat_user_ok'),
    url(r'^set_password/','addr_book.views.set_password'),
    )
