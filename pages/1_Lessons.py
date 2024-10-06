import streamlit as st

def app():
    st.title("📘 **Introduction to Topic Modeling** 📘")

    # Introduction
    st.markdown("""
    Welcome to the interactive lessons on **Topic Modeling**! This technique uncovers hidden themes in large text collections. One key method is **LDA (Latent Dirichlet Allocation)**. 🎯
    """)

    # Lesson 1: What is Topic Modeling?
    st.markdown("## 🧠 **Lesson 1: What is Topic Modeling?**")
    st.markdown("""
    Topic modeling groups large amounts of text into themes by:
    - 📊 **Summarizing**: Quickly highlights main ideas.
    - 🔍 **Finding Patterns**: Reveals recurring themes in text.
    - 📝 **Categorizing**: Automatically organizes content.
    """)

    st.markdown("""
    **Example**: Automatically group thousands of **customer reviews** into themes like quality, service, or price.
    """)

    # Lesson 2: What is LDA (Latent Dirichlet Allocation)?
    st.markdown("## 🧑‍💻 **Lesson 2: What is LDA (Latent Dirichlet Allocation)?**")
    st.markdown("""
    **LDA** is an algorithm that scans documents for word patterns and groups them into **topics**:
    - 🧠 Finds words that frequently appear together.
    - 🔄 Automatically assigns topics to documents.
    """)

    st.markdown("""
    **Example**: In news articles, LDA might group "election," "government," and "policy" into one topic, and "soccer," "match," and "goal" into another.
    """)

    # Quiz on LDA
    st.markdown("### 📝 **Quick Check: What does LDA do?**")
    answer = st.radio("Choose an answer:", ["", "Assigns random topics", "Groups documents by word patterns", "Manually categorizes text"], index=0)
    
    if answer == "":
        st.warning("Please select an answer.")
    elif answer == "Groups documents by word patterns":
        st.success("✅ Correct! LDA finds topics based on word patterns.")
    else:
        st.error("❌ Incorrect. LDA doesn't categorize text manually.")

    # Lesson 3: What is TF-IDF (Term Frequency-Inverse Document Frequency)?
    st.markdown("## 📊 **Lesson 3: What is TF-IDF (Term Frequency-Inverse Document Frequency)?**")
    st.markdown("""
    **TF-IDF** is a method that identifies important words by considering:
    - **TF (Term Frequency)**: How often a word appears in the document.
    - **IDF (Inverse Document Frequency)**: How rare the word is across documents.
    """)

    # TF-IDF quick check
    st.markdown("### 📝 **Quick Check: Which word has a higher TF-IDF score?**")
    answer_2 = st.radio("Choose an answer:", ["", "'the' in an article", "'machine learning' in a research paper"], index=0)
    
    if answer_2 == "":
        st.warning("Please select an answer.")
    elif answer_2 == "'machine learning' in a research paper":
        st.success("✅ Correct! 'Machine learning' is more unique and important.")
    else:
        st.error("❌ Incorrect. Common words like 'the' have lower significance.")

    # TF-IDF use case
    with st.expander("🔎 **Where is TF-IDF Used?**"):
        st.markdown("""
        **TF-IDF** is used in search engines to rank relevant documents and in text mining to find important words in large datasets.
        """)

if __name__ == '__main__':
    app()
