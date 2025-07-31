from nicegui import ui


def header():
   with ui.row().classes('w-full items-center p-2 px-4'):
    ui.label('WebJAT').classes('text-xl font-bold text-gray-800')  

    with ui.row().classes('items-center gap-2 ml-auto' ):
        ui.icon('account_circle').classes('text-gray-400 text-2xl')
        ui.label('Admin').classes('text-sm font-small text-gray-400')

