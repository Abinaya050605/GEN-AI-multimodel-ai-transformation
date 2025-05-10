import cohere

# Initialize Cohere with your API key
co = cohere.Client('myFPYVEJcMwpY7NYtLYMHZzEgzeG0JRBXuE9XOib')

# Define the user query
message = """
I really found 'Anxious People' and 'Lessons in Chemistry' interesting, can you suggest me more such books?
"""

# Send the query to Cohere's chat model
response = co.chat(
    message=message,
    chat_history=[]
)

# Display the response
print("\n=== Book Recommendations ===\n")
print(response.text)