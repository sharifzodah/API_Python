# Created by Admin at 12/4/2022
Feature: GitHub API validation


  @Git
  Scenario: Session management check
    Given I have GitHub auth credentials
    When I hit getRepo API of GitHub
    Then the status code of response should be 200
