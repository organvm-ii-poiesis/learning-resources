"""Exercise creation and assessment rubrics.

Provides the ExerciseBank for creating exercises with multiple
question types and automated scoring rubrics.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


class QuestionType(Enum):
    """Types of exercise questions."""

    MULTIPLE_CHOICE = "multiple_choice"
    SHORT_ANSWER = "short_answer"
    CODE_CHALLENGE = "code_challenge"
    REFLECTION = "reflection"


@dataclass
class Question:
    """A single exercise question."""

    question_id: str
    question_type: QuestionType
    prompt: str
    correct_answer: str | None
    points: int
    hints: list[str] = field(default_factory=list)


@dataclass
class Exercise:
    """A collection of questions forming an exercise."""

    exercise_id: str
    title: str
    topic_id: str
    questions: list[Question] = field(default_factory=list)

    @property
    def total_points(self) -> int:
        """Return the maximum possible score."""
        return sum(q.points for q in self.questions)


class ExerciseBank:
    """Manages a bank of exercises with creation and scoring.

    Provides methods for creating exercises, adding questions,
    and computing scores against rubrics.
    """

    def __init__(self) -> None:
        self._exercises: dict[str, Exercise] = {}

    @property
    def exercise_count(self) -> int:
        """Return the number of exercises in the bank."""
        return len(self._exercises)

    def create_exercise(self, title: str, topic_id: str) -> Exercise:
        """Create a new exercise.

        Args:
            title: Exercise title.
            topic_id: The curriculum topic this exercise assesses.

        Returns:
            The newly created Exercise.
        """
        exercise = Exercise(
            exercise_id=uuid4().hex[:8],
            title=title,
            topic_id=topic_id,
        )
        self._exercises[exercise.exercise_id] = exercise
        return exercise

    def add_question(
        self,
        exercise_id: str,
        question_type: QuestionType,
        prompt: str,
        correct_answer: str | None = None,
        points: int = 10,
        hints: list[str] | None = None,
    ) -> Question | None:
        """Add a question to an exercise.

        Args:
            exercise_id: The exercise to add to.
            question_type: Type of question.
            prompt: The question text.
            correct_answer: Expected answer (None for reflections).
            points: Point value.
            hints: Optional hints for the learner.

        Returns:
            The created Question, or None if exercise not found.
        """
        exercise = self._exercises.get(exercise_id)
        if exercise is None:
            return None

        question = Question(
            question_id=uuid4().hex[:8],
            question_type=question_type,
            prompt=prompt,
            correct_answer=correct_answer,
            points=points,
            hints=hints or [],
        )
        exercise.questions.append(question)
        return question

    def score_answers(
        self, exercise_id: str, answers: dict[str, str]
    ) -> dict[str, Any] | None:
        """Score a set of answers against an exercise.

        Args:
            exercise_id: The exercise to score against.
            answers: Mapping of question_id to submitted answer.

        Returns:
            Scoring summary, or None if exercise not found.
        """
        exercise = self._exercises.get(exercise_id)
        if exercise is None:
            return None

        total = 0
        earned = 0
        details: list[dict[str, Any]] = []

        for question in exercise.questions:
            total += question.points
            submitted = answers.get(question.question_id, "")
            correct = (
                question.correct_answer is not None
                and submitted.strip().lower() == question.correct_answer.strip().lower()
            )
            points_earned = question.points if correct else 0
            earned += points_earned
            details.append({
                "question_id": question.question_id,
                "correct": correct,
                "points_earned": points_earned,
                "points_possible": question.points,
            })

        return {
            "exercise_id": exercise_id,
            "total_points": total,
            "earned_points": earned,
            "percentage": round(earned / total * 100, 1) if total > 0 else 0.0,
            "details": details,
        }
