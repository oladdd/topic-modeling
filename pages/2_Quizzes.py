import streamlit as st

def app():
    # Intro description
    st.title("🎮 **Welcome to Two-Pic Modeling!** 🎮")

    st.markdown(""" 
    --- 
    ### What is Two-Pic Modeling?  
    **Two-Pic Modeling** is an interactive game inspired by **topic modeling**. In topic modeling, algorithms analyze documents and group them by identifying hidden themes. In this game, documents were replaced with **pictures**.  
    Just like words in a document, these images represent abstract ideas, and your goal is to group them into the correct **topic clusters**.

    **Instructions:**  
    - You'll be presented with **two images** side-by-side in each round.
    - Choose the correct **topic cluster** for the images.
    - Each cluster represents a different theme, just like in topic modeling!

    Let’s begin and see how well you can classify these images! 🚀 
    --- 
    """)

    # Define total number of rounds
    total_rounds = 5  

    # Define the rounds with specific images and clusters
    rounds_data = [
        {
            "images": ["data/1img1.png", "data/1img2.png"],
            "clusters": [
                "Cluster 1: Park, Grass, Families, Outdoors",
                "Cluster 2: Mountains, Snowboarding, Hiking, Scenery",
                "Cluster 3: City, Urban, Buildings, Nightlife",
                "Cluster 4: Beach, Ocean, Relaxation, Vacation"
            ],
            "correct": "Cluster 1: Park, Grass, Families, Outdoors"
        },
        {
            "images": ["data/2img1.png", "data/2img2.png"],
            "clusters": [
                "Cluster 1: Music, Instruments, Melody, Concerts",
                "Cluster 2: Movies, Films, Actors, Theater",
                "Cluster 3: Video Games, Players, Virtual World, Strategy",
                "Cluster 4: Books, Reading, Stories, Literature"
            ],
            "correct": "Cluster 3: Video Games, Players, Virtual World, Strategy"
        },
        {
            "images": ["data/3img1.png", "data/3img2.png"],
            "clusters": [
                "Cluster 1: Science, Technology, Advancement, Innovation",  # Changed to correct cluster
                "Cluster 2: Environment, Sustainability, Ecology, Nature",
                "Cluster 3: Religion, Spirituality, Rituals, Beliefs",
                "Cluster 4: Urban, Infrastructure, Development, Modernization"
            ],
            "correct": "Cluster 1: Science, Technology, Advancement, Innovation"  # This is now the correct option
        },
        {
            "images": ["data/4img1.png", "data/4img2.png"],
            "clusters": [
                "Cluster 1: Commerce, Trade, Market, Exchange",
                "Cluster 2: Festivals, Celebration, Tradition, Community",
                "Cluster 3: City, Urban, Buildings, Nightlife",
                "Cluster 4: Art, Creativity, Exhibitions, Design"
            ],
            "correct": "Cluster 1: Commerce, Trade, Market, Exchange"
        },
        {
            "images": ["data/5img1.png", "data/5img2.png"],
            "clusters": [
                "Cluster 1: Science, Exploration, Phenomena",
                "Cluster 2: Quantum Physics, Theory, Paradoxes",
                "Cluster 3: Singularity, Reality, Dimensions, Cyberpunk",
                "Cluster 4: Sci-Fi, Dystopia, Alternate Realities"
            ],
            "correct": "Cluster 4: Sci-Fi, Dystopia, Alternate Realities"
        }
    ]

    # Start the rounds of the game
    for round_num in range(total_rounds):
        st.markdown(f"### Round {round_num + 1}")

        # Display images for the current round
        st.image(rounds_data[round_num]["images"], width=300, caption=["Image 1", "Image 2"])

        # Radio button for cluster selection with a blank default option
        cluster_option = st.radio("Which cluster do these images belong to?", 
                                   ["",  # Blank option
                                    *rounds_data[round_num]["clusters"]], 
                                   key=f"radio_{round_num}")

        # Button for submitting the answer
        if st.button(f"Submit Round {round_num + 1}"):
            if cluster_option == "":
                st.warning("Please select an answer.")  # Prompt for selection
            elif cluster_option == rounds_data[round_num]["correct"]:
                st.success("✅ Correct!")
            else:
                st.error("❌ Try again.")

if __name__ == '__main__':
    app()
