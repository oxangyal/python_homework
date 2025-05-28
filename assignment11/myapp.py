from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Load the gapminder dataset
df = pldata.gapminder()

# Get unique country names for the dropdown
countries = df['country'].unique()

# Initialize Dash app
app = Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    # Filter data for selected country
    filtered_df = df[df['country'] == selected_country]

    # Create line plot
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP per Capita Growth in {selected_country}",
        markers=True
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)
