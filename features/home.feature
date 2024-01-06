Feature: As a user, I want to be able to access my github account page

  Scenario Outline: Given home page, i can go to Repositories page
    Given the home page "<homepage>" is open
    When i click "repos" tab on the home page
    And the next page is "<page>" page
    And the page url contain "<link>"
    And i click "<project>" project link
    Then the repos page description is "<description>"
    Examples:
      | homepage   | tab | page | link | project |  description |
      | https://github.com/stckwok | repos  |  Repositories  | repositories  | github_api_test | GitHub API validation using Playwright  |