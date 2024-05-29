# Created by Dimitri at 5/27/2024
Feature: Contact Us Page Access
  As a user,
  I want to be able to access the Contact Us page
  So that I can reach out to the support team.

  Scenario: User can open the Contact Us page
    Given I am on the main page
    When I log in
    And I click on the settings option
    And I click on the Contact Us option
    Then the Contact Us page should open
    And there should be at least 4 social media icons
