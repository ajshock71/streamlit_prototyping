import streamlit as st
import graphviz
import matplotlib

# import platform
# st.info(f"python version: {platform.python_version()}")

st.write("Generated from 'st.graphviz_chart(graphviz.Digraph)'")
dg = graphviz.Digraph()

for (u,d) in [(1,2), (1,3), (2,3), (1,4), (2,4)]:
    dg.edge(str(u), str(d))

st.graphviz_chart(dg)
