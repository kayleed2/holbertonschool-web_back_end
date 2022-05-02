function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {};
  const inc = `income-${getCurrentYear()}`;
  const g = `gdp-${getCurrentYear()}`;
  const cap = `capita-${getCurrentYear()}`;
  budget[inc] = income;
  budget[g] = gdp;
  budget[cap] = capita;

  return budget;
}
