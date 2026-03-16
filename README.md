# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Purpose
This project is a Streamlit number-guessing game used to practice debugging AI-generated code, fixing state-management issues, and improving testability through refactoring.

### Bugs Found
- Hint direction bug: too-high guesses told players to go higher.
- State reset bug: new games did not fully reset game state.
- Attempt counter bug: attempts started at `1` instead of `0`.
- Difficulty consistency bug: range messaging/reset behavior did not always match difficulty.
- Type comparison bug: mixed numeric types could produce incorrect comparisons.

### Fixes Applied
- Moved game logic functions into `logic_utils.py` and imported them in `app.py`.
- Corrected hint direction logic in `check_guess`.
- Fixed session-state initialization and full reset behavior for new games/difficulty changes.
- Standardized numeric comparisons in `check_guess`.
- Updated and expanded tests in `tests/test_game_logic.py`.
- Added `pytest.ini` to stabilize import resolution during test runs.

Detailed process notes are in `reflection.md`.

## 📸 Demo

![Winning game screenshot](<images/game screenshot.png>)
