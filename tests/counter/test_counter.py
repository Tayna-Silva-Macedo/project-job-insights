from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    words_list = ["python", "Python", "javascript", "Javascript"]
    expected_list = [1639, 1639, 122, 122]

    for index in range(len(words_list)):
        assert (
            count_ocurrences(path, words_list[index]) == expected_list[index]
        )
