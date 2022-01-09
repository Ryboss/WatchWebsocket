"""
ASGI config for websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# Импортировать модуль os
import os
# Импортировать get_asgi_application для обработки протокола http
from django.core.asgi import get_asgi_application
# Import ProtocolTypeRouter и URLRouter для установки маршрутизации веб-сокетов
from channels.routing import ProtocolTypeRouter, URLRouter
# Import AuthMiddlewareStack для обработки веб-сокета
from channels.auth import  AuthMiddlewareStack
# Импортировать маршрутизацию веб-сокетов
from socketapp.routing import ws_urlpatterns

# Назначьте значение для DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

# Определить переменные приложения для обработки HTTP и WebSocket
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})