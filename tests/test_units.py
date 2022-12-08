"""Testing units."""

from pytest import approx  # type: ignore

import physical_units as units


def test_time() -> None:
    """Time."""
    t = units.Time()
    t.s = 123
    assert t.s == 123
    assert approx(t.ns) == 123 * 1e9
    t.ns = 456
    assert approx(t.s) == 456 / 1e9
