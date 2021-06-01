import streamlit as st

import os

#import re
#import logging
#import requests

#code = """<!-- Global site tag (gtag.js) - Google Analytics -->
#<script async src="https://www.googletagmanager.com/gtag/js?id=UA-197317436-1"></script>
#<script>
#  window.dataLayer = window.dataLayer || [];
#  function gtag(){dataLayer.push(arguments);}
#  gtag('js', new Date());
#  gtag('config', 'UA-197317436-1');
#</script>"""

#st.title("This is my site")
#sentence = st.text_input('Entrer votre phrase ici... svp')

#logging.warning(sentence)

#if st.button("Bonjour Je suis LE Bouton"):
#    req = requests.get("https://analytics.google.com/analytics/web/#/report-home/a197317436w272866964p243204955")
#    st.text(req.status_code)
#    st.markdown(req.text)
#else:
#    st.write('Goodbye')

from pytrends.request import TrendReq

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['Ramen','Soba'])

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
st.line_chart(interest_over_time_df)

# Interest by Region
#interest_by_region_df = pytrend.interest_by_region()
#st.text(interest_by_region_df)
# Related Queries, returns a dictionary of dataframes
#related_queries_dict = pytrend.related_queries()

# Get Google Hot Trends data
#trending_searches_df = pytrend.trending_searches()

# Get Google Hot Trends data
#today_searches_df = pytrend.today_searches()

# Get Google Top Charts
#top_charts_df = pytrend.top_charts(2018, hl='en-US', tz=300, geo='GLOBAL')
#st.title(top_charts_df.head())

# Get Google Keyword Suggestions
#suggestions_dict = pytrend.suggestions(keyword='pizza')
