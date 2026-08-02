import os


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_uploaded_file(uploaded_file):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    if not os.path.exists(filepath):

        with open(filepath, "wb") as f:

            f.write(uploaded_file.getbuffer())

    return filepath