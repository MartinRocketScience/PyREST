class SampleModel:
    def check_json_key_title_value(self, context, title):
        """
        Checks if the 'title' key in the JSON response body matches the expected title.
        
        Args:
            context: Behave context object that holds the response.
            title (str): The expected value of the 'title' key in the response JSON.
        
        Raises:
            AssertionError: If the 'title' key in the response JSON does not match the expected title.
        """
        response_json = context.response.json()
        assert response_json['title'] == title, f"Expected title '{title}' but got '{response_json['title']}'"
