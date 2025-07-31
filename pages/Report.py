from nicegui import ui
from Components import Card, Header, Layout , Sidebar

def render():
     Header.header()
     with ui.row().classes('w-full h-screen'):
          Sidebar.Sidebar()
          with ui.row():
               Card.Component("Report", "this is Report")

