import streamlit as st
import pandas as pd
import openpyxl

# 簡単なExcelデータの表示
st.title('Sample Streamlit App')
df = pd.DataFrame({
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6]
})
st.write(df)
