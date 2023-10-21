import streamlit as st
import graphviz
import matplotlib

st.warning("... goodbye world")
st.table(dir(graphviz.Digraph))

dg = graphviz.Digraph()

for (u,d) in [(1,2), (1,3), (2,3), (1,4), (2,4)]:
    dg.edge(str(u), str(d))

st.graphviz_chart(dag)
