from lib.renderer import request_render


def index(request):
    tpl_vars = {
        'page_title': '\_o<~ KOIN KOIN INDEX'
    }
    return request_render(request, 'index.j2', tpl_vars)
