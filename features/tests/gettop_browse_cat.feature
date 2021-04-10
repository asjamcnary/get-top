# Created by asjamcnary at 4/6/21
Feature: Test for Browse Categoris
  # Enter feature description here

  Scenario: Verify Browse Categories functionalities

    Given Open Gettop page 'https://gettop.us/'
    Then  Header "Browse Our Categories" text is shown
    And   4 Header Titles are shown
    And   Verify correct Header Titles
    When  Click thru each Header Title
    Then  Correct page opens

