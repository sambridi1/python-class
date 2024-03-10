

import streamlit as st
import pandas as pd
# import streamlit as st
st.image('data:image/jpeg;base64,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[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', caption='Sunrise by the mountains')
st.write("hello darling")
