import streamlit as st
import graphviz
import matplotlib

st.warning("... goodbye world")
st.table(dir(graphviz))

dg = graphviz.Digraph()
st.write(help(dg.edge))

#for (u,d) in [(1,2), (1,3), (2,3), (1,4), (2,4)]:
#    dg.edge((u, d))

#st.graphviz_chart(dag)
