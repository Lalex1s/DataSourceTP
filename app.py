import streamlit as st
import os
import re

code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-197317436-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-197317436-1');
</script>"""

a=os.path.dirname(st.__file__) + '/static/index.html'
with open(a, 'r') as f:
    data=f.read()
    if len(re.findall('UA-', data)) == 0:
        with open(a, 'w') as f:
            newdata=re.sub('<head>','<head>' + code, data)
            f.write(newdata)

import streamlit.components.v1 as components

_radio_button = components.declare_component(
    "radio_button", url="http://localhost:3001",
)


def custom_radio_button(label, options, default, key=None):
    return _radio_button(label=label, options=options, default=default, key=key)


result = custom_radio_button(
    "How many bats?",
    options=["one bat", "TWO bats", "THREE bats", "FOUR BATS! ah ah ah!"],
    default="one bat",
)
st.write("This many: %s" % result)
