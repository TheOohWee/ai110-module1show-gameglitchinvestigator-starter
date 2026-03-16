# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the app I noticed 5 bugs. The game looked playable on the surface, but the hints were off and the attempt counter was already wrong before I even guessed.

1. **Hints were backwards.** When my guess was too high (e.g., I guessed 80 and the secret was 30), the game said "Go HIGHER!" — the exact wrong direction. When my guess was too low it said "Go LOWER!"

2. **New Game button didn't actually reset the game.** Clicking "New Game" generated a new secret number but left the game status (won/lost) and history unchanged. If I had lost a round, clicking New Game still showed the "Game over" message and blocked me from guessin while expected was a fresh game with a clean slate.

3. **First attempt wasn't being tracked in history.** After the new game button was pressed, the history from the previous game lingered. The first guess of the new game appeared to be missing because history was never cleared on reset.

4. **Attempt counter started at 1 instead of 0.** The session state initialized `attempts = 1`, so the very first guess was already labeled as attempt #2 internally while expected was for `attempts` to start at 0 so the first real guess is attempt #1.

5. **"Attempts left" showed 7 instead of 8 at the start.** This was a direct consequence of bug #4, because `attempts` started at 1, the formula `attempt_limit - attempts` showed 8 − 1 = 7 on Normal difficulty right from the beginning instead of the correct 8.

Maybe 3-5 is the same bug, but it causes various problems, so I labeled it into this 3. 


---

## 2. How did you use AI as a teammate?

I used GitHub Copilot as my primary AI teammate while debugging and refactoring. One correct suggestion was to move `check_guess` into `logic_utils.py` and keep `app.py` focused on Streamlit UI flow; that made the code easier to test and maintain. I verified that change by running `pytest` and confirming the game still called the same function through imports. One misleading path came from running plain `pytest`, which used a global Anaconda environment and caused a `ModuleNotFoundError`; it looked like the code was broken, but the real problem was environment mismatch. I verified the root cause by comparing `pytest --version` and rerunning tests with `.venv/bin/python -m pytest`.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after both behavior and tests agreed: manual logic checks for gameplay flow and automated checks for function outputs. I ran `pytest` repeatedly as I patched issues, and by the end it reported `5 passed`. A key test I added checks `check_guess(9, "10")` returns `("Too Low", "Go HIGHER!")`, which protects against accidental string/lexicographic comparisons. Another useful check confirms a too-high guess returns the lower hint, so the original high/low bug cannot silently return. AI helped by suggesting edge cases to test and by pointing out contract mismatches between test expectations and actual function return values.

---

## 4. What did you learn about Streamlit and state?

The secret number changed because Streamlit reruns the script on every interaction, so values that are not protected by `st.session_state` can be regenerated unexpectedly. I would explain reruns as: each button press re-executes the file top to bottom, and session state is the memory that survives those reruns. The fix was to initialize and update core game state (`secret`, `attempts`, `status`, `score`, `history`) through `st.session_state` only, and reset it intentionally on `New Game` or difficulty changes. I also removed the odd/even secret type-switching logic so comparisons stay numeric and predictable. That made guesses stable and hints consistent across turns.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is making small, testable commits per bug so I can isolate regressions quickly. Next time, I would verify the Python environment first (`which pytest` and `python -m pytest`) before trusting failure output, because tooling mismatch can waste time. I also want to keep adding edge-case tests whenever I touch comparison logic, not just happy-path tests. This project changed my view of AI-generated code by showing that AI can accelerate debugging, but only if I verify every assumption with tests and runtime checks. AI is useful as a collaborator, not as an autopilot.
