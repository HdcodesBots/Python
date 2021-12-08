import pandas as pd
import plotly.express as px

df = pd.read_csv("charts/hi.csv")
dl = px.scatter(df , x = "date" , y ="cases" , color="country" ) 
dl.show()