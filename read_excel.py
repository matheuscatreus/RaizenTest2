import pandas as pd
import datetime,time, locale

def str_to_date(str):
    locale.setlocale(locale.LC_TIME, "pt_br")
    local_time = time.strptime(str,"%Y-%b")

    return datetime.datetime(local_time.tm_year,local_time.tm_mday, 1)

excel_path = r"G:\RaizenTest\vendas-combustiveis-m3.xls"
csv_path = r"G:\RaizenTest\fuel-sells-m3.xls"

df = pd.read_excel(excel_path, sheet_name="Sheet1").drop(columns=["TOTAL"])

pivoted_df = df.melt(id_vars=["COMBUSTÍVEL","ANO","REGIÃO","ESTADO","UNIDADE"], var_name='year_month', value_name='volume')

pivoted_df["year_month"] = pivoted_df.apply(lambda row: str_to_date(str(row['ANO']) + '-' + row["year_month"]), axis=1)
pivoted_df["created_at"] = pd.Timestamp.date(datetime.datetime.now())

pivoted_df.drop(columns=['ANO','REGIÃO'], inplace=True)

pivoted_df.columns = ['product','uf','unit','year_month','volume','created_at']

pivoted_df.to_csv(csv_path,index=False ,encoding='utf-8-sig')

