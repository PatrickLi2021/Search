import pytest
from index import *

def test_term_frequency_1():
    """ 
    Testing a page that contains no links and has no stop words or stemming 
    involved.
    """

    indexer_1 = Index("tf_idf_example_1.xml", "a", "b", "c")
    dict1 = {"zero": {"0": 0.5*math.log(3, 10)}, "simmon": {"0": 0, "1": 0,
                                                            "2": 0},
             "dog": {"0": 0.5*math.log(1.5, 10), "1": math.log(1.5, 10)},
             "bit": {"0": 0.5*math.log(1.5, 10), "2": 0.5*math.log(1.5, 10)},
             "man": {"0": 0.5*math.log(3, 10)}, "first": {"1": math.log(3, 10)},
             "ate": {"1": math.log(3, 10)},
             "chees": {"1": math.log(1.5, 10), "2": math.log(1.5, 10)},
             "second": {"2": 0.5*math.log(3, 10)}}
    assert dict1 == indexer_1.words_to_ids_to_term_relevance

def test_term_frequency_2():
    """ 
    Testing a page in which all of the words in a page do NOT appear in any 
    other pages in the corpus
    """

    indexer_1 = Index("tf_idf_example_2.xml", "a", "b", "c")
    dict1 = {"soccer": {"1": (1.0/3) * math.log(3, 10)},
             "ronaldo": {"1": (1.0/3) * math.log(3, 10)},
             "messi": {"1": math.log(3, 10)},
             "salah": {"1": (2.0/3) * math.log(3, 10)},
             "mbapp": {"1": (2.0/3) * math.log(3, 10)},
             "haaland": {"1": (1.0/3) * math.log(3, 10)},
             "basketbal": {"2": 0.25 * math.log(3, 10)},
             "jame": {"2": 0.25 * math.log(3, 10)},
             "embiid": {"2": 0.75 * math.log(3, 10)},
             "durant": {"2": 0.25 * math.log(3, 10)},
             "irv": {"2": 0.5 * math.log(3, 10)},
             "jokic": {"2": math.log(3, 10)},
             "derozan": {"2": 0.5 * math.log(3, 10)},
             "booker": {"2": 0.75 * math.log(3, 10)},
             "footbal": {"3": 0.2 * math.log(3, 10)},
             "rodger": {"3": 0.4 * math.log(3, 10)},
             "bradi": {"3": 0.6 * math.log(3, 10)},
             "mahom": {"3": 0.4 * math.log(3, 10)},
             "jackson": {"3": 0.6 * math.log(3, 10)},
             "adam": {"3": 0.4 * math.log(3, 10)},
             "ertz": {"3": 0.4 * math.log(3, 10)},
             "murray": {"3": math.log(3, 10)}}
    assert dict1 == indexer_1.words_to_ids_to_term_relevance

def test_term_frequency_3():
    """
    Testing a corpus where each page has no links and a page has more than 1 
    occurrences of a particular word
    """

    i = Index("tf_idf_example_3.xml", "a", "b", "c")
    ids_to_titles = {"1": "How I Met Your Mother", "2": "Brooklyn 99",
                     "3": "Parks and Recreation"}
    titles_to_ids = {"How I Met Your Mother": "1", "Brooklyn 99": "2",
                     "Parks and Recreation": "3"}
    pg_to_links = {"1": ["Brooklyn 99", "Parks and Recreation"],
                   "2": ["How I Met Your Mother", "Parks and Recreation"],
                   "3": ["How I Met Your Mother", "Brooklyn 99"]}
    expected_term_relevances = {"met": {"1": math.log(3, 10)},
                                "mother": {"1": math.log(3, 10)},
                                "best": {"1": math.log(3, 10)},
                                "show": {"1": 0, "2": 0, "3": 0},
                                "brooklyn": {"2": 0.5*math.log(3, 10)},
                                "99": {"2": 0.5*math.log(3, 10)},
                                "also": {"2": 0.5*math.log(3, 10)},
                                "funni": {"2": math.log(1.5, 10),
                                          "3": math.log(3/2, 10)},
                                "park": {"3": math.log(3, 10)},
                                "recreat": {"3": math.log(3, 10)},
                                "anoth": {"3": math.log(3, 10)}}
    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance

def test_term_frequency_4():
    """
    Testing corpus where every page has only links that link out of corpus
    """

    i = Index("tf_idf_example_5.xml", "a", "b", "c")
    ids_to_titles = {"1": "Hello", "2": "bye", }
    titles_to_ids = {"Hello": "1", "bye": "2", }
    pg_to_links = {"1": ["bye"], "2": ["Hello"], }
    expected_term_relevances = {"hello": {"1": 0, "2": 0},
                                "interest": {"1": 0, "2": 0},
                                "word": {"1": 0, "2": 0},
                                "exampl": {"1": 0.5*math.log(2, 10)},
                                "look": {"1": 0.5*math.log(2, 10)},
                                "bye": {"2": math.log(2, 10)},
                                "also": {"2": 0.5*math.log(2, 10)},
                                "super": {"2": 0.5*math.log(2, 10)},
                                "mean": {"2": 0.5*math.log(2, 10)},
                                "someth": {"2": 0.5*math.log(2, 10)},
                                "differ": {"2": 0.5*math.log(2, 10)},
                                "instanc": {"2": 0.5*math.log(2, 10)},
                                "glanc": {"2": 0.5*math.log(2, 10)},
                                "page": {"2": 0.5*math.log(2, 10)},
                                "click": {"2": 0.5*math.log(2, 10)}
                                }
    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance

def test_term_frequency_5():
    """
    Testing a corpus with pages that link to themselves only
    """

    i = Index("tf_idf_example_6.xml", "a", "b", "c")
    ids_to_titles = {"1": "Patrick", "2": "Angela"}
    titles_to_ids = {"Patrick": "1", "Angela": "2"}
    pg_to_links = {"1": ["Angela"], "2": ["Patrick"]}
    expected_term_relevances = {"patrick": {"1": math.log(2, 10)},
                                "okay": {"1": 0.5*math.log(2, 10)},
                                "angela": {"2": math.log(2, 10)},
                                "fine": {"2": 0.5*math.log(2, 10)}}
    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance

def test_term_frequency_6():
    """
    Testing a corpus with one page with no links and all relevances are 0
    """

    i = Index("tf_idf_example_7.xml", "a", "b", "c")
    ids_to_titles = {"1": "TEST"}
    titles_to_ids = {"TEST": "1"}
    pg_to_links = {"1": []}
    expected_term_relevances = {"test": {"1": 0},
                                "link": {"1": 0},
                                "page": {"1": 0},
                                "anoth": {"1": 0},
                                "edg": {"1": 0},
                                "case": {"1": 0}}
    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance

def test_term_frequency_7():
    """
    Testing a corpus where each page links to itself and all other documents
    """

    i = Index("tf_idf_example_8.xml", "a", "b", "c")
    ids_to_titles = {"1": "EVERYTHING", "2": "OTHER"}
    titles_to_ids = {"EVERYTHING": "1", "OTHER": "2"}
    pg_to_links = {"1": ["OTHER"], "2": ["EVERYTHING"]}
    expected_term_relevances = {"everyth": {"1": 0, "2": 0},
                                "link": {"1": math.log(2, 10)},
                                "everi": {"1": 1/3*math.log(2, 10)},
                                "page": {"1": 0, "2": 0}}
    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance

def test_term_frequency_8():
    """
    Testing a corpus in which each page in the XMl only contains links that do
    NOT link to any other pages in the corpus
    """

    i = Index("tf_idf_example_9.xml", "a", "b", "c")
    ids_to_titles = {"1": "Brown University Information",
                     "2": "Brown Buildings"}
    titles_to_ids = {"Brown University Information": "1",
                     "Brown Buildings": "2"}
    pg_to_links = {"1": ["Brown Buildings"],
                   "2": ["Brown University Information"]}
    expected_term_relevances = {"brown": {"1": 0, "2": 0},
                                "univers": {"1": math.log(2, 10)},
                                "inform": {"1": 0, "2": 0},
                                "colleg": {"1": 0.5*math.log(2, 10)},
                                "specialti": {"1": 1/2*math.log(2, 10)},
                                "dean": {"1": math.log(2, 10)},
                                "exact": {"1": 1/2*math.log(2, 10)},
                                "locat": {"1": math.log(2, 10)},
                                "provost": {"1": 1/2*math.log(2, 10)},
                                "presid": {"1": 1/2*math.log(2, 10)},
                                "build": {"2": 1/3*math.log(2, 10)},
                                "von": {"2": 1/3*math.log(2, 10)},
                                "miller": {"2": math.log(2, 10)},
                                "metcalf": {"2": 1/3*math.log(2, 10)},
                                "dine": {"2": 1/3*math.log(2, 10)},
                                "hall": {"2": 1/3*math.log(2, 10)},
                                "center": {"2": 1/3*math.log(2, 10)},
                                "technolog": {"2": 1/3*math.log(2, 10)},
                                "vdub": {"2": 1/3*math.log(2, 10)},
                                "sharp": {"2":  1/3*math.log(2, 10)},
                                "refectori": {"2": 1/3*math.log(2, 10)}}
    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance

def test_term_frequency_9():
    """
    Testing a corpus in which each page in the XML contains links that ONLY 
    link to other pages in the corpus
    """

    i = Index("tf_idf_example_10.xml", "a", "b", "c")
    ids_to_titles = {"1": "Miami Heat", "2": "Charlotte Hornets",
                     "3": "Atlanta Hawks", "4": "Orlando Magic",
                     "5": "Dallas Mavericks"}
    titles_to_ids = {"Miami Heat": "1", "Charlotte Hornets": "2",
                     "Atlanta Hawks": "3", "Orlando Magic":
                     "4", "Dallas Mavericks": "5"}
    pg_to_links = {"1": ["Orlando Magic", "Charlotte Hornets", "Atlanta Hawks"],
                   "2": ["Orlando Magic", "Atlanta Hawks", "Miami Heat"],
                   "3": ["Orlando Magic", "Charlotte Hornets", "Miami Heat"],
                   "4": ["Charlotte Hornets", "Atlanta Hawks", "Miami Heat"],
                   "5": ["Charlotte Hornets", "Atlanta Hawks"]}
    expected_term_relevances = {"miami": {"1": 0.5*math.log(5/3, 10),
                                          "2": 0.5*math.log(5/3, 10),
                                          "4": math.log(5/3, 10)},
                                "heat": {"1": 0.5*math.log(5/4, 10),
                                         "2": 0.5*math.log(5/4, 10),
                                         "3": math.log(5/4, 10),
                                         "4": math.log(5/4, 10)},
                                "orlando": {"1": math.log(5/3, 10),
                                            "2": 0.5*math.log(5/3, 10),
                                            "4": 0.5*math.log(5/3, 10)},
                                "magic": {"1": math.log(5/4, 10),
                                          "2": 0.5*math.log(5/4, 10),
                                          "3": math.log(5/4, 10),
                                          "4": 0.5*math.log(5/4, 10)},
                                "charlott": {"1": 0.5*math.log(5/3, 10),
                                             "2": math.log(5/3, 10),
                                             "3": math.log(5/3, 10)},
                                "hornet": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0},
                                "atlanta": {"1": 0.5*math.log(5/4, 10),
                                            "3": math.log(5/4, 10),
                                            "4": 0.5*math.log(5/4, 10),
                                            "5": math.log(5/4, 10)},
                                "hawk": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0},
                                "dalla": {"5": math.log(5, 10)},
                                "maverick": {"5": math.log(5, 10)}}

    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance

def test_term_frequency_10():
    """
    Testing a corpus in which each page contains no text (only has titles)
    """

    i = Index("tf_idf_example_4.xml", "a", "b", "c")
    ids_to_titles = {"1": "Page 1", "2": "Page 2", "3": "Page 3"}
    titles_to_ids = {"Page 1": "1", "Page 2": "2", "Page 3": "3"}
    pg_to_links = {"1": ["Page 2", "Page 3"],
                   "2": ["Page 1", "Page 3"],
                   "3": ["Page 1", "Page 2"]}
    expected_term_relevances = {"page": {"1": 0, "2": 0, "3": 0},
                                "1": {"1": math.log(3, 10)}, "2": {"2":
                                math.log(3, 10)},
                                "3": {"3": math.log(3, 10)}}

    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance

def test_term_frequency_11():
    """
    Testing a corpus in which each page has the exact same text (but unique 
    titles) and each word on a page only occurs once
    """

    i = Index("tf_idf_example_11.xml", "a", "b", "c")
    ids_to_titles = {"1": "Foods", "2": "Fruits", "3": "Comestibles",
                     "4": "Consumables"}
    titles_to_ids = {"Foods": "1", "Fruits": "2", "Comestibles": "3",
                     "Consumables": "4"}
    pg_to_links = {"1": ["Fruits", "Comestibles", "Consumables"],
                   "2": ["Foods", "Comestibles", "Consumables"],
                   "3": ["Foods", "Fruits", "Consumables"],
                   "4": ["Foods", "Fruits", "Comestibles"]}
    expected_term_relevances = {"food": {"1": math.log(4, 10)},
                                "appl": {"1": 0, "2": 0, "3": 0, "4": 0},
                                "banana": {"1": 0, "2": 0, "3": 0, "4": 0},
                                "orang": {"1": 0, "2": 0, "3": 0, "4": 0},
                                "tomato": {"1": 0, "2": 0, "3": 0, "4": 0},
                                "fruit": {"2": math.log(4, 10)},
                                "comest": {"3": math.log(4, 10)},
                                "consum": {"4": math.log(4, 10)}}
    assert ids_to_titles == i.id_to_title
    assert titles_to_ids == i.title_to_id
    assert pg_to_links == i.page_to_links
    assert expected_term_relevances == i.words_to_ids_to_term_relevance