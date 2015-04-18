from django.conf.urls import patterns, url

from data import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),


    #url(r'^(?P<id>\d+)/user_table/$', views.user_table, name='user_table'),

    # http://meghdeep.pythonanywhere.com/data/user_table/<name_in>/
    url(r'^user_table/(?P<name_in>\d+)/$', views.user_table, name='user_table'),

    # http://meghdeep.pythonanywhere.com/data/test/id/latitude/longitude
    #url(r'^test/$', views.test, name='test'),

    # http://meghdeep.pythonanywhere.com/data/distance/<id>/<latitude>/<longitude>/
    url(r'^distance/(?P<id>\d+)/(?P<latitude>[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?))/(?P<longitude>[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?))/$', views.distance, name='distance'),

    # http://meghdeep.pythonanywhere.com/data/shop_list/<station_id_in>/
    url(r'^shop_list/(?P<station_id_in>\d+)/$', views.shop_list, name='shop_list'),

    # http://meghdeep.pythonanywhere.com/data/shop_menu/<vendor_id_in>/
    url(r'^shop_menu/(?P<vendor_id_in>\d+)/$', views.shop_menu, name='shop_menu'),

    # http://meghdeep.pythonanywhere.com/data/enter_food_order/<pnr_in>/<vendor_id_in>/<user_id_in>/<order_in>/
    url(r'^enter_food_order/(?P<pnr_in>\d+)/(?P<vendor_id_in>\d+)/(?P<user_id_in>\d+)/(?P<order_in>\d+)/$', views.enter_food_order, name='enter_food_order'),

    # http://meghdeep.pythonanywhere.com/data/create_new_user/<name_in>/<phone_number_in>/<user_password_in>/<email_in>/
    url(r'^create_new_user/(?P<name_in>\w+)/(?P<phone_number_in>\d+)/(?P<user_password_in>\w+)/(?P<email_in>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)/$', views.create_new_user, name='create_new_user'),

    # http://meghdeep.pythonanywhere.com/data/what_was_ordered/<order_in>/
    url(r'^what_was_ordered/(?P<order_in>\d+)/$', views.what_was_ordered, name='what_was_ordered'),

    # http://meghdeep.pythonanywhere.com/data/station_lister/<pnr_in>/
    url(r'^station_lister/(?P<pnr_in>\d+)/$', views.station_lister, name='station_lister'),

)
