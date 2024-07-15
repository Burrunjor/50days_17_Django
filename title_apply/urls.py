from django.urls import path
from . import views

# now we are importing the views file into this.....and anothe r mdule
# this is connecting the index page to the home path "" (I think), and giving it a name
# so after that we need to go to the urls.py file within the project and add to the urlpatterns list
#path('', incldude('title_apply.urls')
# and you will also need to import include, you'll see it at the top, i haven't commnented on that page
# so then he basically just copied and pasted the flask html over thetop of the last one
# then he removed the {% with messages = get_flashed_messages.... line
# and he also removed the final {% endwith %}, this pairs with that
# then he added {% csrf_token %} just below the form tag
# now we go to views so that we can build the pick up on the data......

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about")       #views is the name of the function in views.py
]