from django.urls import include, path
from .views import (login, index, presentation,
                    detail_news, register, simulator,
                    create_post)

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('presentation', presentation, name='presentation'),
    path('login/', login, name="login"),
    path('detail/', detail_news, name="detail"),
    path('register/', register, name="register"),
    path('simulator/', simulator, name="simulator"),
    path('create-post/', create_post),
    path('city/', include('city.urls'))
]
