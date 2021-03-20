import pandas as pd
from pandas import DataFrame

# 전처리하기 todo 쿼리로 dataframe 만들기
df = pd.read_csv ('Source.csv')

dfTarget = df[df['SorT'] =='Target']
df = df[df['SorT'] =='Source']

df.insert(2,'Target',df['ETL'].map(dfTarget.set_index('ETL')['Table']))

LinkSourceTarget = pd.DataFrame({'node':list(set(list(df.Table)+list(df.Target) ))})
LinkSourceTarget['index'] = LinkSourceTarget.index.tolist()

df.insert(3, 'linkSource',df['Table'].map(LinkSourceTarget.set_index('node')["index"]))
df.insert(4, 'linkTarget',df['Target'].map(LinkSourceTarget.set_index('node')["index"]))
# df.loc[df['Location'] == 'Lake', 'LocationColor'] = 'rgba(44, 160, 44, 0.4)'
# df.loc[df['Location'] == 'DAP', 'LocationColor'] = 'rgba(31, 119, 180, 0.4)'
# df = df.fillna('rgba(255,0,255, 0.4)')

df.to_csv('df.csv')
LinkSourceTarget.to_csv('nodeinfo.csv')

# ['rgba(31, 119, 180, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(227, 119, 194, 0.4)', 'rgba(127, 127, 127, 0.4)', 'rgba(188, 189, 34, 0.4)', 'rgba(31, 119, 180, 0.4)', 'rgba(23, 190, 207, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(214, 39, 40, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(127, 127, 127, 0.4)', 'rgba(127, 127, 127, 0.4)', 'rgba(127, 127, 127, 0.4)', 'rgba(188, 189, 34, 0.4)', 'rgba(23, 190, 207, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(148, 103, 189, 0.4)', 'rgba(148, 103, 189, 0.4)', 'rgba(255,0,255, 0.4)', 'rgba(255,0,255, 0.4)', 'rgba(227, 119, 194, 0.4)', 'rgba(188, 189, 34, 0.4)', 'rgba(127, 127, 127, 0.4)', 'rgba(23, 190, 207, 0.4)', 'rgba(23, 190, 207, 0.4)', 'rgba(31, 119, 180, 0.4)', 'rgba(31, 119, 180, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(44, 160, 44, 0.4)', 'rgba(214, 39, 40, 0.4)', 'rgba(214, 39, 40, 0.4)', 'rgba(148, 103, 189, 0.4)', 'rgba(148, 103, 189, 0.4)', 'rgba(148, 103, 189, 0.4)', 'rgba(227, 119, 194, 0.4)', 'rgba(227, 119, 194, 0.4)', 'rgba(227, 119, 194, 0.4)', 'rgba(148, 103, 189, 0.4)', 'rgba(140, 86, 75, 0.4)', 'rgba(227, 119, 194, 0.4)', 'rgba(127, 127, 127, 0.4)', 'rgba(255,0,255, 0.4)', 'rgba(255,0,255, 0.4)']