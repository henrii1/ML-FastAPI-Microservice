import pytest
from webapp.app_greedy import greedy_coin




def test_coin():
    coin = greedy_coin("23")
    assert len(coin) > 0
