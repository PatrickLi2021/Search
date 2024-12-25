import pytest
from index import *


def test_parse_xml_1():
    """ Tests to see if each of the following dictionaries are properly 
        populated in the parse_xml function using DocProcessingExample1.

        This XML file contains a mixture of links in the [[...|...]], [[...]], 
        and meta links formats as well as links to pages outside of the corpus
    """

    indexer_1 = Index("DocProcessingExample1.xml", "a", "b", "c")
    ids_to_titles = {"1": "Liverpool", "2": "Manchester City", "3": "EPL"}
    titles_to_ids = {"Liverpool": "1", "Manchester City": "2", "EPL": "3"}
    page_to_links = {"1": ["Manchester City", "EPL"], "2": ["EPL"],
                     "3": ["Manchester City", "Liverpool"]}
    assert ids_to_titles == indexer_1.id_to_title
    assert titles_to_ids == indexer_1.title_to_id
    assert page_to_links == indexer_1.page_to_links


def test_parse_xml_2():
    """ Tests to see if each of the following dictionaries are properly 
        populated in the parse_xml function using DocProcessingExample2

        This XML file contains is a larger file with 12 unique pages where the 
        pages contain different link types. Some pages only contain links to 
        pages outside the corpus while others contains links to other pages in 
        the corpus"""

    indexer_1 = Index("DocProcessingExample2.xml", "a", "b", "c")
    ids_to_titles = {"1": "Philadelphia 76ers", "2": "Raptors", "3": "Celtics",
                     "4": "New York Knicks", "5": "Brooklyn Nets",
                     "6": "Scottie Barnes", "7": "Pascal Siakam",
                     "8": "Fred VanVleet", "9": "Joel Embiid",
                     "10": "Tobias Harris",
                     "11": "National Basketball Association",
                     "12": "Category: Basketball (sport)"}
    titles_to_ids = {"Philadelphia 76ers": "1", "Raptors": "2", "Celtics": "3",
                     "New York Knicks": "4", "Brooklyn Nets": "5",
                     "Scottie Barnes": "6", "Pascal Siakam": "7",
                     "Fred VanVleet": "8", "Joel Embiid": "9", "Tobias Harris":
                     "10",
                     "National Basketball Association": "11",
                     "Category: Basketball (sport)": "12"}
    page_to_links = {"1": ["Brooklyn Nets", "New York Knicks",
                           "Raptors", "Celtics", "Tobias Harris", "Joel Embiid",
                           "National Basketball Association",
                           "Category: Basketball (sport)"],
                     "2": ["Fred VanVleet", "Pascal Siakam", "Scottie Barnes",
                           "National Basketball Association"],
                     "3": ["National Basketball Association"],
                     "4": ["National Basketball Association"],
                     "5": ["Philadelphia 76ers", "Raptors", "Celtics",
                           "New York Knicks", "Scottie Barnes", "Pascal Siakam",
                           "Fred VanVleet", "Joel Embiid", "Tobias Harris",
                           "National Basketball Association",
                           "Category: Basketball (sport)"], "6": ["Raptors"],
                     "7": ["Raptors"], "8": ["Raptors"],
                     "9": ["Philadelphia 76ers"],
                     "10": ["Philadelphia 76ers"],
                     "11": ["Philadelphia 76ers", "Raptors", "Celtics",
                            "New York Knicks", "Brooklyn Nets",
                            "Scottie Barnes", "Pascal Siakam", "Fred VanVleet",
                            "Joel Embiid", "Tobias Harris",
                            "Category: Basketball (sport)"],
                     "12": ["National Basketball Association"]}
    assert ids_to_titles == indexer_1.id_to_title
    assert titles_to_ids == indexer_1.title_to_id
    assert page_to_links == indexer_1.page_to_links


def test_parse_xml_3():
    """ Tests to see if each of the following dictionaries are properly 
        populated in the parse_xml function using DocProcessingExample3

        This XML file is rather simple and only contains 4 different pages. Two 
        of the pages contain links while the other 2 contain only text"""

    indexer_1 = Index("DocProcessingExample3.xml", "a", "b", "c")
    ids_to_titles = {"1": "Cats", "2": "Dogs", "3": "Mice", "4": "Rabbits"}
    titles_to_ids = {"Cats": "1", "Dogs": "2", "Mice": "3", "Rabbits": "4"}
    page_to_links = {"1": ["Dogs"], "2": ["Cats", "Mice", "Rabbits"], "3": [
        "Cats", "Dogs", "Rabbits"], "4": ["Cats", "Dogs", "Mice"]}
    assert ids_to_titles == indexer_1.id_to_title
    assert titles_to_ids == indexer_1.title_to_id
    assert page_to_links == indexer_1.page_to_links


def test_stem_stop():
    """Testing the stem_stop function in index.py"""

    # Running stem_stop on an empty list of words
    indexer_1 = Index("DocProcessingExample1.xml", "a", "b", "c")
    list_1 = []
    assert [] == indexer_1.stem_stop(list_1)

    # Testing if -ing words are stemmed properly
    indexer_1 = Index("DocProcessingExample1.xml", "a", "b", "c")
    list_1 = ["running", "jumping", "eating"]
    list_2 = ["run", "jump", "eat"]
    assert list_2 == indexer_1.stem_stop(list_1)

    # Testing to see if all words in a list containing stop words are removed
    indexer_1 = Index("DocProcessingExample1.xml", "a", "b", "c")
    list_1 = ["is", "they", "it", "a", "an", "and", "the", "in"]
    assert [] == indexer_1.stem_stop(list_1)

    # Testing a mixture of stop words and words that should be stemmed
    indexer_1 = Index("DocProcessingExample1.xml", "a", "b", "c")
    list_1 = ["Brown", "University", "located", "in", "Providence", "Rhode",
              "Island"]
    list_2 = ["brown", "univers", "locat", "provid", "rhode", "island"]
    assert list_2 == indexer_1.stem_stop(list_1)

    # Testing mixture of different types of words in all capital letters
    indexer_1 = Index("DocProcessingExample1.xml", "a", "b", "c")
    list_1 = ["THE", "EAST", "COAST", "HAS", "VERY", "COLD", "TEMPERATURES",
              "IN", "WINTER"]
    print(indexer_1.stem_stop(list_1))
    list_2 = ["east", "coast", "cold", "temperatur", "winter"]
    assert list_2 == indexer_1.stem_stop(list_1)

# Testing to see if invalid filepath argument into index is caught
# (picture of test output in README)
def test_file_not_found_error():
    def test_my_func():
        with pytest.raises(FileNotFoundError) as message:
            message = Index("FakeFile.xml", "a", "b", "c")
            assert "File was not found" in str(message)