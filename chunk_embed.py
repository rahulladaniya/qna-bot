from typing import List
from scraper import obj_scrap_data
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from logger import Logger
import traceback

class embedding:
    def __init__(self):
        self.logger = Logger.get_logger(self.__class__.__name__) 

    def chunk_text(self,text, chunk_size= 500, chunk_overlap= 50):
            
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
            )
            return splitter.split_text(text)
        
        except Exception as e:
            e=traceback.format_exc()
            self.logger.error(f"Error Occured: {e}")

    def embed_and_store(self,urls, faiss_index_path= "vector.index"):
            
        try:
            self.logger.info(f"Input Urls {urls}")
            
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

            all_texts = []
            all_metadatas = []

            for url in urls:
    
                text = obj_scrap_data.scrape_url(url)
                if not text:
                    self.logger.info(f"Skipping url: {url}, no text found")
                    continue

                chunks = self.chunk_text(text)
                self.logger.info(f"Length of chunks generated: {len(chunks)}")

                all_texts.extend(chunks)
                all_metadatas.extend([{"source_url": url}] * len(chunks))

            if not all_texts:
                self.logger.error("No data to embed/store.")
                return
            
            self.logger.info(f"All Text: {all_texts}")
            self.logger.info(f"All metadata: {all_metadatas}")

            self.logger.info("Embeddings and Store")
            vectordb = FAISS.from_texts(all_texts, embeddings, metadatas=all_metadatas)

            vectordb.save_local(faiss_index_path)
            self.logger.info(f"Vector store saved to: {faiss_index_path}")

        except Exception as e:
            e=traceback.format_exc()
            self.logger.error(f"Error Occured: {e}")


obj_embeddings=embedding()

# if __name__ == "__main__":
#     # Example usage
#     urls = [
#         "https://www.freepressjournal.in/sports/itne-toh-virat-bhai-ke-paas-bhi-nahin-hain-nitish-rana-vaibhav-suryavanshi-engage-in-hilarious-chat-after-rr-vs-mi-ipl-2025-match-video",
#         "https://en.wikipedia.org/wiki/Vaibhav_Suryavanshi"
#         # Add more URLs as needed
#     ]
#     embed_and_store(urls)