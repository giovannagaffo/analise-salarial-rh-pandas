import pandas as pd
import numpy as np

#Loading the data spreadsheet 
df = pd.read_excel('1st_Phase_-_Selective_Process_-_Data_Science_-_DataBase.xlsx', engine='openpyxl')

#Function to calculate the Median Absolute Deviation
def calculate_mad(series):
    median = series.median()
    return (series - median).abs().median()

#Generating salary analysis tables grouped by job title and location 
analysis = df.groupby(['CARGO', 'LOCAL'])['SALARIO_MENSAL'].agg([
    ('Mediana_Salarial', 'median'),
    ('MAD_Salarial', calculate_mad),
    ('Contagem', 'count')
]).reset_index()

#Calculating the percentage difference in median salaries between locations
pivot_mediana = analysis.pivot(index='CARGO', columns='LOCAL', values='Mediana_Salarial')
pivot_mediana['Diff_Perc_Cap_Int'] = ((pivot_mediana['CAPITAL'] - pivot_mediana['INTERIOR']) / pivot_mediana['INTERIOR']) * 100

#Assessing operational continuity risk: identifying high-tenure employees near retirement age
df['Risco_Sucessao'] = (df['IDADE'] > 50) & (df['TEMPOCASA'] > 15)
risco_df = df[df['Risco_Sucessao'] == True][['ID', 'CARGO', 'IDADE', 'TEMPOCASA', 'SALARIO_MENSAL']]

#Defining turnover and retention indicators by identifying salary anomalies relative to tenure
medias_por_cargo = df.groupby('CARGO')['SALARIO_MENSAL'].transform('median')

df['Alerta_Turnover'] = 'Normal'
df.loc[(df['TEMPOCASA'] > 10) & (df['SALARIO_MENSAL'] < medias_por_cargo), 'Alerta_Turnover'] = 'Veterano c/ Salário Baixo'
df.loc[(df['TEMPOCASA'] < 2) & (df['SALARIO_MENSAL'] > medias_por_cargo), 'Alerta_Turnover'] = 'Novato c/ Salário Alto'

#Generating turnover alert table: filtering non-standard salary-to-tenure outliers
tabela_turnover = df[df['Alerta_Turnover'] != 'Normal'][['ID', 'CARGO', 'TEMPOCASA', 'SALARIO_MENSAL', 'Alerta_Turnover']]

#Educational salary gap table: comparing median compensation by job role and degree level
tabela_educacao = df.groupby(['CARGO', 'EDUCAÇÃO'])['SALARIO_MENSAL'].median().unstack().reset_index()

#Exporting data to Excel: finalizing the file creation and ensuring all buffers are written
writer = pd.ExcelWriter('Analise_Salarial_Final.xlsx', engine='xlsxwriter')

#Writing data to worksheets
analysis.to_excel(writer, sheet_name='Analise_Principal', index=False)
pivot_mediana.to_excel(writer, sheet_name='Comparativo_Cap_Int')
risco_df.to_excel(writer, sheet_name='Risco_Sucessao', index=False)
tabela_turnover.to_excel(writer, sheet_name='Alertas_Turnover', index=False)
tabela_educacao.to_excel(writer, sheet_name='Comparativo_Educacao', index=False)

#chart on the main worksheet
workbook  = writer.book
#selecting the specific sheet where the chart will be placed
worksheet = writer.sheets['Analise_Principal']
#initializing a new chart object and defining it as a column chart
chart = workbook.add_chart({'type': 'column'}) 

#configuring the data series for the chart
chart.add_series({
    'name':       'Mediana Salarial',
    'categories': ['Analise_Principal', 1, 0, 6, 1],
    'values':     ['Analise_Principal', 1, 2, 6, 2],
    'fill':       {'color': '#4F81BD'},
    'data_labels': {'value': True},
})

#setting the main title for the chart visualization
chart.set_title({'name': 'Mediana Salarial por Segmento'})
#inserting the finalized chart into the worksheet starting at cell e2
worksheet.insert_chart('E2', chart)

#closing the writer to finalize data writing and save the file
writer.close()

#printing a success message to confirm the file was successfully created
print("O arquivo 'Analise_Salarial_Final.xlsx' foi gerado.")