import pandas as pd
import plotly.express as px

df = pd.read_csv("charts/data.csv")
dl = px.bar(df,x = "Country" , y = "InternetUsers" , color = "Country" )
dl.show()