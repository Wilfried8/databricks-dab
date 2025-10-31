from types import SimpleNamespace

import pytest

from dab_test_labs import main


@pytest.fixture
def fake_spark():
    dataframe = SimpleNamespace(count=lambda: 6)
    reader = SimpleNamespace(table=lambda _: dataframe)
    return SimpleNamespace(read=reader)


def test_find_all_taxis(monkeypatch, fake_spark):
    monkeypatch.setattr(main, "_load_databricks_spark", lambda: fake_spark)
    taxis = main.find_all_taxis()
    assert taxis.count() > 5
