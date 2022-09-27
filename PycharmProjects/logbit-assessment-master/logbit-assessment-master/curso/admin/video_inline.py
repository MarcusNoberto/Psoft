import nested_admin

from ..models import Video


class VideoInline(nested_admin.NestedStackedInline):
    model = Video

    extra = 0

    fields = [
        'titulo',
        'descricao',
        'thumbnail',
        'video',
        'ordem',
    ]

    classes = [
        'collapse',
    ]
