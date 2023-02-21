from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import Http404
from django.utils import six
from rest_framework import pagination


def get_paginated_serializer(queryset, request, serializer_class, context,
                              page_size=50, page_kwarg='page', *args, **kwargs):
    '''Get paginated serializer loaded with all the data'''
    paginator = Paginator(queryset, page_size)
    page_kw = kwargs.get(page_kwarg)
    page_query_param = request.query_params.get(page_kwarg)
    page = page_kw or page_query_param or 1

    try:
        page_number = paginator.validate_number(page)
    except InvalidPage:
        if page == 'last':
            page_number = paginator.num_pages
        else:
            raise  Http404("Page is not 'last', nor can it be converted to an int.")

    try:
        queryset = paginator.page(page_number)
    except InvalidPage as exc:
        error_format = _('Invalid page (%(page_number)s): %(message)s')
        raise Http404(error_format % {
            'page_number': page_number,
            'message': six.text_type(exc)
        })

    class PaginatedSerializer(pagination.PaginationSerializer):
                class Meta:
                    object_serializer_class = serializer_class
    serializer = PaginatedSerializer(instance=queryset, context=context)
    return serializer