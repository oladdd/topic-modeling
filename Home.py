import streamlit as st

def app():
    st.title("🌐 **Interactive Topic Modeling** 🌐")
    
    # Introduce the concept with an appealing introduction
    st.markdown("""
    ---
    ### 🎯 **What is Topic Modeling?**
   Topic modeling is a technique to **automatically uncover hidden themes** in large text datasets.   
   
    💡 Imagine a library where you can instantly see the main topics in each book without reading everything!

    ---
    """)
    
    # Include an informative image related to data science or text analysis
    st.image("https://cdn.botpenguin.com/assets/website/Topic_Modeling_35bd15572c.webp", caption="Visualizing Topic Clusters in Data")

    st.markdown("""
    ---  
    ### 🔍 **How Does it Work?**  
    Topic models like **LDA** and **TF-IDF** help identify patterns in text:  
    - 🧠 **LDA**: Groups words that frequently appear together into topics.  
    - 📈 **TF-IDF**: Measures word importance in a document compared to the entire dataset.  
    These models show the hidden structure of the text, similar to how our minds categorize ideas.
    ---  
    """)

    # Interactive section
    st.markdown("### 🎮 **Ready to Explore?**")
    if st.button("🚀 Start Learning!"):
        st.success("Use the menu to access lessons, games, and quizzes! 🎉")

if __name__ == '__main__':
    app()