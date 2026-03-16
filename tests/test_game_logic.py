from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, the outcome is too high and hint says lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "Go LOWER!"


def test_guess_too_low():
    # If secret is 50 and guess is 40, the outcome is too low and hint says higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "Go HIGHER!"


def test_numeric_string_secret_too_low():
    # Numeric string secrets should be compared numerically, not lexicographically.
    outcome, message = check_guess(9, "10")
    assert outcome == "Too Low"
    assert message == "Go HIGHER!"


def test_numeric_string_secret_too_high():
    outcome, message = check_guess(12, "10")
    assert outcome == "Too High"
    assert message == "Go LOWER!"
