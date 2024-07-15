from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    current_titles = models.CharField(max_length=80)

    # this megthod allows you to define a string to be returned for the instance of the class
    # rather than the string talking about the object
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# narrative starts here?
# there is already a db.sqlite table created here, but no migrations, the command into the terminal now...
# python manage.py makemigrations
# that creates a middle man file between the models things and the database, they haven't been applied
# so to execute that we run another command....now
# python manage.py migrate
# so its a two step process, if you wanted to add new fields of data to your table you would run those steps again
# that app execution command again
# python manage.py runserver
# he also added to the INSTALLED_APPS list in the settings for the project, the name of the app title_apply
# think I missed that
# so whn we ran the py. start app, we got a views.py file in the app folder....so lets go to views


