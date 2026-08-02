import fitz


def read_pdf(file_path):
    """
    Reads a PDF and returns a list of dictionaries:
    [
        {
            "page": 1,
            "text": "..."
        }
    ]
    """

    document = fitz.open(file_path)

    pages = []

    for page_number in range(len(document)):

        page = document.load_page(page_number)

        text = page.get_text()

        pages.append(
            {
                "page": page_number + 1,
                "text": text
            }
        )

    document.close()

    return pages