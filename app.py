import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

# スプレッドシートに接続
conn = st.connection("gsheets", type=GSheetsConnection)

# データの読み込み
df = conn.read()

# タイムスタンプ列を日付型に変換
df['タイムスタンプ'] = pd.to_datetime(df['タイムスタンプ'])

# グラフの描画
st.title('環境データ可視化')

st.line_chart(df.set_index('タイムスタンプ')[['気温', '湿度', 'CO2濃度']])

# データテーブルの表示（オプション）
st.dataframe(df)

# 5分経ってから再実行
time.sleep(300)
st.experimental_rerun()