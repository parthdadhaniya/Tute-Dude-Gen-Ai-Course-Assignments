# summarize_chains.py - Implementation of load_summarize_chain
# Student: Parth Dadhaniya

from langchain_core.prompts import PromptTemplate


class StuffChain:
    """Combines all input documents into a single prompt for summarization."""

    def __init__(self, llm):
        self.llm = llm
        self.prompt = PromptTemplate.from_template(
            "Write a concise summary of the following document:\n\n{text}\n\nSummary:"
        )

    def invoke(self, inputs):
        docs = inputs.get("input_documents", [])
        text = "\n\n".join([d.page_content if hasattr(d, "page_content") else str(d) for d in docs])
        chain = self.prompt | self.llm
        res = chain.invoke({"text": text})
        return {"output_text": res.content if hasattr(res, "content") else str(res)}


class MapReduceChain:
    """Summarizes each chunk individually (Map) then combines all summaries (Reduce)."""

    def __init__(self, llm):
        self.llm = llm
        self.map_prompt = PromptTemplate.from_template(
            "Summarize this chunk in 1-2 sentences:\n\n{chunk}\n\nChunk Summary:"
        )
        self.reduce_prompt = PromptTemplate.from_template(
            "Combine these chunk summaries into a cohesive final summary:\n\n{summaries}\n\nFinal Summary:"
        )

    def invoke(self, inputs):
        docs = inputs.get("input_documents", [])
        chunk_summaries = []
        map_chain = self.map_prompt | self.llm

        # 1. Map step: summarize each chunk
        for d in docs:
            chunk_text = d.page_content if hasattr(d, "page_content") else str(d)
            res = map_chain.invoke({"chunk": chunk_text})
            chunk_summaries.append(res.content if hasattr(res, "content") else str(res))

        # 2. Reduce step: combine all summaries
        reduce_chain = self.reduce_prompt | self.llm
        combined_text = "\n".join(chunk_summaries)
        res = reduce_chain.invoke({"summaries": combined_text})
        final_text = res.content if hasattr(res, "content") else str(res)

        return {
            "output_text": final_text,
            "intermediate_steps": chunk_summaries,
        }


class RefineChain:
    """Iteratively updates and refines the summary chunk by chunk."""

    def __init__(self, llm):
        self.llm = llm
        self.init_prompt = PromptTemplate.from_template(
            "Write an initial summary of this text:\n\n{text}\n\nSummary:"
        )
        self.refine_prompt = PromptTemplate.from_template(
            "Existing summary: {existing_summary}\n\nNew text: {new_chunk}\n\nRefined Summary:"
        )

    def invoke(self, inputs):
        docs = inputs.get("input_documents", [])
        if not docs:
            return {"output_text": ""}

        # 1. Initial summary of first chunk
        first_text = docs[0].page_content if hasattr(docs[0], "page_content") else str(docs[0])
        res = (self.init_prompt | self.llm).invoke({"text": first_text})
        current = res.content if hasattr(res, "content") else str(res)

        # 2. Refine with subsequent chunks
        refine_chain = self.refine_prompt | self.llm
        for d in docs[1:]:
            chunk_text = d.page_content if hasattr(d, "page_content") else str(d)
            res = refine_chain.invoke({"existing_summary": current, "new_chunk": chunk_text})
            current = res.content if hasattr(res, "content") else str(res)

        return {"output_text": current}


def load_summarize_chain(llm, chain_type="stuff"):
    """Creates a summarization chain matching LangChain's interface."""
    if chain_type == "stuff":
        return StuffChain(llm)
    elif chain_type == "map_reduce":
        return MapReduceChain(llm)
    elif chain_type == "refine":
        return RefineChain(llm)
    raise ValueError(f"Unknown chain_type: {chain_type}")
