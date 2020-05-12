import pytest
from src.film import Film

def test_exercise(capsys):
    chipmunks = Film("Alvin and the Chipmunks: The Squeakquel", 0)
    age = 20

    if (age >= chipmunks.age_rating):
        print("You may watch the film " + chipmunks.name)
    else:
        print("You may not watch the film " + chipmunks.name)

    out, err = capsys.readouterr()
    assert out == "You may watch the film Alvin and the Chipmunks: The Squeakquel\n"
