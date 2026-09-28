import requests

def fetch_book_from_openlibrary(isbn: str):
    try:
        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
        res = requests.get(url, timeout=10)

        # Don't use raise_for_status() - handle it yourself
        if res.status_code!= 200:
            # Return None so main.py can give fallback, not 500
            print(f"OpenLibrary status {res.status_code} for {isbn}")
            return None

        data = res.json()
        key = f"ISBN:{isbn}"
        if key not in data or not data[key]:
            print(f"ISBN {isbn} not found in Open Library")
            return None

        book_data = data[key]

        return {
            "isbn": isbn,
            "title": book_data.get("title"),
            "author": ", ".join([a["name"] for a in book_data.get("authors", [])]),
            "pages": book_data.get("number_of_pages"),
            "publisher": book_data.get("publishers", [{}])[0].get("name") if book_data.get("publishers") else "Unknown",
            "published_date": book_data.get("publish_date"),
            "source": "OpenLibrary Live"
        }
    except Exception as e:
        print(f"External API failed: {e}")
        return None