class Config:
    SECRET_KEY = '57e86353aa22384859a33d3156a60abfa247869323cb7cfc'

# Add all blueprints and Dash apps to be registered
blueprints = [
    {'name':'main'}
]

dash_apps = [
    {'name': 'dash_app', 'multi_page': False}, 
    {'name': 'dash_app2', 'multi_page': False}
]