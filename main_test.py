from main import assignment_1
import pytest

def test_assignment_1():
  try:
    result = assignment_1(3, True, False, False, "plots/", "fetal_health_datasets/fetal_health.csv")
    print(result)
  except Exception as e:
    pytest.fail(f"An error occurred: {e}")
