# Watkins, jmw4dx
from django.http import HttpResponseRedirect, HttpResponse
from studentprofile.models import Student, Schedule, Course, Class
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render, reverse


def home(request):
    return HttpResponse("Hello, world! You're at the site.")

def submit_profile(request):
    # Fetch the current user
    user = User.objects.get(pk=request.user.id)
    
    # Error for if user name is null
    null_name_error = render(request, 'login/index.html', { # Redirects the user to the profile page again
        'error_message': "Username cannot be blank.", # Description for the error message displayed
    })


    if (request.POST['Name'] != " " and request.POST['Name'] !=""):
        # Create a Student Object that connects to that user
        student = Student(user = user, name = request.POST['Name'], year = request.POST['Year'],
                      major = request.POST['Major'], num = request.POST['NumClass'])
    
        # Save the Student Object we have just created
        student.save()

    else: 
        return null_name_error

    # Create an array equivalent to the size of the number of classes a user wants to input
    num_of_classes = request.POST['NumClass']
    num = []
    for i in range(0,int(num_of_classes)):
        num.append(1) # Note that it does not matter what is in the array
                      # it just simply needs to be the size of the number of classes

    # This creates a dict for the template to be able to access num
    context = {'num': num}

    # Redirect to the schedule making page
    return render(request, 'studentprofile/schedule.html', context)

class ProfileView(generic.TemplateView):
    model = Student
    template_name = 'studentprofile.html'

