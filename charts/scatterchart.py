import pandas as pd
import plotly.express as px

df = pd.read_csv("charts/data.csv")
dl = px.scatter(df , x = "Population" , y="Per capita" , color="Country" , size_max= 60)
dl.show()