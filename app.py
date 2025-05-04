import streamlit as st
from chunk_embed import obj_embeddings
from answer import obj_answer

def main():
    st.title("Web Content Q&A Tool")

    urls_input = st.text_area("Input one or more URLs (one per line):")
    embed_clicked = st.button("Ingest URL Content")

    # Split input into list of URLs
    urls = [u.strip() for u in urls_input.splitlines() if u.strip()]

    if embed_clicked and urls:
        with st.spinner("Scraping and embedding..."):
            obj_embeddings.embed_and_store(urls)
        st.success("Content ingested. Now ask a question.")

    # Only load the vector store after embedding or if vector.index exists
    question = st.text_input("Ask a question about your ingested web content:")
    answer_clicked = st.button("Get Answer")

    if answer_clicked and question:
        with st.spinner("Retrieving answer..."):
            vectordb = obj_answer.load_vector_store()
            context = obj_answer.retrieve_context(question, vectordb, k=10)
            if context:
                st.subheader("Answer")
                answer = obj_answer.generate_answer(question, context)
                st.write(answer)
            else:
                st.write("No relevant content found.")

if __name__ == "__main__":
    main()