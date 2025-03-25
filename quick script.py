from nicegui import ui

with ui.pagination(1,5):
    for i in range(1,100):
        ui.label("i")
# Run the UI
ui.run()
