Feature: Wishlist

  Scenario: Adding a product to the wishlist from its card
    When open the main page
    And go to the guest page
    And go to the wishlist
    And the product list in the wishlist is empty
    And go to the main page
    And choose random section
    And choose random category
    And choose random subcategory
    And close promo popup form
    And open random product card
    And add the product to the wishlist
    And go to the guest page
    And go to the wishlist
    Then there's 1 product in the wishlist
