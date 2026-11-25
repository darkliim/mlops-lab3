from src.user_input import *
import re   

def test_username(monkeypatch):
    responses = iter(["", "ab", "admin", " valid_user"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    
    result = ask_username()

    #not empty
    assert len(result) > 0

    #no spaces
    assert result.count(" ") == 0

    #not in the banned list
    assert result.lower() not in ["admin", "root", "moderator", "mod", "null"]

def test_mail(monkeypatch):
    responses = iter(["", "dasha.com", "dasha@gmail.", "dasha@gmail.com"])
    attempts = 0

    def fake_input(_promt=""):
        nonlocal attempts
        attempts += 1
        return next(responses)

    monkeypatch.setattr("builtins.input", fake_input)

    result = ask_mail()
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    assert re.fullmatch(pattern, result)

    print(f"The number of attempts to validate the test: {attempts}")

def test_display_name(monkeypatch):
    responses = iter(["", "esrser234", "dasha123"])
    attempts = 0
    user_name = None

    def fake_input(_promt=""):
        nonlocal attempts
        attempts += 1
        return next(responses)     

    def spy_username():
        nonlocal user_name
        user_name = ask_username()
        return user_name

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr("src.user_input.ask_username", spy_username)

    result = ask_display_name()

    assert len(result) >= 3 and len(result) <=20
    pattern = "^[A-Za-z][A-Za-z0-9_]*$"
    assert re.match(pattern, result)
    assert result.lower() not in ["admin", "root", "moderator", "mod", "null"]
    assert result == user_name

    print(f"The number of attempts needed for success:{attempts}")
    

 
    