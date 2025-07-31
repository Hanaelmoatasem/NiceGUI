from nicegui import ui
from Components import Card, Header, Layout, Sidebar
from Components.Buttons import defense_option

def styled_input(label: str, placeholder: str):
    with ui.column().classes('flex-1'):
        ui.label(label).classes('text-sm text-gray-500 mb-1')
        ui.input(placeholder).props('outlined dense').classes(
            'w-full rounded-md bg-white shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
        )

def render():
  
        with ui.row().classes('bg-gray-100 w-full '):
            Sidebar.Sidebar2()

            with ui.column().classes('gap-4 ml-64 p-4 flex-1 overflow-auto'):
                
                
                with ui.row().classes('w-full justify-between items-center'):
                    with ui.row().classes('gap-1'):
                        ui.label('Virtual Target #1  /').classes('text-gray-500 text-base')
                        ui.label('Policies  /').classes('text-gray-500 text-base')

                        ui.label('Security Rules').classes('text-gray-700 text-base font-semibold')

               
                with ui.card().classes('p-6 rounded-xl shadow bg-white w-full'):
                    ui.label('Paranoia Level').classes('text-xl font-bold text-gray-800 mb-4')

                    with ui.row().classes('w-full gap-6'):
                        defense_option(
                                title='Basic Defense',
                                badge_text='Standard',
                                description_lines=[
                                    'Basic validation and threat detection.',
                                    'Assumes normal user and system behavior.',
                                    'Best for non-critical, low-risk applications.',
                                    'Low false positives, may miss critical issues.',
                                ],
                                selected=True
                            )

                        defense_option(
                                title='Medium Defense',
                                badge_text='Balanced',
                                description_lines=[
                                    'Reasonable validation and error handling.',
                                    'Protects against common errors and attacks.',
                                    'Suited for moderately critical applications.',
                                    'Occasional false positives possible.',
                                ],
                                selected=False
                            )
                        defense_option(
                                title='High Defense',
                                badge_text='Strict',
                                description_lines=[
                                    'Reasonable validation and error handling.',
                                    'Protects against common errors and attacks.',
                                    'Suited for moderately critical applications.',
                                    'May trigger occasional false positives',
                                ],
                                selected=False
                            )   
                        defense_option(
                                title='Extreme Defense',
                                badge_text='Paranoid',
                                description_lines=[
                                    'Reasonable validation and error handling.',
                                    'Protects against common errors and attacks.',
                                    'Suited for moderately critical applications.',
                                    'May trigger occasional false positives',
                                ],
                                selected=False
                            )     

                with ui.card().classes('p-6 rounded-xl shadow bg-white w-full'):
                    ui.label('Select Defense Presets').classes('text-xl font-bold text-gray-800 mb-4')
                    ui.label ('Add node, configure and monitor items').classes('text-sm text-gray-500 mb-4')
                    with ui.row().classes('gap-6'):
                         Card.CardButton("+", "Add New Node", on_click=lambda: ui.navigate.to('/'))
                         Card.Node_Component("Node 1", "address: https://jsonplaceholder", on_click=lambda: print("Node1"))

                with ui.card().classes('p-6 rounded-xl shadow bg-white w-full'):
                    ui.label('Node Name').classes('text-xl font-bold text-gray-800 mb-4')
                    ui.label ('Add node, configure and monitor items').classes('text-sm text-gray-500 mb-4')
                  

          
                with ui.row().classes(
                    'w-full h-12 bg-white border-t border-gray-200 justify-center items-center fixed bottom-0 z-50'):
                    ui.label('© 2025 WebJAT - All rights reserved').classes('text-gray-500 text-sm')

