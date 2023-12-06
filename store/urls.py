from django.urls import path

from . import views

# model => urls => views => templates (get the data from the model and display it in the template)

# namespace = "store"
# this is used to differentiate between the urls of different apps
app_name = "store"

urlpatterns = [
    path("", views.product_all, name="product_all"),
    # first slug refers to the variable, second slug refers to the datatype slug
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("search/<slug:category_slug>/", views.category_list, name="category_list"),
]
