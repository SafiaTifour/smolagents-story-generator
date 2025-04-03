from agents import story_planner, story_writer, story_illustrator, image_generator

def generate_story(genre, tone, character, setting, theme):
    """Generates a story and corresponding images based on user inputs."""
    try:
        if not theme or theme == "Surprise me!":
            themes_list = str(story_planner.run("List five creative fantasy story themes."))
            theme = themes_list.split("\n")[0] if "\n" in themes_list else "Mystical Quest"
        
        story_prompt = (
            f"Write a {tone} {genre} story in English. "
            f"The main character is {character}, and the setting is {setting}. "
            f"The theme of the story is: {theme}. Keep it immersive, creative, and engaging."
        )
        story_text = str(story_writer.run(story_prompt))
        
        # Generate illustration descriptions
        illustration_prompt = f"Describe three key visual scenes for this story: {story_text}"
        illustration_response = str(story_illustrator.run(illustration_prompt))
        illustration_descriptions = illustration_response.split("\n")[:3]

        # Generate images
        images = []
        for desc in illustration_descriptions:
            try:
                img_result = str(image_generator.run(f"Generate an image for this scene: {desc}"))
                images.append(img_result)
            except Exception:
                images.append(None)

        return story_text, [img for img in images if img]

    except Exception as e:
        return f"An error occurred: {str(e)}", []
