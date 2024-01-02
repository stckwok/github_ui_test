Feature: As a user, I want to be able to access my github account page

  Scenario: Given home page, i can go to Repositories page
    Given the home page is open
    When i click "repos" tab on the home page
    Then the next page is "Repositories" page