import streamlit as st
from gptModel import MyModel

def short_text(model: MyModel):
    st.title("Генерация короткого текста")
    st.write("Введите начало текста, а модель вам поможет продолжить")
    input_text = st.text_area("Введите текст", height=100, key='1', max_chars=1000)
    if st.button("Сгенерировать!"):
        with st.spinner("Генерация..."):
            result_text = model.gen_short_text(input_text)
            st.write("Результат: \n", result_text)
            st.success("Генерация завершена")
