import streamlit as st
import pandas as pd
import os
from PIL import Image
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
file_path4 = os.path.join(os.getcwd(), 'Kazu_message.xlsx')
file_path5 = os.path.join(os.getcwd(), 'Tama_message.xlsx')
file_path6 = os.path.join(os.getcwd(), 'Kazu_prompt.xlsx')
file_path7 = os.path.join(os.getcwd(), 'Tama_prompt.xlsx')

st.title('Kazutama-net アプリ')

st.header('SN：KZ012312X0006　USER：里中 耕也　USER No：1',divider='rainbow')

st.write('測定コード')

# df1 = pd.read_excel(r'C:\Users\jcnw\.streamlit\Sokutei_code.xlsx',sheet_name='Sokutei_code')

df1 = pd.read_excel(file_path1,sheet_name='Sokutei_code')

# データフレーム内のすべての日時列を日付のみに変換
for column in df1.select_dtypes(include=['datetime64[ns]', 'datetime']):
    df1[column] = pd.to_datetime(df1[column]).dt.date

# 数字の区切り点を表示しないようにフォーマットを適用
df1['測定コード'] = df1['測定コード'].map('{:.0f}'.format)

st.data_editor(df1, height=300)

col8, col9 = st.columns(2)

with col8:
    st.button('ファイルに保存')
with col9:
    st.button('削除')


st.write('測定コード統計')

# df2 = pd.read_excel(r'C:\Users\jcnw\.streamlit\Statics_code.xlsx',sheet_name='Statics_code')

df2 = pd.read_excel(file_path2,sheet_name='Statics_code')

# 数字の区切り点を表示しないようにフォーマットを適用
df2['測定コード'] = df2['測定コード'].map('{:.0f}'.format)

img = Image.open("グラフ１.jpg")

col10, col11 = st.columns(2)

with col10:
    st.data_editor(df2, height=300)

with col11:
    st.image(img)

col1, col2, col3 = st.columns(3)

with col1:
    st.button('メッセージ生成')
with col2:
    st.button('印刷')
with col3:
    st.button('機器操作')

st.write('かずちゃんメッセージ')

df4 = pd.read_excel(file_path4,sheet_name='AImessage')

st.table(df4)

col4, col5 = st.columns(2)

with col4:
    st.button('かずちゃん音声読み上げ')
with col5:
    st.button('かずちゃんチャット')

st.write('たまちゃんメッセージ')

df5 = pd.read_excel(file_path5,sheet_name='AImessage')

st.table(df5)

col6, col7 = st.columns(2)

with col6:
    st.button('たまちゃん音声読み上げ')
with col7:
    st.button('たまちゃんチャット')

st.sidebar.write('## 検索条件選択')

st.sidebar.selectbox('測定メニュー選択',['貴男のメンタル','貴女のメンタル','愛犬のメンタル','愛猫のメンタル','家・車等のエネルギー調整','人間関係全般','人間関係（家族）','人間関係（我が子）','人間関係（義父母）','人間関係（義理の兄弟姉妹）','人間関係（現在の恋人）','人間関係（昔の恋人）','人間関係（友人・仲間）','人間関係（社長・上司）','人間関係（同僚）','人間関係（部下）','人間関係（社員・従業員）','人間関係（配偶者）','すべて'])

st.sidebar.selectbox('測定モード選択',['すべて','エーテルモード','アストラルモード'])

st.sidebar.radio('検索期間', ('最新','期間選択','すべて'))

st.sidebar.selectbox('始点',['2025/5/10','2025/5/12','2025/5/15','2025/5/18','2025/5/20','2025/5/25','2025/5/30','2025/6/1','2025/6/10','2025/6/13','2025/6/15','2025/6/18','2025/6/20','2025/6/22','2025/6/25','2025/6/28','2025/6/30'])

st.sidebar.selectbox('終点',['2025/5/10','2025/5/12','2025/5/15','2025/5/18','2025/5/20','2025/5/25','2025/5/30','2025/6/1','2025/6/10','2025/6/13','2025/6/15','2025/6/18','2025/6/20','2025/6/22','2025/6/25','2025/6/28','2025/6/30'])

st.sidebar.button('更新')

st.sidebar.selectbox('メッセージタイプ',['スピリチュアル','フロイト心理学','ユング心理学','アドラー心理学','占星術','禅宗'])

st.sidebar.selectbox('LLM',['Amazon Titan','Claude','AI21 Jurassic','Cohere','ChatGPT','GEMINI'])

st.sidebar.button('メッセージ更新')

st.sidebar.write('かずちゃんへの指示')

df6 = pd.read_excel(file_path6,sheet_name='AImessage')

st.sidebar.table(df6)

st.sidebar.button('かずちゃんメッセージ生成')

st.sidebar.write('たまちゃんへの指示')

df7 = pd.read_excel(file_path7,sheet_name='AImessage')

st.sidebar.table(df7)

st.sidebar.button('たまちゃんメッセージ生成')