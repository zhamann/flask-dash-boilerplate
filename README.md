# Flask App Boilerplate

This repository is designed to include all of the setup components of a Flask application, including configuration for Dash applications within the Flask application.

The app is structured as follows:

```
- app
    - __init.py__
    - blueprints
        - main
            - __init.py__
            - routes.py
    - dash_app
    - dash_app2
    - static
    - templates
- .env
- config.py
- requirements.txt
- run.py
```

All blueprints and Dash apps that have been added to **config.py** are initalized in the **app/init.py** file.
