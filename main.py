from nicegui import ui
from pages import Dashboard , Home , Report , Setting

from Components import Card, Header , Layout , Sidebar

from nicegui import ui



@ui.page('/')
def Home_page():
     Home.render()
     

@ui.page('/dashboard')
def Dashboard_page():
     Dashboard.render()

@ui.page('/report')
def Report_page():
     Report.render()



@ui.page('/settings')
def settings():
     Setting.render()




ui.run()
