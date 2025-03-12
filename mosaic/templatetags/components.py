from django import template
from web_components.loader import replace_components

register = template.Library()

@register.filter(name='render_components')
def render_components(value):
    """Render custom web components (PascalCase or x- style)."""
    return replace_components(value)
