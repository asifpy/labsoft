from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from labsoft.lab.user.forms import UserForm
from labsoft.core.models import UserProfile

class UserListView(generic.ListView):
    template_name = 'lab/user/user_list.html'
    model = UserProfile
    context_object_name = 'users'

@login_required
def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            employee = form.cleaned_data['employee']
            new_user = User.objects.create_user(username, email, password)
            if employee:
                profile = UserProfile.objects.create(user=new_user, employee=employee)
            return HttpResponseRedirect(reverse('labsoft-lab-user-list'))
    else:
        form = UserForm()
    return render_to_response('lab/user/user_create.html',
        {'form': form},
        context_instance=RequestContext(request))
