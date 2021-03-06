from django.conf.urls import patterns, url

from data import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),


    #url(r'^(?P<id>\d+)/user_table/$', views.user_table, name='user_table'),

    #### http://meghdeep.pythonanywhere.com/data/name_lookup/<name_in>/<pass_in>/
    ###url(r'^auth_lookup/(?P<name_in>\w+)/(?P<pass_in>\d+)/$', views.auth_lookup, name='auth_lookup'),

    # http://meghdeep.pythonanywhere.com/data/user_table/<name_id_in>/
    url(r'^user_table/(?P<name_id_in>\d+)/$', views.user_table, name='user_table'),
    # Sends back - JSON containing user_id, user_name, phone_number, password, email

    # http://meghdeep.pythonanywhere.com/data/test/id/latitude/longitude
    #url(r'^test/$', views.test, name='test'),

    url(r'^user_table_complete/(?P<password>\w+)/$', views.user_table_complete, name='user_table_complete' ),

    # http://meghdeep.pythonanywhere.com/data/distance/<id>/<latitude>/<longitude>/
    url(r'^distance/(?P<id>\d+)/(?P<latitude>[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?))/(?P<longitude>[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?))/$', views.distance, name='distance'),

    # http://meghdeep.pythonanywhere.com/data/shop_list/<station_id_in>/
    url(r'^shop_list/(?P<station_id_in>\d+)/$', views.shop_list, name='shop_list'),

    # http://meghdeep.pythonanywhere.com/data/station_add/<station_name_in>/
    url(r'^station_add/(?P<station_name_in>\w+)/$', views.station_add, name='station_add'),

    # http://meghdeep.pythonanywhere.com/data/shop_menu/<vendor_id_in>/
    url(r'^shop_menu/(?P<vendor_id_in>\d+)/$', views.shop_menu, name='shop_menu'),

    # http://meghdeep.pythonanywhere.com/data/enter_food_order/<pnr_in>/<vendor_id_in>/<user_id_in>/<order_in>/
    url(r'^enter_food_order/(?P<pnr_in>\d+)/(?P<vendor_id_in>\d+)/(?P<user_id_in>\d+)/(?P<order_in>\d+)/$', views.enter_food_order, name='enter_food_order'),

    # http://meghdeep.pythonanywhere.com/data/create_new_user/<name_in>/<phone_number_in>/<user_password_in>/<email_in>/
    url(r'^create_new_user/(?P<name_in>\w+)/(?P<phone_number_in>\d+)/(?P<user_password_in>\w+)/(?P<email_in>([\w.-]+)@([\w.-]+))/$', views.create_new_user, name='create_new_user'),
    #url(r'^create_new_user/(?P<name_in>\w+)/(?P<phone_number_in>\d+)/(?P<user_password_in>\w+)/(?P<email_in>\w+)/$', views.create_new_user, name='create_new_user'),
    # Sends back - 200 OK

    # http://meghdeep.pythonanywhere.com/data/what_was_ordered/<order_in>/
    url(r'^what_was_ordered/(?P<order_in>\d+)/$', views.what_was_ordered, name='what_was_ordered'),

    # http://meghdeep.pythonanywhere.com/data/station_list/<pnr>/
    url(r'^station_list/(?P<pnr>\d+)/$', views.station_list, name='station_list'),

    # http://meghdeep.pythonanywhere.com/data/status/<pnr>/<station_name_in>/
    url(r'^status/(?P<pnr>\d+)/(?P<station_name_in>\w+)/$', views.status, name='status'),

    # http://meghdeep.pythonanywhere.com/data/scrape_run/<pnr>/
    url(r'^scrape_run/(?P<pnr>\d+)/$', views.scrape_run, name='scrape_run'),
    # To make the Scraper Scrape for a PNR only

    # http://meghdeep.pythonanywhere.com/data/displayer/
    url(r'^displayer/$', views.displayer, name='displayer'),
    # To make the Views Read out the Intermediate Storage File only
)
