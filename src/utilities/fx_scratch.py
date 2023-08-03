# ## Original code block for returning views as instances ...

# for file in os.listdir("pages"):
#     if os.path.isfile(f"pages/{file}"):
#         filename = os.path.splitext(file)[0]
#         if "/" + filename == route:
#             filepath = os.path.join("pages", file)
#             module_spec = importlib.util.spec_from_file_location(
#                 filename, filepath
#             )
#             module = importlib.util.module_from_spec(module_spec)
#             module_spec.loader.exec_module(module)
#             return module.FxView(page, docs)
