export default function getSanFranciscoDescription () {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479'
  };
  let newthing = getSanFranciscoDescription();
  return 'As of ${newthing.year} it was the seventh-highest income county in the United States, with a per capita personal income of ${newthing.budget.income}. As of 2015, San Francisco proper had a GDP of ${newthing.budget.gdp}, and a GDP per capita of ${newthing.budget.capita}.';
}
