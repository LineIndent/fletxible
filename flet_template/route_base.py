route_page = """from script import run_template_script

returned_modules, __ = run_template_script()


def router(e, route):
    e.page.views.clear()
%s
    
"""
