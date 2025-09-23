import pandas as pd

authors = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
languages = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
metadata = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"

def list_authors(by_languages=True, alias=True):
    # Load data
    authors_df = pd.read_csv(authors)
    languages_df = pd.read_csv(languages)
    metadata_df = pd.read_csv(metadata)

    # Merge step 1: metadata ↔ languages
    meta_lang = pd.merge(metadata_df, languages_df, on="gutenberg_id", how="inner")

    # Merge step 2: add authors
    full_df = pd.merge(meta_lang, authors_df, on="gutenberg_author_id", how="inner")

    # Group and sort
    sorted_authors = (
        full_df.groupby("alias")["total_languages"]
        .sum()
        .sort_values(ascending=False)
    )

    return sorted_authors.index.tolist()