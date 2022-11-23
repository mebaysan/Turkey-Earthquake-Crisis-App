"""
# Introduction

I've created this repo to present a minimal crisis map for earhquakes in Turkey.

"""

import streamlit as st
import pandas as pd
from scrapers.rasathane import get_json_data

eq_data = pd.DataFrame(get_json_data())

st.write(eq_data)