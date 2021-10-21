from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=20),
    'ROTATE_REFRESH_TOKENS': True,  # повертати Refresh token при рефреші
    'BLACKLIST_AFTER_ROTATION': True, # класти уже "мертвий" токін в blacklist після відправки нового Refresh token
    'AUTH_HEADER_TYPES': ('Bearer',), # частіше всього перед токіном ставлять дане слово 'Bearer' або 'JWT'
}