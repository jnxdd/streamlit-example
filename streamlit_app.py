from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

# example
components.html('''
<style>
mash-donate-button::part(button-solid){
    margin-left: 260px;
    margin-top: 260px;
}
</style>
  <script>
    window.MashSettings = {
      id: "dd9f18f3-6539-4967-97bc-de1b6bac7b7c"
    };
    var loader = function () {
      window.Mash.init();
    };
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.defer = true;
    script.onload = loader;
    script.src = "https://app.mash.com/sdk/sdk.js";
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(script);
  </script>
  <mash-donate-button handle="my-handle" mode="all" button-size="md" button-variant="solid">
  </mash-donate-button>
''', height=900, width=450)

st.markdown(
    """
    <style>
        iframe[width="400"] {
            position: fixed;
            bottom: 0px;
            right: 20px;
        } 
    </style>
    """,
    unsafe_allow_html=True,
)
