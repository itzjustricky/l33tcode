# Write your MySQL query statement below

SELECT s.Score, ScoreRanks.Rank
FROM Scores s
LEFT JOIN (
          SELECT s.DistinctScore as Score, ROW_NUMBER() OVER () as 'Rank'
          FROM (
              SELECT DISTINCT Score as DistinctScore
              FROM Scores
              ORDER BY DistinctScore DESC) s
      ) ScoreRanks
ON s.Score = ScoreRanks.Score
ORDER BY ScoreRanks.Rank ASC
