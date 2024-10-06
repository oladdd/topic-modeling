import streamlit as st

def app():
    st.title("📘 **Topic Modeling Lessons** 📘")

    # Introduction to Topic Modeling
    st.markdown("""
    Welcome to the interactive lesson on **Topic Modeling**! This powerful technique helps uncover hidden patterns and themes in large text datasets. By grouping similar words and documents, topic modeling saves time and offers meaningful insights from unstructured data. One of the most commonly used techniques is **LDA (Latent Dirichlet Allocation)**. 🎯
    """)

    # Lesson 1: What is Topic Modeling?
    st.markdown("""
                ---
                ## 🧠 **Lesson 1: What is Topic Modeling?**
                """)
    st.markdown("""
    Topic modeling is a method used to discover abstract topics within large collections of text. Instead of manually categorizing the data, **topic modeling automatically groups words and documents** into relevant themes, making it a powerful tool for processing unstructured text.

    ### Why is Topic Modeling Important?
    - **📊 Summarization**: It helps condense huge amounts of text into manageable topics.
    - **🔍 Pattern Discovery**: It reveals frequently discussed themes that may not be immediately obvious.
    - **📝 Automatic Categorization**: It categorizes the content without human intervention, making it efficient and scalable.
    """)

    st.markdown("""
    **Example**: Suppose you have thousands of customer reviews on an e-commerce website. Topic modeling can automatically group them into categories like **product quality**, **customer service**, and **pricing**, helping the company focus on key areas of customer feedback.
    """)

    # Expand on where Topic Modeling is used
    with st.expander("🔎 **Where is Topic Modeling Used?**"):
        st.markdown("""
        - **Customer Feedback Analysis**: Automatically categorizing reviews into common themes.
        - **News Aggregation**: Grouping similar news articles into distinct topics like politics, sports, or technology.
        - **Academic Research**: Sorting academic papers into fields or subjects without manually tagging them.
        - **Social Media Analysis**: Discovering trending themes or concerns in social media posts.
        """)

    # Lesson 2: What is LDA (Latent Dirichlet Allocation)?
    st.markdown("""
                --- 
                ## 🧑‍💻 **Lesson 2: What is LDA (Latent Dirichlet Allocation)?**
                
                """)
    st.markdown("""
    **LDA** is one of the most popular algorithms used for topic modeling. It works by analyzing the patterns of words that appear together in documents and grouping them into **topics**. It assumes each document consists of a mixture of topics, and each topic is a mixture of words.

    ### Key Concepts of LDA:
    - **🧠 Word Patterns**: LDA identifies patterns of word co-occurrence across documents.
    - **🔄 Topic Assignment**: LDA assigns each document to a set of topics based on these word patterns.
    """)

    st.markdown("""
    **Example**: In a news dataset, LDA might group the words "election", "vote", "government" into a **politics** topic and the words "team", "match", "goal" into a **sports** topic.
    """)

    # Expanding on LDA workings
    with st.expander("🔎 **How Does LDA Work?**"):
        st.markdown("""
        LDA works by:
        - **Generating Topics**: It assumes each document contains multiple topics and that each word belongs to one of these topics.
        - **Distribution of Words**: LDA calculates the probability that a word belongs to a topic and assigns topics to documents accordingly.
        - **Iterative Refinement**: Through multiple iterations, LDA adjusts topic assignments until the patterns of words are stable.
        """)

    # Quiz on LDA
    st.markdown("### 📝 **Quick Check: What does LDA do?**")
    answer_lda = st.radio("Choose an answer:", ["", "Assigns random topics", "Groups documents by word patterns", "Manually categorizes text"], index=0)
    
    if answer_lda == "":
        st.warning("Please select an answer.")
    elif answer_lda == "Groups documents by word patterns":
        st.success("✅ Correct! LDA uses word patterns to group documents automatically.")
    else:
        st.error("❌ Incorrect. LDA doesn't manually categorize text or assign random topics.")

    # Lesson 3: What is TF-IDF (Term Frequency-Inverse Document Frequency)?
    st.markdown("""
                --- 
                ## 📊 **Lesson 3: What is TF-IDF (Term Frequency-Inverse Document Frequency)?**
                """)
    st.markdown("""
    **TF-IDF** is a technique used to measure how important a word is in a document, relative to a collection of documents. It highlights words that are more unique and significant within the text, allowing us to focus on the key terms in each document.

    ### TF-IDF Components:
    - **TF (Term Frequency)**: Measures how frequently a word appears in a document. Words that appear more frequently in a document get a higher score.
    - **IDF (Inverse Document Frequency)**: Measures how rare a word is across all documents. If a word appears in many documents, it receives a lower score.
    """)

    st.markdown("""
    **Example**: In a corpus of research papers, the word "algorithm" might appear frequently in one document and rarely across others, giving it a higher TF-IDF score. Meanwhile, common words like "the" and "is" receive lower scores.
    """)

    # Expanding on the use cases of TF-IDF
    with st.expander("🔎 **Where is TF-IDF Used?**"):
        st.markdown("""
        **TF-IDF** is widely used in:
        - **Search Engines**: To rank web pages by relevance to a search query.
        - **Text Mining**: To identify the most important words in a text.
        - **Document Classification**: To classify documents based on key terms.
        """)

    # TF-IDF quick check
    st.markdown("### 📝 **Quick Check: Which word would likely have a higher TF-IDF score?**")
    answer_tfidf = st.radio("Choose an answer:", ["", "'the' in an article", "'machine learning' in a research paper"], index=0)
    
    if answer_tfidf == "":
        st.warning("Please select an answer.")
    elif answer_tfidf == "'machine learning' in a research paper":
        st.success("✅ Correct! 'Machine learning' is more unique and relevant to the paper.")
    else:
        st.error("❌ Incorrect. Common words like 'the' have a lower TF-IDF score.")

if __name__ == '__main__':
    app()
