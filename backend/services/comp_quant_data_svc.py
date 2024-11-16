from typing import List

class CompiledQuantitativeDataService:
    def count_courses_offered(data, semester_filter: List[str], adjustment: List[int]):
        """
        Mimics COUNTIF logic for counting courses based on a filter.
        - data: List of course offerings (e.g., semesters like "Fall 2020").
        - semester_filter: Filter string (e.g., "Fall 2020").
        - adjustment: Value to subtract from the count.
        """

        for i in range(len(semester_filter)):
            count = sum(
                1 for entry in data if semester_filter in entry
            )  # COUNTIF equivalent
            return count - adjustment[i]