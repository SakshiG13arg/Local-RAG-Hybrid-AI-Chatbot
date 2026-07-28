from ddgs import DDGS


def search_web(
    query: str,
    max_results: int = 3
) -> list:
    """
    Searches the web using DuckDuckGo.
    """

    results = []

    try:

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for result in search_results:

                results.append(
                    {
                        "title": result["title"],
                        "body": result["body"],
                        "href": result["href"]
                    }
                )

    except Exception as e:

        print("\n========== WEB SEARCH ERROR ==========")
        print(e)
        print("======================================\n")

    return results