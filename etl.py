# I want to show task & status o/p in table format

import pandas as pd
import streamlit as st

st.write('AVD')
data = {
        'Task': ['Extract', 'Transfer', 'Load'],
         'Status': ['Completed','Inprogress','Pending']
    }
df = pd.DataFrame(data)
st.write('ETL pipline execution status1:', df)
