import streamlit as st

st.set_page_config(
    page_title="Clubes de Ciencia",
    page_icon="🔬",
    layout="centered",
)

st.header("Putting the black box to the test: Can AI diagnose cancer?")

st.write("This page will help us to store all the content that we'll see these days! " \
"Below you will find tabs with the content of every day, including notebooks and" \
" slides")

st.write("This is the repository where everything will be added, in case you want to save it")

st.link_button("Open in github", "https://github.com/ZaidDeAnda/CdeC2026-blackbox/tree/main")

st.divider()

tabs = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])

tabs[0].subheader("Python crash course part 1")

tabs[0].link_button("Notebook", "https://githubtocolab.com/ZaidDeAnda/CdeC2026-blackbox/blob/main/notebooks/python-day1.ipynb")

tabs[1].write("WIP")

tabs[2].write("WIP")

tabs[3].write("WIP")

tabs[4].write("WIP")