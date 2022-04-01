import io
from contextlib import redirect_stdout

from questions.basic_io.main import *
from questions.basic_io.challenge import word_exists_in_file


def test_say_hello(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Bob")
    out = io.StringIO()
    with redirect_stdout(out):
        say_hello()

    assert out.getvalue() == "Hello Bob!\n"


def test_calculate_sum(mocker):
    mocker.patch("builtins.input", side_effect=["2", "3"])
    out = io.StringIO()

    with redirect_stdout(out):
        calculate_sum()

    assert out.getvalue() == "5\n"

    # Challenge Test
    mocker.patch("builtins.input", side_effect=["10", "5", "-"])
    out = io.StringIO()
    with redirect_stdout(out):
        calculate_sum()

    assert out.getvalue() == "5\n"

    mocker.patch("builtins.input", side_effect=["10", "5", "*"])
    out = io.StringIO()
    with redirect_stdout(out):
        calculate_sum()

    assert out.getvalue() == "50\n"


def test_print_out_authors():
    out = io.StringIO()
    with redirect_stdout(out):
        print_out_authors()

    assert out.getvalue() == "Bob\n\nJane\n\n"


def test_word_exists_in_file(mocker):
    mocker.patch("builtins.input", side_effect=["questions/basic_io/authors.txt", "Bob"])
    assert word_exists_in_file()

    mocker.patch("builtins.input", side_effect=["questions/basic_io/authors.txt", "Spy"])
    assert not word_exists_in_file()


