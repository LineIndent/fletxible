
def route(e, route):
    e.page.views.clear()
    if route == '/index':
        e.page.views.append(returned_modules[route].loader.load_module().page_view())
        e.page.go('/index')
    if route == '/about':
        e.page.views.append(returned_modules[route].loader.load_module().page_view())
        e.page.go('/about')

