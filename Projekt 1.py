import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('ludnosc.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

print(df[['Kraj',2006, 2017]])
roznica = pd.Series(abs(df[2006] - df[2017]))
df['Roznica'] = roznica

plik = df[['Kraj',2006,2017,'Roznica']]
sortuj = plik.sort_values(by = 'Roznica', ascending = False)
print(sortuj[0:10])
posortowane = (sortuj[0:10])
wynik = posortowane[['Kraj',2006,2017]]
wynik.plot.bar('Kraj', figsize = (10, 10))
plt.ylabel('Populacja w miliardach', fontsize = 12)
plt.xlabel('Kraj', fontsize = 15)
plt.xticks(rotation = 10)
plt.legend(loc = 'upper right')
plt.title('Największa różnica w liczbie ludności pomiędzy 2006 a 2017 rokiem.')
plt.show()