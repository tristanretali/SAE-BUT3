from django.contrib.auth.models import Group
from wagtail import hooks
from django.urls import reverse
from wagtail.admin.menu import MenuItem
from django.shortcuts import redirect

website = "http://localhost:3000"
    
@hooks.register('after_create_user')
def add_user_to_group(request, user):
    if user:
       group = Group.objects.get_or_create(name='Editors')
       user.groups.add(group)
       
@hooks.register('register_admin_menu_item')
def register_frank_menu_item():
  return MenuItem('Go back to recipy', website, icon_name='globe', order=0)

@hooks.register('after_create_snippet')
def redirect_to_website(request, snippet):
	return redirect(website)