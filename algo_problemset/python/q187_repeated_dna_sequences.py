from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        DnaLength = len(s)
        if DnaLength < 10:
            return []

        sequencesSeen, repeatingSequences = set(), set()
        for sequenceEnd in range(10, DnaLength+1):
            sequenceStart = sequenceEnd - 10
            seq = s[sequenceStart:sequenceEnd]
            if seq in sequencesSeen:
                repeatingSequences.add(seq)

            sequencesSeen.add(seq)

        return list(repeatingSequences)
