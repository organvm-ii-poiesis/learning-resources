"""Tests for the paths module."""

from src.paths import LearningPath


class TestLearningPath:
    def test_empty_path_has_zero_progress(self) -> None:
        path = LearningPath("Test Path")
        assert path.step_count == 0
        assert path.progress_pct == 0.0

    def test_add_step(self) -> None:
        path = LearningPath("Test")
        step = path.add_step("mod_1", "First Step")
        assert step.step_id == 0
        assert path.step_count == 1

    def test_complete_step_updates_progress(self) -> None:
        path = LearningPath("Test")
        path.add_step("mod_1", "Step 1")
        path.add_step("mod_2", "Step 2")
        path.complete_step(0, score=0.9)
        assert path.completed_count == 1
        assert path.progress_pct == 50.0

    def test_complete_invalid_step_returns_false(self) -> None:
        path = LearningPath("Test")
        assert path.complete_step(99) is False

    def test_get_next_step_returns_first_incomplete(self) -> None:
        path = LearningPath("Test")
        path.add_step("mod_1", "Step 1")
        path.add_step("mod_2", "Step 2")
        path.complete_step(0)
        next_step = path.get_next_step()
        assert next_step is not None
        assert next_step.step_id == 1

    def test_get_next_step_returns_none_when_all_complete(self) -> None:
        path = LearningPath("Test")
        path.add_step("mod_1", "Step 1")
        path.complete_step(0)
        assert path.get_next_step() is None

    def test_average_score(self) -> None:
        path = LearningPath("Test")
        path.add_step("m1", "S1")
        path.add_step("m2", "S2")
        path.complete_step(0, score=0.8)
        path.complete_step(1, score=1.0)
        assert path.get_average_score() == 0.9
