""" python dict tests """
from timeit import timeit


print("in check", timeit('''\
from typing import Any, Dict

def default_dict_with_in_check(init_kwargs: Dict[str, Any], widget: Any):
    """ ensure that the passed dict contains item and sub-item. """
    if 'tap_kwargs' not in init_kwargs:
        init_kwargs['tap_kwargs'] = dict()
    tap_kwargs = init_kwargs['tap_kwargs']

    if 'tap_widget' not in tap_kwargs:
        tap_kwargs['tap_widget'] = widget

    if 'popup_kwargs' not in tap_kwargs:
        tap_kwargs['popup_kwargs'] = dict()
    popup_kwargs = tap_kwargs['popup_kwargs']
    if 'parent' not in popup_kwargs:
        popup_kwargs['parent'] = widget

default_dict_with_in_check(dict(), object())
'''))

print("with get", timeit('''\
from typing import Any, Dict

def default_dict_with_get(init_kwargs: Dict[str, Any], widget: Any):
    """ ensure that the passed dict contains item and sub-item. """
    init_kwargs['tap_kwargs'] = tap_kwargs = init_kwargs.get('tap_kwargs', dict())
    tap_kwargs['tap_widget'] = tap_kwargs.get('tap_widget', widget)
    tap_kwargs['popup_kwargs'] = popup_kwargs = tap_kwargs.get('popup_kwargs', dict())
    popup_kwargs['parent'] = popup_kwargs.get('parent', widget)

default_dict_with_get(dict(), object())
'''))
