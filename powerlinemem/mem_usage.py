import psutil

def _sizeof_fmt(num, suffix='B'):
    """
    Converts a byte value into a human-readable string.
    Stolen from http://stackoverflow.com/a/1094933/236130

    Args:
        num: The byte value
        suffix: The suffix appended to 'Mi', 'Gi' etc.

    Returns a string representation of the bytes.
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def _get_mem_used(mem_data, mem_type):
    mem_used = getattr(mem_data, mem_type, None)
    if mem_used is None:
        mem_used = mem_data.used
    return mem_used

def mem_usage(pl, format="%s/%s", mem_type='used'):
    mem_data = psutil.virtual_memory()
    mem_used = _get_mem_used(mem_data, mem_type)
    mem_percentage = (float(mem_used) / mem_data.total) * 100
    return [
        {
            'contents': format % (_sizeof_fmt(mem_used), _sizeof_fmt(mem_data.total)),
            'gradient_level': mem_percentage,
            'highlight_groups': ['mem_usage_gradient', 'mem_usage']
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
            'highlight_groups': ['mem_usage_gradient', 'mem_usage']
        }
    ]
