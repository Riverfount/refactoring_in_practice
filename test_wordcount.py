import sys

from wordcount import main


def run(mode, capsys, monkeypath):
    monkeypath.setattr(sys, "argv", ["wordcount.py", mode, "letras.txt"])
    main()
    out, _ = capsys.readouterr()
    return out


def test_count(capsys, monkeypatch):
    assert run("--count", capsys, monkeypatch) == "a 2\nb 4\nc 3\n"


def test_topcount(capsys, monkeypatch):
    assert run("--topcount", capsys, monkeypatch) == "b 4\nc 3\na 2\n"
