import psutil
from powerline import Segment, with_docstring


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
            return "%3.1f%s%s" % (num, unit[int(short)], suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, ('Yi', 'Y')[int(short)], suffix)


class MemUsageSegment(Segment):

    def _get_mem_data(self):
        return psutil.virtual_memory()

    def _get_mem_type(self, mem_data, mem_type):
        mem_used = getattr(mem_data, mem_type, None)
        if mem_used is None:
            mem_used = mem_data.used
        return mem_used

    def _get_segment(self, content, gradient_level, highlight_groups=None,
                     divider_highlight_group="background:divider"):
        if highlight_groups is None:
            highlight_groups = ['mem_usage_gradient', 'mem_usage']
        return [
            {
                'contents': content,
                'gradient_level': gradient_level,
                'highlight_groups': highlight_groups,
                'divider_highlight_group': divider_highlight_group
            }
        ]

    def mem_usage(self, pl, mem_type='used', short=False, fmt='%s/%s'):
        mem_data = self._get_mem_data()
        mem_used = self._get_mem_type(mem_data, mem_type)
        mem_percentage = (float(mem_used) / mem_data.total) * 100
        return self._get_segment(fmt % (_sizeof_fmt(mem_used, short), _sizeof_fmt(mem_data.total, short)),
                                 mem_percentage)

    def mem_usage_percent(self, pl, mem_type='used', fmt="%d%%"):
        mem_data = self._get_mem_data()
        mem_used = self._get_mem_type(mem_data, mem_type)
        mem_percentage = (float(mem_used) / mem_data.total) * 100
        return self._get_segment(fmt % (mem_percentage,), mem_percentage)

    def __call__(self, pl, format_type='used_total', mem_type='used', short=False):
        mem_usage_function_mapping = {
            "used_total": self.mem_usage,
            "percentage": self.mem_usage_percent
        }
        return mem_usage_function_mapping.get(format_type)(pl, mem_type, short)


mem_usage = with_docstring(MemUsageSegment(), """
Return the memory usage of the system.

It can return the memory usage in two ways, either as a fraction in the form of mem_used/mem_total or as a percentage 
{mem_used}%.

:param str format_type:
    Mention the format_type to be used to show the memory usage of the system. Currently, only two format types are 
    supported - `used_total`, `percentage`.

:param str mem_type:
    Mention the type of memory that is to be evaluated. Valid options are `used`, `active`, `inactive`, `available`, 
    `buffers`, `cached`, `shared` and `slab`. Default value is `used`. If any invalid value is used, it defaults to 
    `used`.

:param bool short:
    Show the MBs, KBs, GBs as M, K, G, etc. A value of `True` shows the short version else shows the default version.

Divider highlight group used: ``background:divider``.
Highlight groups used: ``mem_usage``, ``mem_usage_gradient``.
""")
