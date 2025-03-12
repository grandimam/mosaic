import re
from django.template.loaders.filesystem import Loader as FileSystemLoader
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

COMPONENT_REGEX = re.compile(r'<(?:x-)?([A-Z][\w-]*)\s*([^>/]*)\s*(/?)>(.*?)</\1>?', re.DOTALL)


def parse_attributes(attr_string):
    """Convert HTML attributes into a dictionary and transform camelCase to snake_case."""
    attrs = {}
    matches = re.findall(r'([\w-]+)="(.*?)"', attr_string)
    for key, value in matches:
        key = key.replace("-", "_")  # Convert kebab-case to snake_case
        attrs[key] = value
    return attrs


def replace_components(content):
    """Replace <Button> and <x-button> with actual Django component templates."""

    def render_component(match):
        component_name = match.group(1)  # e.g., "Button"
        attributes = match.group(2)  # e.g., ' text="Click Me"'
        is_self_closing = match.group(3) == "/"  # Detect self-closing tag
        slot_content = match.group(4) if not is_self_closing else ""

        attrs_dict = parse_attributes(attributes)
        attrs_dict["content"] = slot_content.strip()

        # Convert PascalCase to snake_case for template lookup (Button → button)
        component_template = f"components/{component_name.lower()}.html"
        return render_to_string(component_template, attrs_dict)

    return mark_safe(COMPONENT_REGEX.sub(render_component, content))


class ComponentLoader(FileSystemLoader):
    """Custom Django Template Loader to process <Button> components."""

    def get_contents(self, origin):
        """Override the default get_contents method to replace components."""
        content = super().get_contents(origin)  # Load original template
        return replace_components(content)  # Replace components dynamically
