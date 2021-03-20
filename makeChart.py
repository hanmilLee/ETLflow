import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv ('df.csv')
LinkSourceTarget = pd.read_csv ('nodeinfo.csv')

table = input('Table명을 입력하세요: ')

str_expr = "Table.str.contains('{}')".format(table) # 문자열에 tiger 포함
tablelist = list(set(list(df.query(str_expr).Table)))
a = 0

while True:
    b = len(tablelist)
    if a == b:
        break
    a = b
    tablelist = list(set(list(df[df['Target'].isin(tablelist)].Table) + list(df[df['Table'].isin(tablelist)].Target)))

df = df[df['Table'].isin(tablelist)]


fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = list(LinkSourceTarget.node),
      customdata = list(LinkSourceTarget.node),
      # color='grey'
    ),
    link = dict(
      source = list(df.linkSource), # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = list(df.linkTarget),
      value = [1]*len(list(df.linkTarget)),
      customdata = list(df.ETL),
      # color = list(df.LocationColor),
      hovertemplate='Source: %{source.customdata}<br />Target: %{target.customdata}<br />'+'ETL Job: %{customdata}<extra></extra>',
  ))])

fig.update_layout(title_text="[%{}% Table 기준] ETL flow <br><a href=''></a>".format(table),
                  # font_size=10
                  )
fig.show()