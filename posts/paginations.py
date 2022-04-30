from rest_framework.pagination import LimitOffsetPagination

class CustomeLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4