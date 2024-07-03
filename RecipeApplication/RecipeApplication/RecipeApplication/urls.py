from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from search import views as search_views
from user import views as user_views
from recipe import views as recipe_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', user_views.UserViewSet)
router.register(r'recipes',recipe_views.RecipeViewSet)
router.register(r'ingredients',recipe_views.IngredientViewSet)

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path('user/', include('user.urls')),
    path('recipe', include('recipe.urls')),
    path('rest/', include(router.urls)),  # routes REST générées
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # route pour documentation API REST
    path('', include(wagtail_urls))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
