from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture()
def jobs_mock():
    return [
        {"min_salary": 100, "max_salary": 1000, "date_posted": "2020-06-10"},
        {"min_salary": 50, "max_salary": 2000, "date_posted": ""},
        {"min_salary": "", "max_salary": 3000, "date_posted": "2020-05-24"},
        {"min_salary": 200, "max_salary": "", "date_posted": "2020-05-02"},
    ]


def test_sort_by_criteria(jobs_mock):
    sorted_by_min = [
        {"min_salary": 50, "max_salary": 2000, "date_posted": ""},
        {"min_salary": 100, "max_salary": 1000, "date_posted": "2020-06-10"},
        {"min_salary": 200, "max_salary": "", "date_posted": "2020-05-02"},
        {"min_salary": "", "max_salary": 3000, "date_posted": "2020-05-24"},
    ]

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == sorted_by_min

    sorted_by_max = [
        {"min_salary": "", "max_salary": 3000, "date_posted": "2020-05-24"},
        {"min_salary": 50, "max_salary": 2000, "date_posted": ""},
        {"min_salary": 100, "max_salary": 1000, "date_posted": "2020-06-10"},
        {"min_salary": 200, "max_salary": "", "date_posted": "2020-05-02"},
    ]

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == sorted_by_max

    sorted_by_date = [
        {"min_salary": 100, "max_salary": 1000, "date_posted": "2020-06-10"},
        {"min_salary": "", "max_salary": 3000, "date_posted": "2020-05-24"},
        {"min_salary": 200, "max_salary": "", "date_posted": "2020-05-02"},
        {"min_salary": 50, "max_salary": 2000, "date_posted": ""},
    ]

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == sorted_by_date
