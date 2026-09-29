# Task 5: WebBase Loader
# Author: Parth Dadhaniya

import os
import warnings
warnings.filterwarnings("ignore")

os.environ["USER_AGENT"] = "PersonalKnowledgeAssistant/1.0"

from langchain_community.document_loaders import WebBaseLoader

# loading public webpage (Wikipedia: Artificial intelligence)
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
print(f"Loading webpage from: {url}")

loader = WebBaseLoader(url)
docs = loader.load()

print("\nDocuments loaded:", len(docs))
print("Page Title:", docs[0].metadata.get("title"))
print("Source URL:", docs[0].metadata.get("source"))

# clean up whitespace for clear display
clean_content = " ".join(docs[0].page_content.split())
print("\nFirst 500 characters extracted from webpage:")
print(clean_content[:500])

print("\nUse Case in Personal Knowledge Assistant:")
print("- Ingesting live API documentation, support blogs, or public release notes")
print("- Keeps knowledge base up-to-date with external web sources")
