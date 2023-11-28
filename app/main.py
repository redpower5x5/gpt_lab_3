import streamlit as st
from streamlit_option_menu import option_menu
from gptModel import MyModel
from genShortText import short_text
from genLongText import long_text

page_names_to_funcs = {
    "Генерация короткого текста": short_text,
    "Генерация длинного текста": long_text,
}

model = MyModel()

with st.sidebar:
    selected = option_menu("Лаба.3", ["Генерация короткого текста", 'Генерация длинного текста'],
        icons=['table', 'file-earmark-lock'], menu_icon="cast", default_index=0)
page_names_to_funcs[selected](model)