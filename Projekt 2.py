import pandas as pd
import matplotlib.pyplot as plt
import xlrd 
import openpyxl

xlsx = pd.ExcelFile("ludnosc.xlsx")
df = pd.read_excel(xlsx,'Arkusz1')
plik = df[['Kraj', 2017]]
sort = plik.sort_values(by = 2017, ascending = False)
print(sort[0:10])
sort= (sort[0:10])
group = sort.groupby(['Kraj']).agg({2017:['sum']})
group.plot.pie(subplots = True, autopct = '%.2f %%', fontsize = 10, figsize = (12, 12))
plt.legend(loc = "upper left", fontsize = 7)

plt.title('Najludniejsze kraje i regiony świata')
plt.show()