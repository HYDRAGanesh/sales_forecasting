import dash
from dash.dependencies import Input, Output, State
import login

external_stylesheets = ['style.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = login.layout()


@app.callback(Output('login-output', 'children'),
              [Input('login-button', 'n_clicks')],
              [State('login-username', 'value'),
               State('login-password', 'value')])
def login_callback(n_clicks, username, password):
    if n_clicks is None:
        return ''
    elif n_clicks > 0:
        return login.login(username, password)


if __name__ == '__main__':
    app.run_server(debug=True)
