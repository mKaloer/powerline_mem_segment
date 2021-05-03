import psutil

def _sizeof_fmt(num, short=False, suffix='B'):
    """
    Converts a byte value into a human-readable string.
    Stolen from http://stackoverflow.com/a/1094933/236130

    Args:
        num: The byte value
        short: The short form of units
        suffix: The suffix appended to 'Mi', 'Gi' etc.

    Returns a string representation of the bytes.
    """
    if short:
        suffix = ''
    for unit in [('', ''), ('Ki', 'K'), ('Mi', 'M'), ('Gi', 'G'), ('Ti', 'T'), ('Pi', 'P'), ('Ei', 'E'), ('Zi', 'Z')]:
        if abs(num) < 1024.0:
            return ("%3.1f%s%s" if num else "%d%s%s") % (num, unit[int(short)], suffix)
        num /= 1024.0
    return ("%.1f%s%s" if num else "%d%s%s") % (num, ('Yi', 'Y')[int(short)], suffix)

def _get_mem_used(mem_data, mem_type):
    mem_used = getattr(mem_data, mem_type, None)
    if mem_used is None:
        mem_used = mem_data.used
    return mem_used

def mem_usage(pl, format="%s/%s", mem_type='used', short=False):
    mem_data = psutil.virtual_memory()
    mem_used = _get_mem_used(mem_data, mem_type)
    mem_percentage = (float(mem_used) / mem_data.total) * 100
    return [
        {
            'contents': format % (_sizeof_fmt(mem_used, short), _sizeof_fmt(mem_data.total, short)),
            'gradient_level': mem_percentage,
            'highlight_groups': ['mem_usage_gradient', 'mem_usage'],
            'divider_highlight_group': 'background:divider'
        }
    ]

def mem_usage_percent(pl, format="%d%%", mem_type='used'):
    mem_data = psutil.virtual_memory()
    mem_used = _get_mem_used(mem_data, mem_type)
    mem_percentage = (float(mem_used) / mem_data.total) * 100
    return [
        {
            'contents': format % (mem_percentage, ),
            'gradient_level': mem_percentage,
            'highlight_groups': ['mem_usage_gradient', 'mem_usage'],
            'divider_highlight_group': 'background:divider'
        }
    ]

def mem_swap(pl, format="%s/%s", mem_type='used', short=False):
    mem_data = psutil.swap_memory()
    mem_used = _get_mem_used(mem_data, mem_type)
    mem_percentage = ((float(mem_used) / mem_data.total) * 100) if mem_data.total else 0
    try:
        formatted = format % (_sizeof_fmt(mem_used, short), _sizeof_fmt(mem_data.total, short))
    except TypeError:
        formatted = format % _sizeof_fmt(mem_used, short)
    return [
        {
            'contents': formatted,
            'gradient_level': mem_percentage,
            'highlight_groups': ['mem_usage_gradient', 'mem_usage'],
            'divider_highlight_group': 'background:divider'
        }
    ]

def mem_swap_percent(pl, format="%d%%", mem_type='used'):
    mem_data = psutil.swap_memory()
    mem_used = _get_mem_used(mem_data, mem_type)
    mem_percentage = ((float(mem_used) / mem_data.total) * 100) if mem_data.total else 0
    return [
        {
            'contents': format % (mem_percentage, ),
            'gradient_level': mem_percentage,
            'highlight_groups': ['mem_usage_gradient', 'mem_usage'],
            'divider_highlight_group': 'background:divider'
        }
    ]
