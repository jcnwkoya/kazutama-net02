import streamlit as st
import pandas as pd
import os
_ = """
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'service_account3.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

SP_SHEET_KEY = '1qZLtO10hJXCE_vWKbhVReb_UCoefbHoKXQ6u7IxeA6I'
sh = gc.open_by_key(SP_SHEET_KEY)

SP_SHEET = '測定コード'
codesheet = sh.worksheet(SP_SHEET)

deta = codesheet.get_all_values()
df1 = pd.DataFrame(deta[1:],columns=deta[0])


SP_SHEET = '測定コード統計'
staticcode = sh.worksheet(SP_SHEET)

deta = staticcode.get_all_values()
df2 = pd.DataFrame(deta[1:],columns=deta[0])


SP_SHEET = 'AIメッセージ表示'
message = sh.worksheet(SP_SHEET)

deta = message.get_all_values()
df3 = pd.DataFrame(deta[2:3])
"""

# ファイルのパスを設定
file_path1 = os.path.join(os.getcwd(), 'Sokutei_code.xlsx')
file_path2 = os.path.join(os.getcwd(), 'Statics_code.xlsx')
file_path3 = os.path.join(os.getcwd(), 'AImessage.xlsx')

st.title('Kazutama-net サンプルアプリ')

st.header('SN：KZ012312X0006　USER：里中 耕也',divider='rainbow')

st.write('測定コード')

# df1 = pd.read_excel(r'C:\Users\jcnw\.streamlit\Sokutei_code.xlsx',sheet_name='Sokutei_code')

df1 = pd.read_excel(file_path1,sheet_name='Sokutei_code')

# データフレーム内のすべての日時列を日付のみに変換
for column in df1.select_dtypes(include=['datetime64[ns]', 'datetime']):
    df1[column] = pd.to_datetime(df1[column]).dt.date

# 数字の区切り点を表示しないようにフォーマットを適用
df1['測定コード'] = df1['測定コード'].map('{:.0f}'.format)

st.data_editor(df1, height=300)

st.write('測定コード統計')

# df2 = pd.read_excel(r'C:\Users\jcnw\.streamlit\Statics_code.xlsx',sheet_name='Statics_code')

df2 = pd.read_excel(file_path2,sheet_name='Statics_code')

# 数字の区切り点を表示しないようにフォーマットを適用
df2['測定コード'] = df2['測定コード'].map('{:.0f}'.format)

st.data_editor(df2, height=300)

st.write('カウンセリングメッセージ')

# st.write(df3)

# df3 = pd.read_excel(r'C:\Users\jcnw\.streamlit\AImessage.xlsx',sheet_name='AImessage')

df3 = pd.read_excel(file_path3,sheet_name='AImessage')

st.table(df3)

col1, col2, col3 = st.columns(3)

with col1:
    st.button('コード送信')
with col2:
    st.button('修正コード作成')
with col3:
    st.button('ヒーリング')


st.sidebar.write('## 検索条件選択')

st.sidebar.selectbox('測定メニュー選択',['すべて','貴男のメンタル','貴女のメンタル','愛犬のメンタル','愛猫のメンタル','家・車等のエネルギー調整','人間関係全般','人間関係（家族）','人間関係（我が子）','人間関係（義父母）','人間関係（義理の兄弟姉妹）','人間関係（現在の恋人）','人間関係（昔の恋人）','人間関係（友人・仲間）','人間関係（社長・上司）','人間関係（同僚）','人間関係（部下）','人間関係（社員・従業員）','人間関係（配偶者）'])

st.sidebar.selectbox('測定モード選択',['すべて','エーテルモード','アストラルモード'])

st.sidebar.radio('検索期間', ('すべて','最新','期間選択'))

st.sidebar.selectbox('始点',['2024/5/10','2024/5/12','2024/5/15','2024/5/18','2024/5/20','2024/5/25','2024/5/30','2024/6/1','2024/6/10','2024/6/13','2024/6/15','2024/6/18','2024/6/20','2024/6/22','2024/6/25','2024/6/28','2024/6/30'])

st.sidebar.selectbox('終点',['2024/5/10','2024/5/12','2024/5/15','2024/5/18','2024/5/20','2024/5/25','2024/5/30','2024/6/1','2024/6/10','2024/6/13','2024/6/15','2024/6/18','2024/6/20','2024/6/22','2024/6/25','2024/6/28','2024/6/30'])

st.sidebar.selectbox('メッセージタイプ',['スピリチュアル','フロイト心理学','ユング心理学','アドラー心理学','占星術','禅宗'])

st.sidebar.selectbox('LLM',['Amazon Titan','Claude','AI21 Jurassic','Cohere','ChatGPT','GEMINI'])

st.sidebar.button('更新')
