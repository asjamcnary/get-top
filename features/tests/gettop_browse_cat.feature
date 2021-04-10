# Created by asjamcnary at 4/6/21
Feature: Test for Browse Categoris
  # Enter feature description here

  Scenario: Verify Browse Categories functionalities

    Given Open Gettop page 'https://gettop.us/'
    Then  Header "Browse Our Categories" text is shown
    And   4 category titles are shown
    And   Verify correct category title
    When  Click thru each category title
    Then  Correct page opens

