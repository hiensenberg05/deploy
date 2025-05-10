import streamlit as st
from rag2 import ask_question  # 👈 from your backend

st.set_page_config(page_title="WonderVector5000 QA", page_icon="🤖", layout="centered")

st.title("💬 Ask about the WonderVector5000!")
st.markdown("Ask anything about the fictional WonderVector5000 device. Answers powered by LLaMA3 + RAG.")

# User input
query = st.text_input("Type your question here 👇", placeholder="e.g., How do I start the WonderVector5000?")

# Answer display
if st.button("Ask") and query:
    with st.spinner("Thinking... 🤔"):
        try:
            answer, context = ask_question(query)
            st.success("Answer:")
            st.write(answer)

            with st.expander("Show Source Context"):
                for i, doc in enumerate(context):
                    st.markdown(f"**Chunk {i+1}:**")
                    st.markdown(doc.page_content)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
