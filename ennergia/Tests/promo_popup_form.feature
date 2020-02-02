Feature: Popup form with a proposal to receive a promotional code for the first buy

  Scenario: Closing a form with a proposal to receive a promotional code
    When open the main page
    And choose section
    And choose category
    And choose subcategory
    Then appearance of a form with a proposal to receive a promotional code
    And this form can be closed
