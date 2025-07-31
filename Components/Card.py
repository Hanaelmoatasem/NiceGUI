from nicegui import ui

def Component(title: str, Host: str, Balancer_Strategy: str, Request_Timeout:str, mood:str ):
    with ui.card().classes('w-full sm:w-80 h-40 rounded-2xl flex flex-wrap justify-center p-4 border-l-8 border-2 border-green-600 hover:bg-gray-100 shadow'):
        ui.label(title).classes('text-xl font-bold mb-1 text-gray-600 text-left')
        ui.label(Host).classes('text-gray-500 text-sm text-left')
        ui.label(Balancer_Strategy).classes('text-gray-500 text-sm text-left')
        ui.label(Request_Timeout).classes('text-gray-500 text-sm text-left')
        ui.label(mood).classes('text-sm font-medium text-green-700 mt-2')

def CardButton(title: str, description: str, on_click):
    with ui.button(on_click=on_click).classes(
        ' group w-full sm:w-80 h-40 bg-white rounded-2xl border border-dashed border-gray-600 box-shadow-none'):
        with ui.column().classes('flex flex-col items-center justify-center p-4 '):
            ui.label(title).classes('text-4xl font-medium text-gray-400 text-center group-hover:text-gray-700')
            ui.label(description).classes('text-gray-400 text-sm text-center normal-case group-hover:text-gray-700')

def Node_Component (title: str, descrp: str,on_click):
    with ui.button(on_click=on_click).props('flat unelevated').classes(
        ' w-full sm:w-80 h-40 bg-white rounded-2xl border border-solid border-gray-200 hover:bg-gray-100 '):
        with ui.column().classes('w-full items-start p-4 gap-2'):
            ui.label(title).classes('text-xl font-bold mb-1 text-gray-600 text-left normal-case')
            ui.label(descrp).classes('text-gray-500 text-sm text-left normal-case')
