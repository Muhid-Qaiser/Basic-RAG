from langchain.prompts import ChatPromptTemplate
from prompts import PROMPT_TEMPLATE


CHROMA_PATH = "chroma"
DATA_PATH = "documents\\"


def predict(model, query_text, db):

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=4)

    if len(results) == 0 or results[0][1] < 0.2:
        return f"Unable to find matching results."

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # model = ChatOpenAI()
    response_text = model.invoke(prompt)    

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"{response_text.content}"
    return formatted_response





