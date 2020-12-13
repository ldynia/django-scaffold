from config.settings import INSTALLED_APPS

def valid_arg(arg):
    return arg is not None or arg != '' 

def app_exist(app, apps=INSTALLED_APPS):
    return app in [app.split('.')[0] for app in apps]