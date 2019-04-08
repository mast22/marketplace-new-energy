from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('new_work/', views.new_work, name='new_work'),
    path('<int:item_id>/offer/<int:offer_id>', views.offer_details_view, name='offer_details'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:item_id>/new_offer/', views.new_offer, name='new_offer'),

    path('work_done_custome/<int:item_id>/<int:offer_id>/', views.work_done_custome, name='work_done_custome'),
    path('work_done_contractor/<int:item_id>/<int:offer_id>/', views.work_done_contractor, name='work_done_contractor'),

    path('review/<int:item_id>/<int:offer_id>/', views.review, name='review'),
    path('contractor_review/<int:item_id>/<int:offer_id>/', views.contractor_review, name='contractor_review'),

    path('contractors_raiting/', views.ContractorsRaiting.as_view(), name='contractors_raiting'),
    path('choose_contractor/<int:item_id>/<int:offer_id>/', views.choose_contractor, name='choose_contractor'),

    path('uncontr/', views.uncontr, name='uncontr'),
    # load_contract
    path('load_contract/', views.load_contract, name='load_contract'),

    path('index_filter/', views.index_filter, name='index_filter'),
]
