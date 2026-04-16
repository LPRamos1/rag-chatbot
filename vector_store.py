import chromadb


def create_collection():
    """
    Initializes and returns a persistent ChromaDB collection.
    """
    client = chromadb.PersistentClient(path="./db")
    return client.get_or_create_collection(name="support_knowledge_base")


def add_documents(collection, data):
    """
    Adds documents and metadata to the collection.

    Args:
        collection: ChromaDB collection
        data (list): List of dictionaries with 'text' and 'id'
    """
    collection.add(
        documents=[item["text"] for item in data],
        ids=[str(i) for i in range(len(data))],
        metadatas=[{"source": item["id"]} for item in data],
    )


def query_documents(collection, query_text, n_results=1):
    """
    Queries the vector database for similar documents.

    Args:
        collection: ChromaDB collection
        query_text (str): User query
        category_filter (str, optional): Metadata filter

    Returns:
        dict: Query results
    """
    return collection.query(
        query_texts=[query_text],
        n_results=n_results,
    )
