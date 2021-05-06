import pandas as pd
from openpyxl import load_workbook
# new dataframe with same columns
df = pd.DataFrame({'Country': ["bro"],
                   'PM25': ["wat"],
                   'Year': ["the fuck"]})
writer = pd.ExcelWriter('4c_result.xlsx', engine='openpyxl')
# try to open an existing workbook
writer.book = load_workbook('4c_result.xlsx')
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel(r'4c_result.xlsx')
# write out the new sheet
df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

writer.close()