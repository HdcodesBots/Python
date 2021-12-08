import pandas as pd
import plotly.express as px

df = pd.read_csv("basic/line_chart.csv")
dl = px.line(df , x = "Year" , y ="Per capita income" , color="Country" , title= "Per Capita Income ") 
dl.show()