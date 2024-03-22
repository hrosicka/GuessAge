import requests

class AgifyAPI:
  """Class for working with the Agify.io API."""

  def __init__(self, name):
    """
    Initializes an API instance with the given name.

    Args:
      name: The name to estimate the age for.
    """
    self.name = name
    self.url = f"https://api.agify.io?name={name}"

  def get_estimated_age(self):
    """
    Retrieves the estimated age from the API.

    Returns:
      The estimated age as an integer, or None if an error occurs.
    """
    try:
      response = requests.get(self.url)
      response.raise_for_status()  # Raise an exception for non-200 status codes
      data = response.json()
      return int(data.get("age"))  # Return age as an integer

    except requests.exceptions.RequestException as e:
      print(f"Error: An error occurred while making the API request: {e}")
    except ValueError as e:
      print(f"Error: Invalid JSON response received: {e}")
  

def main():
  """Main function of the program."""

  # Get the name from the user
  name = input("Enter name: ")

  # Create an API instance
  api = AgifyAPI(name)

  # Get the estimated age from the API
  estimated_age = api.get_estimated_age()

  # Print the results
  if estimated_age is not None:
    print(f"Estimated age for {name}: {estimated_age}")
  else:
    print("Could not get estimated age.")

if __name__ == "__main__":
  main()