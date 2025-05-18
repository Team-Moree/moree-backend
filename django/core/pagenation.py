from rest_framework import pagination


class BasePagination(pagination.PageNumberPagination):
    page_size = 500

    def get_paginated_response(self, data):
        response = super(BasePagination, self).get_paginated_response(data)
        response.data["current_page"] = self.page.number
        response.data["max_page"] = self.page.paginator.num_pages
        return response
