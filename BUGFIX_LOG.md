# Bug Fix Log

## Commit 1 - `8b011a0`
- Moved game logic into `logic_utils.py` and updated imports in `app.py`.
- Fixed incorrect hint direction in `check_guess`.
- Updated tests to assert `(outcome, message)` and added `pytest.ini` for stable imports.
- Result: tests passing for hint logic and refactor paths.

## Commit 2 - `f9eab43`
- Fixed state baseline (`attempts` starts at `0`), accurate range text, and safe attempts-left display.
- Fixed `New Game` to reset full state (`secret`, `attempts`, `score`, `status`, `history`) and honor difficulty range.
- Removed mixed-type secret conversion in `app.py` and normalized numeric comparisons in `check_guess`.
- Added regression tests for numeric-string secret comparisons.
- Result: tests passing with extra edge-case coverage.
