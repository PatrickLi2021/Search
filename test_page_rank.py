import pytest
from index import *

def test_page_rank_1():
    """Example test from handout """

    indexer_1 = Index("PageRankExample1.xml", "a", "b", "c")
    page_rank_dict = {"A": 0.4326, "B": 0.2340, "C": 0.333}
    assert page_rank_dict["A"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["1"], 0.001)
    assert page_rank_dict["B"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["2"], 0.001)
    assert page_rank_dict["C"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["3"], 0.001)

def test_page_rank_2():
    """Example test from handout """

    indexer_1 = Index("PageRankExample2.xml", "a", "b", "c")
    assert abs(indexer_1.ids_to_page_ranks["1"] - 0.2018) < 0.001
    assert abs(indexer_1.ids_to_page_ranks["2"] - 0.0375) < 0.001
    assert abs(indexer_1.ids_to_page_ranks["3"] - 0.3740) < 0.001
    assert abs(indexer_1.ids_to_page_ranks["4"] - 0.3867) < 0.001

def test_page_rank_3():
    """Example test from handout """

    indexer_1 = Index("PageRankExample3.xml", "a", "b", "c")
    assert abs(indexer_1.ids_to_page_ranks["1"] - 0.0524) < 0.001
    assert abs(indexer_1.ids_to_page_ranks["2"] - 0.0524) < 0.001
    assert abs(indexer_1.ids_to_page_ranks["3"] - 0.4476) < 0.001
    assert abs(indexer_1.ids_to_page_ranks["4"] - 0.4476) < 0.001

def test_page_rank_4():
    """Example test from handout """

    indexer_1 = Index("PageRankExample4.xml", "a", "b", "c")
    page_rank_dict = {"A": 0.0375, "B": 0.0375, "C": 0.4625, "D": 0.4625}
    assert page_rank_dict["A"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["1"], 0.001)
    assert page_rank_dict["B"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["2"], 0.001)
    assert page_rank_dict["C"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["3"], 0.001)
    assert page_rank_dict["D"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["4"], 0.001)

def test_page_rank_5():
    """ Testing a corpus where each page links to itself and all other 
        documents"""

    indexer_1 = Index("tf_idf_example_8.xml", "a", "b", "c")
    page_rank_dict = {"1": 1/2, "2": 1/2}
    assert page_rank_dict["1"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["1"], 0.001)
    assert page_rank_dict["2"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["2"], 0.001)

def test_page_rank_6():
    """Testing a corpus in which each page in the XMl only contains links that 
       do NOT link to any other pages in the corpus"""

    indexer_1 = Index("tf_idf_example_9.xml", "a", "b", "c")
    page_rank_dict = {"1": 1/2, "2": 1/2}
    assert page_rank_dict["1"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["1"], 0.001)
    assert page_rank_dict["2"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["2"], 0.001)

def test_page_rank_7():
    """ 
    Testing a page that contains no links and has no stop words or stemming 
    involved.
    """
    
    indexer_1 = Index("tf_idf_example_1.xml", "a", "b", "c")
    print(indexer_1.ids_to_page_ranks)
    page_rank_dict = {"0": 1/3, "1": 1/3, "2": 1/3}
    assert page_rank_dict["0"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["0"], 0.001)
    assert page_rank_dict["1"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["1"], 0.001)
    assert page_rank_dict["2"] == \
        pytest.approx(indexer_1.ids_to_page_ranks["2"], 0.001)

def test_euc_distance1():
    """" Distance is zero """
    i = Index("PageRankExample4.xml", "a", "b", "c")
    assert 0 == i.euclidean_distance({1: 1.5, 2: 2.6, 3: 0.0006}, {
                                     1: 1.5, 2: 2.6, 3: 0.0006})

def test_euc_distance2():
    """" Distance is non-zero """
    i = Index("PageRankExample4.xml", "a", "b", "c")
    assert (abs(15.77973384 - i.euclidean_distance({1: 1, 2: 2, 3: 3}, {
                                     1: 5, 2: 10, 3: 16}))) < 0.0001