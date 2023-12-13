from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat
from .forms import FeedingForm

# Add this cats list below the imports
# Sample data for this lesson since we don't have a model yet! Just fake data so we can learn how the render method works!
# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# Get request - Render a template
# templates/<name_of_app>/<model_name>_form.html
# templates/main_app/cat_form.html
# Post request - Receive the contents of the form and add those to the database
class CatCreate(CreateView):
    model = Cat
    # template_name = 'cats/cat_form.html' # <- if you want to override the template naming convention
    fields = '__all__'
    # Alternate approach:
    # fields = ['breed', 'name'] # Select certain fields from the keys on the model to include on for and create
    # If we want to redirect to the detail page:
    # success_url = '/cats/{cat_id}' # This string is special from Django
    # If we want to redirect to the index page: 
    # success_url = '/cats'
    # OR, we can redirect on the model
    # Note: the success_url in the view function takes precedence over the get_absoulte_url on the model. The nice thing about putting it on the model instead is that it applies to both create and update operations (less code!)

# Get request - Render a template
# templates/<name_of_app>/<model_name>_form.html
# templates/main_app/cat_form.html
class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age'] # Will allow updating of all attributes except name
    # The redirect is happening in the get_absolute_url method in the models to go to the detail page

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats' # Redirect to the index page

# Create your views here.
def home(request):
    # Include a .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    # The variable in the template is the key in the dictionary
    # In this case, 'cats' is the key, so the variable in cats/index.html is cats
    cats = Cat.objects.all() # <- Going to the database, getting all the cats and storing it in a variable called cats
    # In Python, it waits until the above line of code finishes before running the next line of code... no need for async/await!
    return render(request, 'cats/index.html', {'cats': cats})

# path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
# cat_id comes from the path in the urls
#  The argument in the function must match the param name
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)

    # Generate an instance of your form on every request
    # feeding_form is an instance
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})

# param cat_id must be matching with the argument of the function
def add_feeding(request, cat_id):
    # create a modelForm instance using the data from the form, in Django: request.POST <--- same as req.body in Express
    form = FeedingForm(request.POST)
    # Then we check if the form is valid (matches the model)
    if form.is_valid():
        # Assign the cat_id to the form
        new_feeding = form.save(commit=False) # Creates an instance (a row to be entered into the table)
        new_feeding.cat_id = cat_id
        # Save that new row (new_feeding) to the database
        new_feeding.save()
        # The row has not ben entered into the table

    # Don't forget to import redirect at the top
    # Use redirect in the view file; use reverse in the model file
    return redirect('detail', cat_id=cat_id)