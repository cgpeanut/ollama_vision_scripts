import ollama

response = ollama.chat(
        model='llama3.2-vision:90b',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['trumpy_one.jpg']
  }]

)

print(response)


response = ollama.chat(
        model='llama3.2-vision:90b',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['ass.jpg']
  }]

)

print(response)
