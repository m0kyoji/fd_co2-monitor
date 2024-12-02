import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# スプレッドシートに接続
conn = st.connection("gsheets", type=GSheetsConnection)

# データの読み込み
@st.cache_data(ttl=300)  # 5分間キャッシュ
def load_data():
    df = conn.read()
    df['タイムスタンプ'] = pd.to_datetime(df['タイムスタンプ'])
    return df

# データを取得
df = load_data()

# グラフの描画
st.title('環境データ可視化')

st.line_chart(df.set_index('タイムスタンプ')[['気温', '湿度', 'CO2濃度']])

# データテーブルの表示
st.dataframe(df)

# 更新ボタン
if st.button('データを更新'):
    st.cache_data.clear()
    st.experimental_rerun()