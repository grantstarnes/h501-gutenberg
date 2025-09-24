# importing pandas
import pandas as pd

# Getting the contents of the data_sources.py file in my tt_gutenberg module, and importing my get_urls function
from tt_gutenberg.data_sources import get_urls

# Calling the get_urls function to assign the three URLs to variables
authors, languages, metadata = get_urls()

def list_authors(by_languages=True, alias=True):
    '''
    This function first takes the csv files from the three URLs and loads them into pandas dataframes.
    Then, it merges the dataframes in two steps: first merging metadata and languages on "gutenberg_id",
    and then merging the resulting dataframe with authors on "gutenberg_author_id".
    Finally, it groups the merged dataframe by "alias", sums the "total_languages" for each author, sorts the authors
    in descending order based on the summed "total_languages", and returns a list of author aliases.
    '''

    authors_df = pd.read_csv(authors)
    languages_df = pd.read_csv(languages)
    metadata_df = pd.read_csv(metadata)

    meta_lang = pd.merge(metadata_df, languages_df, on="gutenberg_id", how="inner")

    full_df = pd.merge(meta_lang, authors_df, on="gutenberg_author_id", how="inner")

    sorted_authors = (
        full_df.groupby("alias")["total_languages"]
        .sum()
        .sort_values(ascending=False)
    )

    return sorted_authors.index.tolist()