from script import route_keys
def route(e, route):
    e.page.views.clear()
    if route == '/index':
        e.page.views.append(route_keys[route].loader.load_module().pageView())
        e.page.go('/index')
    if route == '/about':
        e.page.views.append(route_keys[route].loader.load_module().pageView())
        e.page.go('/about')

