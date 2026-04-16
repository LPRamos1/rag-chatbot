from chatbot import stream_response
from vector_store import create_collection, add_documents, query_documents
from data.sample_data import data


def main():
    """
    Main RAG chatbot loop.
    """
    collection = create_collection()
    add_documents(collection, data)

    print("Chatbot RAG System: Type 'exit' to stop\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        # Retrieve relevant documents (RAG context)
        results = query_documents(collection, user_input, n_results=3)
        documents = results.get("documents", [])

        if not documents or not documents[0]:
            context_text = "No context found"
        else:
            # Join multiple retrieved chunks (better RAG)
            context_text = "\n".join(documents[0])

        print("Chatbot: ", end="", flush=True)

        # Build prompt with context
        messages = [
            {
                "role": "system",
                "content": "You are a technical support assistant.\n "
                "Answer the user in a clear and direct way.\n "
                "Use only the provided context.\n"
                "If the context is not enough, say you don't know.\n\n"
                f"Context:\n{context_text}",
            },
            {"role": "user", "content": user_input},
        ]

        stream_response(messages)
        print()


if __name__ == "__main__":
    main()
