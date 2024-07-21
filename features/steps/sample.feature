Feature: Example API feature

  Scenario: Fetching a post
    When I send a GET request to "posts/1"
    Then the response status should be 200
    And the response body should contain the title "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
