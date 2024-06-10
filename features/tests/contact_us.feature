# Created by Dimitri at 5/27/2024
Feature: Contact Us Page Access


  Scenario: User can open the Contact Us page
    Given I am on the main page
    When I log in
    And I click on the settings option
    And I click on the Contact Us option
    Then The Contact Us page should open
    And There should be at least 4 social media icons

