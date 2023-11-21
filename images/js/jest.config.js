/**
 * For a detailed explanation regarding each configuration property, visit:
 * https://jestjs.io/docs/configuration
 */
/** @type {import('jest').Config} */
const config = {
  clearMocks: true,
  testRegex: "(.*).(test|spec).(jsx?|js?|tsx?)$",
  testPathIgnorePatterns: ["/lib/", "/node_modules/"],
  collectCoverage: false,
  coverageDirectory: "coverage",
};
module.exports = config;
