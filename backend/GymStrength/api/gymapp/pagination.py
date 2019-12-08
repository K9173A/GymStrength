"""
Module for gymapp pagination classes.
"""
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class WorkoutPageNumberPagination(PageNumberPagination):
    """
    Pagination class for list of workouts.
    """
    page_size = 10
    page_query_param = 'page'

    def get_paginated_response(self, data):
        """
        Gets paginated chunk of data
        :return: response with data and pagination information.
        """
        return Response({
            'next': self.get_next_page_number(),
            'curr': self.page.number,
            'prev': self.get_previous_page_number(),
            'results': data,
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
        })

    def get_next_page_number(self):
        """
        Gets next page number if it exists.
        :return: page number.
        """
        if self.page.has_next():
            return self.page.next_page_number()
        return None

    def get_previous_page_number(self):
        """
        Gets previous page number if it exists.
        :return: page number.
        """
        if self.page.has_previous():
            return self.page.previous_page_number()
        return None
