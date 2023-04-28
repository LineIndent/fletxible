""" """


def router(e, route):
    if route == "/index":
        # e.page.views.append(_moduleList[page_route].loader.load_module()._view_())
        e.page.go("/index")
        e.page.update()
    if route == "/about":
        # e.page.views.append(_moduleList[page_route].loader.load_module()._view_())
        e.page.go("/about")
        e.page.update()
    if route == "/contanct":
        # e.page.views.append(_moduleList[page_route].loader.load_module()._view_())
        e.page.go("/contact")
        e.page.update()
