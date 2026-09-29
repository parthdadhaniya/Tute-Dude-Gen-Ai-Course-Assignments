# Task 7: Load YouTube Video Content
# Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")
import config

from langchain_community.document_loaders import YoutubeLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("--- Task 7: Load YouTube Video Content ---")

# Andrej Karpathy: Intro to Large Language Models
video_url = "https://www.youtube.com/watch?v=kCc8FmEb1nY"
print("Video URL:", video_url)

try:
    print("Fetching live transcript from YouTube...")
    loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=False)
    docs = loader.load()
    print("Live transcript loaded successfully!")
except Exception as e:
    print("Could not fetch live transcript, loading from local backup:", e)
    loader = TextLoader("data/youtube_transcript.txt", encoding="utf-8")
    docs = loader.load()

print(f"Total transcript length: {len(docs[0].page_content)} characters")

# split transcript into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=40)
chunks = splitter.split_documents(docs)

print(f"Total chunks created: {len(chunks)}")
print("\nFirst chunk preview:")
print(chunks[0].page_content.strip())
