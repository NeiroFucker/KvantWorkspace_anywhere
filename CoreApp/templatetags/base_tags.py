from datetime import datetime
from django import template


def get_file_extension(file):
    return file.file.name.split(".")[-1]


def get_file_name(file):
    return file.file.name.split("/")[-1]


def get_objects(model_object):
    return model_object.all()


def get_active_btn(active, aside):
    return "active" if aside == active else ""


def get_file_size(file):
    suffix_index = 0
    nbytes = file.file.size
    suffixes = ['B', 'kB', 'MB', 'GB', 'TB', 'PB']
    
    while nbytes >= 1024 and suffix_index < len(suffixes) - 1:
        nbytes /= 1024.
        suffix_index += 1
    size = ('%.2f' % nbytes).split(".00")[0]

    return f'{size} {suffixes[suffix_index]}'


def get_text(html):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)


register = template.Library()

register.filter('get_text', get_text)
register.filter('get_objects', get_objects)
register.filter('get_file_size', get_file_size)
register.filter('get_file_name', get_file_name)
register.filter('get_active_btn', get_active_btn)
register.filter('get_file_extension', get_file_extension)
