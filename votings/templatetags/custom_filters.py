from django.template.defaulttags import register


@register.filter
def get_item(d, key_name):
    key_name = str(key_name)
    return d.get(key_name)
