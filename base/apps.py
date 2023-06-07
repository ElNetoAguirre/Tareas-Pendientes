"""
apps.py "base"
"""

from django.apps import AppConfig


class BaseConfig(AppConfig):
    """Función"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
