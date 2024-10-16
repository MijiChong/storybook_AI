import os
import streamlit as st
import openai

# Set the OpenAI API key
openai.api_key = os.getenv('OpenAI_API_key')


# Story generation function
def story_gen(prompt):
  system_prompt = """
    You are a world-renowned author of young adult fiction short stories.
    Given a concept, generate a short story with a twist ending, based on the provided theme.
    """

  response = openai.ChatCompletion.create(  # Correct method name
      model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo"
      messages=[{
          "role": "system",
          "content": system_prompt
      }, {
          "role": "user",
          "content": prompt
      }],
      temperature=1,
      max_tokens=2000)

  return response['choices'][0]['message']['content']


# Cover art generation function
def art_gen(prompt):
  response = openai.Image.create(  # Correct method for generating images
      prompt=prompt,
      n=1,
      size="256x256")

  return response['data'][0]['url']


# Design generation function
def design_gen(prompt):
  system_prompt = """
    You will be given a short story. Generate a prompt for a cover art that is suitable for the story. The prompt is for DALL·E.
    """

  response = openai.ChatCompletion.create(  # Correct method name
      model="gpt-4o-mini",  # Use "gpt-4" or "gpt-3.5-turbo"
      messages=[{
          "role": "system",
          "content": system_prompt
      }, {
          "role": "user",
          "content": prompt
      }],
      temperature=1.3,
      max_tokens=1000)

  return response['choices'][0]['message']['content']


# Streamlit app interface
prompt = st.text_input("Enter a prompt")

if st.button("Generate"):
  # Generate story
  story = story_gen(prompt)

  # Generate design based on the story
  design = design_gen(story)

  # Generate cover art based on the design prompt
  art = art_gen(design)

  # Display results
  st.caption(design)
  st.divider()
  st.image(art)
  st.divider()
  st.write(story)
