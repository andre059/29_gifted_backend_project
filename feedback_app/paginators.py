from rest_framework.pagination import PageNumberPagination


class FeedbackPaginator(PageNumberPagination):
    """Показывает количество отзывов на странице"""
    page_size = 3
