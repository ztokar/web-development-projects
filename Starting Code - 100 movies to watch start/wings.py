import xlwings as xw 
import pandas as pd
import matplotlib.pyplot as plt
# wb=xw.Book()
# sheet=wb.sheets['Sheet1']
# sheet['A1'].value='Foo 1'
# print(sheet["A1"].value)
# sheet['A1'].value=[[1,23,4],[4,5,6]]
# print(sheet["A1"].expand().value)
# df=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
# sheet["A1"].value=df
xw.Book().sheets['Sheet1']['A1'].value="Hello"

# fig = plt.figure()
# plt.plot([1, 2, 3, 4, 5])
# sheet.pictures.add(fig, name='MyPlot', update=True)