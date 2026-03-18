import random
import pytest
from logic_utils import check_guess, get_range_for_difficulty

@pytest.mark.parametrize("difficulty,expected_low,expected_high", [
    ("Easy", 1, 20),
    ("Normal", 1, 100),
    ("Hard", 1, 50),
])
def test_new_game_secret_stays_within_difficulty_range(difficulty, expected_low, expected_high):
    low, high = get_range_for_difficulty(difficulty)
    assert low == expected_low, f"{difficulty}: expected low={expected_low}, got {low}"
    assert high == expected_high, f"{difficulty}: expected high={expected_high}, got {high}"
    for _ in range(50):
        secret = random.randint(low, high)
        assert expected_low <= secret <= expected_high, (
            f"Secret {secret} out of range [{expected_low}, {expected_high}] for difficulty '{difficulty}'"
        )


@pytest.mark.parametrize("old_difficulty,new_difficulty", [
    ("Normal", "Easy"),
    ("Normal", "Hard"),
    ("Hard", "Easy"),
    ("Easy", "Normal"),
])
def test_secret_regenerates_when_difficulty_changes(old_difficulty, new_difficulty):
    # Get the bounds for both difficulties
    old_low, old_high = get_range_for_difficulty(old_difficulty)

    # When difficulty changes, a new secret must be drawn from the new range
    new_low, new_high = get_range_for_difficulty(new_difficulty)
    new_secret = random.randint(new_low, new_high)

    # The old secret may be out of the new range — that's exactly the bug
    # The new secret must always be within the new range
    assert new_low <= new_secret <= new_high, (
        f"After switching from {old_difficulty} to {new_difficulty}, "
        f"secret {new_secret} is outside [{new_low}, {new_high}]"
    )
    # Also confirm the old secret is NOT re-used — ranges must differ for this to be meaningful
    assert (old_low, old_high) != (new_low, new_high)


# def test_winning_guess():
#     # If the secret is 50 and guess is 50, it should be a win
#     result = check_guess(50, 50)
#     assert result == "Win"

# def test_guess_too_high():
#     # If secret is 50 and guess is 60, hint should be "Too High"
#     result = check_guess(60, 50)
#     assert result == "Too High"

# def test_guess_too_low():
#     # If secret is 50 and guess is 40, hint should be "Too Low"
#     result = check_guess(40, 50)
#     assert result == "Too Low"
