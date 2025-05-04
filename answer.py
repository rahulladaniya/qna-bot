from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from logger import Logger
import traceback

class answer:
    
    def __init__(self):
        self.logger = Logger.get_logger(self.__class__.__name__) 

    def load_vector_store(self,faiss_index_path="vector.index"):
        try:
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vectordb = FAISS.load_local(faiss_index_path, embeddings, allow_dangerous_deserialization=True)
            self.logger.info(f"Vector Store Loaded Successfully")
            return vectordb
        except Exception as e:
            e=traceback.format_exc()
            self.logger.error(f"Error Occured: {e}")

    def retrieve_context(self,question, vectordb, k=5):
        try:

            docs_and_scores = vectordb.similarity_search_with_score(question, k=k)
            context = "\n".join([doc.page_content for doc, _ in docs_and_scores])
            self.logger.info(f"Context: {context}")
            return context
        except Exception as e:
            e=traceback.format_exc()
            self.logger.error(f"Error Occured: {e}")

    def generate_answer(self,question, context):
        try:
            self.logger.info(f"Input Question: {question}")
            self.logger.info(f"Input Context: {context}")
            llm = pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)
            prompt = (
                f"Answer the following question in detail, using only the context below. "
                f"Provide a comprehensive and informative response, combining all relevant points from the context. "
                f"Do not invent facts.\n\n"
                f"Context:\n{context}\n\n"
                f"Question: {question}\n\n"
                f"Detailed Answer:"
            )
            ans = llm(prompt)
            self.logger.info(f"Answer: {ans}")
            return ans[0]['generated_text'].strip()
        
        except Exception as e:
            e=traceback.format_exc()
            self.logger.error(f"Error Occured: {e}")

obj_answer=answer()