import streamlit as st
import pandas as pd
import os
# import openpyxl
file_path3 = os.path.join(os.getcwd(), 'AImessage.xlsx')
# 簡単なExcelデータの表示
st.title('Sample Streamlit App')
df = pd.DataFrame({
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6]
})
st.write(df)
df3 = pd.read_excel(file_path3,sheet_name='AImessage')
st.table(df3)
