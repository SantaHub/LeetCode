import pytest

from simpleSolution import UndergroundSystem


@pytest.fixture
def system() -> UndergroundSystem:
    return UndergroundSystem()


def test_leetcode_example_1(system: UndergroundSystem):
    system.checkIn(45, "Leyton", 3)
    system.checkIn(32, "Paradise", 8)
    system.checkIn(27, "Leyton", 10)
    system.checkOut(45, "Waterloo", 15)
    system.checkOut(27, "Waterloo", 20)
    system.checkOut(32, "Cambridge", 22)
    assert system.getAverageTime("Paradise", "Cambridge") == pytest.approx(14.0)
    assert system.getAverageTime("Leyton", "Waterloo") == pytest.approx(11.0)
    system.checkIn(10, "Leyton", 24)
    assert system.getAverageTime("Leyton", "Waterloo") == pytest.approx(11.0)
    system.checkOut(10, "Waterloo", 38)
    assert system.getAverageTime("Leyton", "Waterloo") == pytest.approx(12.0)


def test_single_trip(system: UndergroundSystem):
    system.checkIn(1, "A", 10)
    system.checkOut(1, "B", 20)
    assert system.getAverageTime("A", "B") == pytest.approx(10.0)


def test_route_direction_matters(system: UndergroundSystem):
    system.checkIn(1, "A", 0)
    system.checkOut(1, "B", 5)
    system.checkIn(2, "B", 0)
    system.checkOut(2, "A", 15)
    assert system.getAverageTime("A", "B") == pytest.approx(5.0)
    assert system.getAverageTime("B", "A") == pytest.approx(15.0)


def test_multiple_trips_same_route(system: UndergroundSystem):
    system.checkIn(1, "X", 0)
    system.checkOut(1, "Y", 4)
    system.checkIn(2, "X", 10)
    system.checkOut(2, "Y", 16)
    assert system.getAverageTime("X", "Y") == pytest.approx(5.0)


def test_overlapping_customers(system: UndergroundSystem):
    system.checkIn(1, "S", 1)
    system.checkIn(2, "S", 2)
    system.checkOut(1, "E", 5)  # duration 4
    system.checkOut(2, "E", 8)  # duration 6
    assert system.getAverageTime("S", "E") == pytest.approx(5.0)


def test_customer_can_travel_again(system: UndergroundSystem):
    system.checkIn(7, "A", 0)
    system.checkOut(7, "B", 3)
    system.checkIn(7, "A", 10)
    system.checkOut(7, "B", 20)
    assert system.getAverageTime("A", "B") == pytest.approx(6.5)


def test_independent_routes(system: UndergroundSystem):
    system.checkIn(1, "A", 0)
    system.checkOut(1, "B", 10)
    system.checkIn(2, "A", 0)
    system.checkOut(2, "C", 4)
    assert system.getAverageTime("A", "B") == pytest.approx(10.0)
    assert system.getAverageTime("A", "C") == pytest.approx(4.0)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
