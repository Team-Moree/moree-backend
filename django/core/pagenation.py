import math
from rest_framework import pagination


class BasePagination(pagination.PageNumberPagination):
    page_size = 500

    def get_paginated_response(self, data):
        response = super(BasePagination, self).get_paginated_response(data)
        count = response.data.get("count", 0)
        if count == 0:
            response.data["max_page"] = 1
        else:
            response.data["max_page"] = math.ceil(count / self.page_size)
        return response
