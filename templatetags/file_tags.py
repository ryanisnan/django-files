# Use the following line in your project's templates to include the usage of this app
#
# {% load file_tags %}
#
# What types of tags should we support
#
# {% file_link filename %}

from django import template
from files.models import File
from django.shortcuts import get_object_or_404, get_list_or_404

register = template.Library()

# Display a Link To A File
@register.inclusion_tag('filetags/file_link.html')
def file_link(filename):
	file = File.objects.get(name=filename)
	return { 'file' : file }