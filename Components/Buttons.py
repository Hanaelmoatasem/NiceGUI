from nicegui import ui

def Button(label: str, on_click=callable):
     with ui.button(on_click=on_click).props('flat unelevated').classes(
                     ' gap-4 p-4 w-full rounded mb-2 no-underline '
                     'hover:bg-transparent  text-white '):      
                with ui.row().classes(' gap-4 w-full hover:text-blue-600'):
                    ui.label(label).classes('text-sm font-medium normal-case')

def defense_option(title: str, badge_text: str, description_lines: list, selected: bool):
    border_color = 'border-blue-500' if selected else 'border-gray-300'
    badge_bg = 'bg-blue-100'
    badge_text_color = 'text-blue-700' 

    with ui.card().classes(f'w-[318px] p-4 border-2 rounded-xl {border_color} hover:bg-blue-100 shadow-sm transition-colors'):
        with ui.row().classes('justify-between items-center'):
            with ui.row().classes('items-center gap-2'):
                ui.label(title).classes('text-lg font-semibold')
                ui.label(badge_text).classes(
                    f'{badge_bg} {badge_text_color} text-xs font-semibold px-2 py-1 rounded-full'
                )
                ui.icon('radio_button_checked' if selected else 'radio_button_unchecked').classes(
                    'text-blue-600 flex justify-end' if selected else 'text-gray-400'
                )

        for line in description_lines:
            ui.label(f'• {line}').classes('text-sm text-gray-600 mt-1')