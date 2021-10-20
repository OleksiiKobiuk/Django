REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
# налаштування пагінації
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,

# налаштування фільтрації
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),

# налаштування Simple JWT (токін)
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (  # вказує, що всіх в'юшок матимуть доступ лише ті, хто вже залогінився в систему,
        # тобто той, хто "прийшов" з токіном
        'rest_framework.permissions.IsAuthenticated',
    )

}