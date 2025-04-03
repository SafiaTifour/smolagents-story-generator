import gradio as gr
from story import generate_story

def gradio_interface(genre, tone, character, setting, theme):
    """Handles interaction between UI and story generation function."""
    story, images = generate_story(genre, tone, character, setting, theme)
    return story, images

def launch_ui():
    """Launches the Gradio UI for the AI Story Generator."""
    with gr.Blocks(css="body {background-color: #f9f9f9;} .gradio-container {max-width: 800px; margin: auto;}") as demo:
        gr.Markdown("""
        # 📖 AI Fantasy Story Generator ✨
        _Create a unique fantasy adventure with AI-generated illustrations._
        """)

        with gr.Row():
            with gr.Column():
                genre = gr.Dropdown(["Fantasy", "Sci-Fi", "Mystery", "Adventure", "Mythology"], label="📜 Genre")
                tone = gr.Radio(["Epic", "Dark", "Whimsical", "Humorous", "Mysterious"], label="🎭 Tone")
                character = gr.Dropdown(
                    ["A lost knight", "A young magician", "A rogue scientist", "A cosmic traveler", "An immortal being"], 
                    label="🧙 Main Character"
                )
                setting = gr.Dropdown(
                    ["A floating city", "A hidden underground world", "A parallel universe", "An ancient temple", "A cyberpunk future"], 
                    label="🌍 Setting"
                )
                theme = gr.Radio(
                    ["Hero's Journey", "Lost Civilization", "Time Travel", "Magical Realism", "Surprise me!"], 
                    label="🎨 Theme"
                )
                generate_btn = gr.Button("🚀 Generate Story")

            with gr.Column():
                story_output = gr.Textbox(label="📝 Your Story", lines=10, interactive=False)
                image_gallery = gr.Gallery(label="🎨 Illustrations")

        generate_btn.click(gradio_interface, [genre, tone, character, setting, theme], [story_output, image_gallery])

    demo.launch()
