from django import template

register = template.Library()

@register.filter
def initials(value):
    if not value:
        return ""
    words = value.split()
    if len(words) == 1:
        return words[0][0].upper()

    return "".join(word[0] for word in words).upper()