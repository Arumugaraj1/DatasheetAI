from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(pages):
    """
    pages:
    [
        {
            "page":1,
            "text":"...."
        }
    ]
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = []

    for page in pages:

        texts = splitter.split_text(page["text"])

        for text in texts:

            chunks.append(
                {
                    "page": page["page"],
                    "text": text
                }
            )

    return chunks