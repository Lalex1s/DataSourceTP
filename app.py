import streamlit as st
import os
import re
import logging 


code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-197317436-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-197317436-1');
</script>"""

st.title("This is my site")
sentence = st.text_input('Entrer votre phrase ici... svp')

logging.warning(sentence)
