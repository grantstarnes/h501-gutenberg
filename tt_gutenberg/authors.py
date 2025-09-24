import pandas as pd

from tt_gutenberg.data_sources import get_urls

authors, languages, metadata = get_urls()

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