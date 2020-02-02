# Created by ksu12 at 01-Feb-20
Feature: Cart

  Scenario: Adding a product to the cart from its card
    When open the main page
    And cart counter doesn't exist
    And choose section
    And choose category
    And choose subcategory
    And close promo popup form
    And any random item is added to the cart
    And going to the cart
    Then there's 1 product in the cart
    And save cookies with 1 product in the cart
