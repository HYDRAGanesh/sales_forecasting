from dash import dcc, html


def layout():
    return html.Div(className='login-form', children=[
        html.H2('Login'),
        html.Label('Username'),
        dcc.Input(id='login-username', type='text'),
        html.Label('Password'),
        dcc.Input(id='login-password', type='password'),
        html.Button('Login', id='login-button'),
        html.Div(id='login-output')
    ])


def login(username, password):
    # Check if the username and password are valid
    if username == 'username' and password == 'mypassword':
        return 'Login successful'
    else:
        return 'Invalid credentials'
