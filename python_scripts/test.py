import pandas as pd
import plotly.express as px


# Your Google Sheet CSV URL
csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRf7_brqmUmLakk3sJddTgOFK9naYpIAPTOMMCIpVbJgysZy3tXpXPa1-JUaiWAOJiqCtfsFpE2tCIP/pub?gid=0&single=true&output=csv'

# Reading the data into a pandas DataFrame
df = pd.read_csv(csv_url)

# Assuming `df` is your DataFrame
fig = px.bar(df, y='Superhelt', x='Total', orientation='h', 
             title="Total Scores of Superheroes",
             labels={"Superhelt": "Superhero", "Total": "Total Score"},
             height=800) # Adjust the height based on the number of items

# Improve the layout
fig.update_layout(yaxis_categoryorder='total ascending')  # This sorts the bars based on 'Total'

# Show the figure
fig.write_html("superheroes_total_score.html")