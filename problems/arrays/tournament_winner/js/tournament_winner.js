export const tournamentWinner = (competitions, results) => {
  let currentLeader = { score: 0, name: "" };

  const scores = {};

  for (let i = 0; i < competitions.length; i++) {
    const [homeTeam, awayTeam] = competitions[i];
    const winner = results[i] === 0 ? awayTeam : homeTeam;

    scores[winner] = (scores[winner] || 0) + 3;

    if (scores[winner] > currentLeader.score) {
      currentLeader = { score: scores[winner], name: winner };
    }
  }

  return currentLeader.name;
};
