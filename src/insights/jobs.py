from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    if not path.endswith(".csv"):
        raise ValueError("Formato de arquivo inválido!")

    try:
        with open(path) as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path}")


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    jobs = read(path)

    unique_job_types = set()
    for job in jobs:
        if job["job_type"]:
            unique_job_types.add(job["job_type"])

    return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    return [job for job in jobs if job["job_type"] == job_type]
