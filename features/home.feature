Feature: As a user, I want to be able to access my github account page

  Scenario: Given home page, i can go to Repositories page
    Given the home page is open
    When i click "repos" tab on the home page
    And the next page is "Repositories" page
    And the page url contain "repositories"
    And i click "github_api_test" project link
    Then the repos page description is "GitHub API validation using Playwright"