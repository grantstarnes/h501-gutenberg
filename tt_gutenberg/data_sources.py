def get_urls():
    """
    Returns the three Gutenberg dataset URLs and sets assigns them to variables (authors, languages, and metadata).
    """
    
    authors = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    languages = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
    metadata = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"

    return authors, languages, metadata