import cohere

# Initialize Cohere client with your API key
co = cohere.Client('myFPYVEJcMwpY7NYtLYMHZzEgzeG0JRBXuE9XOib')  # Replace with your actual API key

# Define your input ingredients
ingredients = "chicken, garlic, and tomatoes"

# Create a message prompt
prompt = f"Create a detailed cooking recipe using the following ingredients: {ingredients}"

# Generate the recipe using chat (command-r)
response = co.chat(
    model='command-r',
    message=prompt,
)

# Print the generated recipe
print("Recipe:\n")
print(response.text.strip())
