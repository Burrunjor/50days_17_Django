from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "current_titles")
    ordering = ("-first_name", ) #this has to be a tuple with the comma. this orders in reverse
    readonly_fields = ("current_titles", )


admin.site.register(Form, FormAdmin)

# we need to go to the terminal now and put in
# python manage.py createsuperuser (put in your creds that you want)
# python manage.py runserver
# then you can see we are inherrting from admin.ModelAdmin to add new functionality to the form

# so thats that done, ill keep the comments here, we are goign to create the menu bar
# we duplciate the index.html and call it base and add anothef ile
# now we are making changes to the index.html, so I have saved the original so you can see it
# but we are splitting that form up into uniwque sheets
# we add the jinga code there into block (in index), we add more jinga 2 at the top and end the block at the end
# we do the latter two on about as well
# then we create the about function in views,py
# and then we add the about list item to urls in the project (not the site)