import pandas as pd
import plotly.express as px

# Your Google Sheet CSV URL
csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRf7_brqmUmLakk3sJddTgOFK9naYpIAPTOMMCIpVbJgysZy3tXpXPa1-JUaiWAOJiqCtfsFpE2tCIP/pub?gid=0&single=true&output=csv'

# Reading the data into a pandas DataFrame
df = pd.read_csv(csv_url)
df['Superhelt'] = df['Superhelt'].apply(lambda x: x + ':    ')

# Melting the DataFrame
df_melted = df.melt(id_vars=["Superhelt"], value_vars=["Kul", "Atypisk", "Plausibel", "Praktisk", "Ekstraordinær"], 
                    var_name="Kategori", value_name="Poeng")

# Creating the stacked bar chart
fig = px.bar(df_melted, y="Superhelt", x="Poeng", color="Kategori", orientation="h",
             labels={"Superhelt": "Superhelt", "Poeng": "Poeng"}, 
             height=600, text="Poeng")

# Improve the layout
fig.update_layout(yaxis_categoryorder='total ascending', # This sorts the bars based on 'Total'
                    yaxis_title="", margin=dict(l=10))  
fig.update_traces(texttemplate='%{text}', textposition='inside', textangle=0)

fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,  # Places the legend above the plot
        xanchor="center",
        x=0.5  # Centers the legend
    )
)

number_of_superheroes = df["Superhelt"].nunique()

for i in range(number_of_superheroes):
    fig.add_annotation(x=0, y=(number_of_superheroes-i-1),
                       text=str(i+1), showarrow=False,
                       xref="paper", yref="y",
                       xanchor='right', yanchor='middle')
    if (i-1) % 5 == 0:
        # Add a divider line after this superhero
        fig.add_shape(
            type="line",
            x0=0,  # Starting x position of the line (adjust as needed)
            y0=i-0.5,  # Starting y position of the line, aligned with the superhero's rank
            x1=1,  # Ending x position of the line (set to span the width of the plot)
            y1=i-0.5,  # Ending y position of the line, same as the starting position to make it horizontal
            xref="paper",  # Using 'paper' reference to span the whole x axis
            yref="y",  # Referencing the y-axis data for positioning
            line=dict(
                color="Grey",  # Line color
                width=2,  # Line thickness
            ),
        )                

# Show the figure
fig.write_html("assets/charts/total.html")
