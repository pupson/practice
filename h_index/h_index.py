"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith
paper, return the researcher's h-index.

The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that
 have each been cited at least h times.

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5
citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with
 no more than 3 citations each, their h-index is 3.

Input: citations = [1,3,1]
Output: 1

"""
import typing
from typing import List

citations = [3,0,6,1,5]
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for paper, citation in enumerate(citations):
            # is citation # >= # of paper
            #print(f"{count} .... {ele}")
            if citation >= paper+1:
                print(citation)
                break
            #print(list(enumerate(citations)))

s = Solution()
s.hIndex(citations)
