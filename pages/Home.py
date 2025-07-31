from nicegui import ui
from Components import Card, Header, Layout, Sidebar

def render():

        with ui.row().classes('bg-gray-100 w-full flex-1 '):  
            Sidebar.Sidebar2() 
            with ui.column().classes('gap-4 ml-64 p-4 flex-1 overflow-auto'):    
                with ui.row().classes('gap-4 p-5 flex-1 '):
                    ui.label('Virtual Target #1  /').classes('text-gray-500 text-base')
                    ui.label('Policies  /').classes('text-gray-500 text-base')

                    ui.label('Security Rules').classes('text-gray-700 text-base font-semibold')
                    
                    with ui.row().classes('gap-4 w-full flex-wrap'):
                        with ui.card().classes('flex flex-row items-center gap-4 p-8 bg-white rounded-lg shadow w-full'):
                            Card.CardButton("+", "Add Virtual Target", on_click=lambda: ui.navigate.to('/settings'))
                            Card.Component("Nour", "Host: dashboard1.aos.fit", "Balancer Strategy: random", "Request Timeout: 5", "🟢 Healthy")
