from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    expected_keys = {"title", "salary", "type"}

    dict_jobs = read_brazilian_file(path)

    keys = set()
    for job in dict_jobs:
        for key in job.keys():
            keys.add(key)

    assert keys == expected_keys
