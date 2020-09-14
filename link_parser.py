import pandas as pd

links = pd.read_csv('product_links.csv')

print(links.head(5))

decades = []

for x in links["Links"]:
    year_string = x[x.find(".com/")+5:]
    year = year_string[0:3]
    decades.append(year)
    print(year)

links.insert(1,"Decade",decades)

seventies_links = links.query('Decade == "197"')['Links']
eighties_links = links.query('Decade == "198"')['Links']
nineties_links = links.query('Decade == "199"')['Links']
twothousand_links = links.query('Decade == "200"')['Links']
twothousandten_links = links.query('Decade == "201"')['Links']

seventies_links.to_csv(path_or_buf='hallmark_ornaments_70.csv',index=False,header="Links")
eighties_links.to_csv(path_or_buf='hallmark_ornaments_80.csv',index=False,header="Links")
nineties_links.to_csv(path_or_buf='hallmark_ornaments_90.csv',index=False,header="Links")
twothousand_links.to_csv(path_or_buf='hallmark_ornaments_20.csv',index=False,header="Links")
twothousandten_links.to_csv(path_or_buf='hallmark_ornaments_21.csv',index=False,header="Links")
