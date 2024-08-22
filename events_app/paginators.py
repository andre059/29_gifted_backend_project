from rest_framework.pagination import PageNumberPagination


class EventsPaginator(PageNumberPagination):
    """Displaying the number of events per page"""

    page_size = 3
