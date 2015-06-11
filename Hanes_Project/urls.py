from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


from django.contrib import admin
from Hanes_Project import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hanes_project_app.views.index_view', name='index_view'),
    url(r'^index/', 'hanes_project_app.views.index_view', name='index_view'),
    url(r'^post-data/', 'hanes_project_app.views.post_query_view', name='post_query_view'),
    url(r'^sub-category-of-menu-category/', 'hanes_project_app.views.sub_category_of_menu_category', name='sub-category-of-menu-category'),
    url(r'^all-post/(?P<menu_category>.*)', 'hanes_project_app.views.selected_menu_all_post', name='menu-all-post'),
    url(r'^capcha-match/', 'hanes_project_app.views.capcha_varification_view', name='capcha-match'),
    url(r'^filterby-region-or-category/', 'hanes_project_app.views.region_or_category_filter_view', name='filterby-region-or-category'),
    url(r'^post-by-title/(?P<post_title>.*)', 'hanes_project_app.views.post_by_menu_post_title', name='post_by_menu_post_title'),
    url(r'^all-post-by-search', 'hanes_project_app.views.all_post_by_search', name='all-post-by-search'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^add-advertise/$', 'hanes_project_app.views.add_advertise', name="add-advertise"),
    url(r'^imagefit/', include('imagefit.urls')),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
