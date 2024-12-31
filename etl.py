# I want to show task & status o/p in table format

import streamlit as st
import pandas as pd 
data = {
        'Task': ['Extract', 'Transfer', 'Load'],
         'Status': ['Completed','Inprogress','Pending']
    }
df = pd.DataFrame(data)
st.write('ETL pipline execution status1')
st.write(df)