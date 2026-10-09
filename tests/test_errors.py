from src.pinterest.client import PinterestAPIError


def test_error_message():

    try:
        raise PinterestAPIError(
            "401 Unauthorized: Check your access token."
        )

    except PinterestAPIError as error:
        print("Handled:", error)


test_error_message()