from nicegui import ui
from Components import Card, Header, Layout , Sidebar



def render():
     Header.header()
     with ui.row().classes('w-full h-screen m-0 '):
          Sidebar.Sidebar()
          with ui.row():
               Card.Component("Dashbord", "this is dashboard")
