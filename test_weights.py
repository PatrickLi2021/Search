import pytest
from index import *

def test_weight_1():
    """ Testing on a page with no links to other pages"""

    indexer_1 = Index("tf_idf_example_1.xml", "a", "b", "c")
    weights = {'0': {'0': 0.15/3, '1': 0.475, '2': 0.475},
               '1': {'0': 0.475, '1': 0.15/3, '2': 0.475},
               '2': {'0': 0.475, '1': 0.475, '2': 0.15/3}}
    assert weights == indexer_1.weights

def test_weight_2():
    """ Testing on a page containing only links to pages outside the corpus"""

    indexer_1 = Index("tf_idf_example_5.xml", "a", "b", "c")
    weights = {'1': {'1': 0.075, '2': 0.85 + 0.075},
               '2': {'1': 0.85 + 0.075, '2': 0.075}}
    assert weights == indexer_1.weights

def test_weight_3():
    """ Testing on a corpus with pages that only link to themselves"""

    indexer_1 = Index("tf_idf_example_6.xml", "a", "b", "c")
    weights = {'1': {'1': 0.075, '2': 0.85 + 0.075},
               '2': {'1': 0.85 + 0.075, '2': 0.075}}
    assert weights == indexer_1.weights

def test_weight_4():
    """ Testing a corpus with one page with no links"""

    indexer_1 = Index("tf_idf_example_7.xml", "a", "b", "c")
    weights = {'1': {'1': 0.15}}
    assert weights == indexer_1.weights

def test_weight_5():
    """ Testing a corpus where each page links to itself and all other 
         documents"""

    indexer_1 = Index("tf_idf_example_8.xml", "a", "b", "c")
    weights = weights = {'1': {'1': 0.075, '2': 0.075 + 0.85},
                         '2': {'1': 0.075 + 0.85, '2': 0.075}}
    assert weights == indexer_1.weights

def test_weight_6():
    """ Testing a corpus in which each page links to both other pages within 
        the corpus and pages outside the corpus"""

    indexer_1 = Index("DocProcessingExample1.xml", "a", "b", "c")
    weights = weights = {'1': {'1': 0.15/3, '2': 0.475, '3': 0.475},
                         '2': {'1': 0.15/3, '2': 0.15/3, '3': 0.90},
                         '3': {'1': 0.475, '2': 0.475, '3': 0.15/3}}
    assert weights == indexer_1.weights

def test_weight_7():
    """ Testing a corpus in which each page links to the other documents in 
        the corpus"""

    indexer_1 = Index("tf_idf_example_10.xml", "a", "b", "c")
    weights = weights = {'1': {'1': 0.03, '2': 0.03 + 0.85/3,
                               '3': 0.03 + 0.85/3, '4': 0.03 + 0.85/3,
                               '5': 0.03},
                         '2': {'1': 0.03 + 0.85/3, '2': 0.03,
                               '3': 0.03 + 0.85/3,
                               '4': 0.03 + 0.85/3, '5': 0.03},
                         '3': {'1': 0.03 + 0.85/3, '2': 0.03 + 0.85/3,
                               '3': 0.03, '4': 0.03 + 0.85/3, '5': 0.03},
                         '4': {'1': 0.03 + 0.85/3, '2': 0.03 + 0.85/3,
                               '3': 0.03 + 0.85/3, '4': 0.03, '5': 0.03},
                         '5': {'1': 0.03, '2': 0.03 + 0.85/2,
                               '3': 0.03 + 0.85/2, '4': 0.03, '5': 0.03}}
    assert weights == indexer_1.weights