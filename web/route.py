def route(e, route):
    current = -1
    index: int

    for view in e.page.views[:]:
        if view.route == route:
            index = e.page.views.index(view)

    if route == "/index":
        e.page.views[index], e.page.views[current] = (
            e.page.views[current],
            e.page.views[index],
        )
        e.page.update()
    if route == "/about":
        e.page.views[index], e.page.views[current] = (
            e.page.views[current],
            e.page.views[index],
        )
        e.page.update()
