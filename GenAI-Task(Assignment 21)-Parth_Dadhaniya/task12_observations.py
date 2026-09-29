# Task 12: Observations & Insights
# Author: Parth Dadhaniya

print("=" * 65)
print("Task 12: Observations & Insights on Loaders and Text Splitters")
print("=" * 65)

print("\n1. Which loader is used for which data type?")
print("-" * 55)
print("""- Plain Text (.txt, .log):
  TextLoader: Loads the entire text file into a single Document object with source metadata.

- Tabular Data (.csv):
  CSVLoader: Converts each row into a distinct Document object with column headers
  formatted as key-value pairs. Ideal for structured row-level retrieval.

- PDF Documents (.pdf):
  PyPDFLoader: Extracts text page by page, preserving page numbers in metadata ('page': 0, 1...).
  Essential for multi-page documents where page citations are required.

- Folders / Collections:
  DirectoryLoader: Recursively scans a directory with glob patterns and delegates to
  specialized loaders based on file extensions.

- Webpages (.html, online docs):
  WebBaseLoader: Uses BeautifulSoup to fetch HTML web content and extract clean,
  human-readable text from blogs, documentation, and articles.""")

print("\n2. Best splitter for each data type:")
print("-" * 55)
print("""- Small Text (Short notes, single paragraphs, tweets):
  Best Splitter: CharacterTextSplitter or simple sentence splitting.
  Reason: The text is already short, so simple delimiter-based splitting or keeping
  the entire document intact avoids over-fragmentation.

- Large PDFs (Research papers, books, manuals, legal documents):
  Best Splitter: PyPDFLoader (page-based) + RecursiveCharacterTextSplitter.
  Reason: Preserves page numbers in metadata for citations while recursively splitting
  long pages on paragraph and sentence boundaries, avoiding cutoffs inside tables or sentences.

- Web Data (HTML articles, documentation pages, blogs):
  Best Splitter: RecursiveCharacterTextSplitter or HTMLHeaderTextSplitter / MarkdownHeaderTextSplitter.
  Reason: Web pages have nested structures (headers <h1>-<h3>, sections, paragraphs).
  Hierarchical splitters preserve header context in metadata, ensuring navigation menus
  and main content are properly compartmentalized.""")

print("\n3. Why chunk overlap is important?")
print("-" * 55)
print("""- Context Continuity Across Boundaries:
  When a document is split strictly at fixed character boundaries, an important
  sentence or idea may get sliced in half. Overlap ensures adjacent chunks share
  boundary text, preserving the full thought in at least one chunk.

- Semantic Retrieval Precision:
  If a user asks a question whose answer bridges the end of paragraph 1 and the
  beginning of paragraph 2, zero overlap causes neither chunk to have the complete
  answer. Overlap guarantees the boundary context is captured in the vector search.

- Mitigates Hallucinations:
  Providing the LLM with complete contextual sentences rather than fragmented phrases
  leads to more grounded and accurate generation.""")
