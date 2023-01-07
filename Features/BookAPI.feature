# Created by Admin at 12/4/2022
#  Terminal command:  behave Features/BookAPI.feature --no-capture --tags=smoke
#  Generating report: behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
Feature: Verify if Books are added and deleted

  @Library
  Scenario: Verify AddBook API Functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And the status code of response should be 200


  @Library
  Scenario Outline: Verify AddBook API Functionality
    Given the Book details with <isbn>, <aisle> and <author>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And the status code of response should be 200
    Examples:
      | isbn | aisle | author    |
      | bcd4 | 1007  | Abduhamid |
      | bcd4 | 1008  | Abduhamid |