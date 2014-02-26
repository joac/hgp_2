from django import forms
from .models import AlbumLink, MediaResource
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.forms.util import flatatt

from django.forms.widgets import Select
from django.utils.encoding import force_text

class SelectWithSteroids(Select):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select{0}>', flatatt(final_attrs))]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
        output.append('<a href="#">Select image</a>')
        return mark_safe('\n'.join(output))

    def render_option(self, selected_choices, option_value, option_label):
        image_url = ''
        if option_value:
            try:
                resource = MediaResource.objects.get(pk=option_value)
                image_url = resource.photo.file.url
            except MediaResource.DoesNotExist:
                pass

        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html('<option value="{0}"{1} data-image-src="{3}">{2}</option>',
                           option_value,
                           selected_html,
                           force_text(option_label),
                           image_url
                        )

class AlbumLinkForm(forms.ModelForm):
    class Meta:
        model = AlbumLink
        widgets = {
            'resource': SelectWithSteroids
        }
