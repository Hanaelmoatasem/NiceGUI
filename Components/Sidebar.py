from nicegui import ui
from nicegui.elements.icon import Icon
from Components import Buttons

def Sidebar():
    with ui.column().classes('w-64 bg-gray-800 text-white p-4 h-full flex'):
        ui.image('Images/logo.png').classes('w-32 h-auto mx-auto mb-6')
        with ui.column().classes('gap-2'):
            def link_btn(icon: str, text: str, path: str):
                with ui.button(on_click=lambda path=path: ui.navigate.to(path)).props('flat unelevated').classes(
                    ' gap-4 p-4 w-full rounded mb-2 no-underline '
                    'hover:bg-gray-100 text-white '
                ):
                    with ui.row().classes(' gap-4 w-full hover:text-gray-800'): 
                        ui.label(text).classes('text-xl font-medium normal-case ')  
            
            link_btn('o_dashboard', 'Virtual Target', '/')
            link_btn('o_lock', 'Certicate Store', '/')
        
        with ui.column().classes('pt-4 border-t border-gray-600'):
            with ui.button(on_click=lambda: print('Logged out')).props('flat unelevated').classes(
                    ' gap-4 p-4 w-full rounded mb-2 no-underline '
                    'hover:bg-gray-100 hover:text-gray-800 text-white '
            ):
                with ui.row().classes('gap-4 w-full hover:text-gray-800'):
                    #ui.label('Logout').classes('text-xl font-medium normal-case')
                    ui.icon('logout').classes('allign-right')



def Sidebar2():
     selected_tab = 'Virtual Targets'
     selected_tab = 'Policies'
     selected_tab = 'Dashboard'
     with ui.column().classes('fixed w-64 bg-gray-800 text-white h-screen flex '):
        ui.image('Images/logo.png').classes('w-32 h-auto mx-auto mb-6 mt-6')
        with ui.column().classes('gap-2 w-full'):
             with ui.column().classes('pt-4 w-full border-b border-gray-600'):
               with ui.row().classes('gap-4 w-full border-l-4 border-blue-500 p-4'):
                    ui.label('Virtual Targets #1').classes('text-xl font-medium normal-case p-2')

             with ui.button(on_click=lambda: print('Dashboard clicked')).props('flat unelevated').classes(
                     ' gap-4 p-4 w-full rounded mb-2 no-underline '
                     'hover:bg-transparent  text-white '):      
                with ui.row().classes(' gap-4 w-full hover:text-blue-600'):
                    ui.label('Dashboard').classes('font-medium normal-case')

             with ui.expansion('SSL/TLS').classes('bg-transparent hover:text-blue-600 w-full'):
                 with ui.column().classes('w-full'):
                     Buttons.Button('Add Certificate', lambda: print('Add Cert'))
                     Buttons.Button('Certificate Store', lambda: print('Cert Store'))

             with ui.expansion('Policies').classes('bg-transparent hover:text-blue-600 w-full'):
                  with ui.column().classes('w-full '):
                       Buttons.Button('Rate Limiter', lambda: print('Rate Limiter'))
                       Buttons.Button('Security Rules', lambda: print('Security Rules'))

              
        
        ui.space();

        
        with ui.row().classes('items-center gap-3 px-2 py-3 rounded-lg hover:bg-blue-100 hover:text-blue-600'):
            ui.avatar('https://www.gravatar.com/avatar/placeholder?d=mp').props('size=36')
            with ui.column().classes('leading-none'):
                ui.label('Admin').classes('text-sm font-semibold')
                ui.label('admin@email.com').classes('text-xs text-gray-400')
