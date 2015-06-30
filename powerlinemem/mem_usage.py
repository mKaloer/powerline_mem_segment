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


def mem_usage(pl, format="%s/%s"):
    mem_data = psutil.virtual_memory()
    mem_percentage = (float(mem_data.used) / mem_data.total) * 100
    return [
        {
            'contents': format % (_sizeof_fmt(mem_data.used), _sizeof_fmt(mem_data.total)),
            'gradient_level': mem_percentage,
            'highlight_group': ['mem_usage_gradient', 'mem_usage']
        }
    ]

def mem_usage_percent(pl, format="%d%%"):
    mem_data = psutil.virtual_memory()
    mem_percentage = (float(mem_data.used) / mem_data.total) * 100
    return [
        {
            'contents': format % (mem_percentage, ),
            'gradient_level': mem_percentage,
            'highlight_group': ['mem_usage_gradient', 'mem_usage']
        }
    ]
