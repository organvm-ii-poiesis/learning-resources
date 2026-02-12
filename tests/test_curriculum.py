"""Tests for the curriculum module."""

from src.curriculum import CurriculumBuilder


class TestCurriculumBuilder:
    def test_create_curriculum_with_title(self) -> None:
        builder = CurriculumBuilder("Art Fundamentals", domain="art")
        assert builder.title == "Art Fundamentals"
        assert builder.module_count == 0

    def test_add_module(self) -> None:
        builder = CurriculumBuilder("Test")
        module = builder.add_module("Intro", "Introduction to the subject")
        assert module.title == "Intro"
        assert builder.module_count == 1

    def test_add_topic_to_module(self) -> None:
        builder = CurriculumBuilder("Test")
        mod = builder.add_module("M1", "Module 1")
        topic = builder.add_topic(mod.module_id, "T1", "Topic 1", duration_minutes=45)
        assert topic is not None
        assert topic.title == "T1"
        assert topic.duration_minutes == 45

    def test_add_topic_to_nonexistent_module(self) -> None:
        builder = CurriculumBuilder("Test")
        result = builder.add_topic("fake_id", "T1", "Topic 1")
        assert result is None

    def test_total_duration(self) -> None:
        builder = CurriculumBuilder("Test")
        mod = builder.add_module("M1", "Module 1")
        builder.add_topic(mod.module_id, "T1", "Topic 1", duration_minutes=30)
        builder.add_topic(mod.module_id, "T2", "Topic 2", duration_minutes=45)
        assert builder.get_total_duration() == 75

    def test_prerequisite_chain(self) -> None:
        builder = CurriculumBuilder("Test")
        m1 = builder.add_module("Foundations", "Base module")
        m2 = builder.add_module("Intermediate", "Builds on foundations", prerequisites=[m1.module_id])
        m3 = builder.add_module("Advanced", "Builds on intermediate", prerequisites=[m2.module_id])
        chain = builder.get_prerequisite_chain(m3.module_id)
        assert m1.module_id in chain
        assert m2.module_id in chain

    def test_export_structure(self) -> None:
        builder = CurriculumBuilder("Export Test", domain="tech")
        builder.add_module("M1", "First module")
        data = builder.export()
        assert data["title"] == "Export Test"
        assert data["domain"] == "tech"
        assert data["module_count"] == 1
