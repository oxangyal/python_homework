# Task 3: Interactive Visualizations with Plotly
import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))

df['strength'] = df['strength'].str.replace(r'.*\-','',regex=True)
df['strength'] = df['strength'].str.replace(r'\D','',regex=True)


df['strength'] =df['strength'].astype('float')


fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Data", hover_data=["strength"])
fig.write_html("wind.html", auto_open=True)