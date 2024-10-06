import streamlit as st

def app():
    st.title("📝 **Topic Modeling Quizzes**")

    # Quiz 1: LDA Full Form
    st.markdown("### 1️⃣ What does LDA stand for?")
    answer_lda = st.radio("Choose an answer:", ["", "Latent Data Algorithm", "Latent Dirichlet Allocation", "Linear Document Analysis"], index=0)
    
    if answer_lda == "":
        st.warning("Please select an answer.")
    elif answer_lda == "Latent Dirichlet Allocation":
        st.success("✅ Correct! LDA stands for Latent Dirichlet Allocation.")
    else:
        st.error("❌ Incorrect. LDA stands for Latent Dirichlet Allocation.")

    # Quiz 2: Purpose of LDA
    st.markdown("### 2️⃣ What does LDA do?")
    answer_lda_purpose = st.radio("Choose an answer:", ["", "Manually assigns topics to documents", "Groups documents based on word patterns", "Summarizes document length"], index=0)
    
    if answer_lda_purpose == "":
        st.warning("Please select an answer.")
    elif answer_lda_purpose == "Groups documents based on word patterns":
        st.success("✅ Correct! LDA groups documents based on word patterns.")
    else:
        st.error("❌ Incorrect. LDA automatically groups documents based on word patterns.")

    # Quiz 3: Full Form of TF-IDF
    st.markdown("### 3️⃣ What does TF-IDF stand for?")
    answer_tfidf = st.radio("Choose an answer:", ["", "Term Frequency-Inverse Document Frequency", "Text Frequency-Information Document Factor", "Total Frequency-Inverse Document Factor"], index=0)
    
    if answer_tfidf == "":
        st.warning("Please select an answer.")
    elif answer_tfidf == "Term Frequency-Inverse Document Frequency":
        st.success("✅ Correct! TF-IDF stands for Term Frequency-Inverse Document Frequency.")
    else:
        st.error("❌ Incorrect. TF-IDF stands for Term Frequency-Inverse Document Frequency.")

    # Quiz 4: Function of TF-IDF
    st.markdown("### 4️⃣ What is the purpose of TF-IDF?")
    answer_tfidf_purpose = st.radio("Choose an answer:", ["", "Count the total words in a document", "Measure word importance based on its frequency", "Identify all nouns in a document"], index=0)
    
    if answer_tfidf_purpose == "":
        st.warning("Please select an answer.")
    elif answer_tfidf_purpose == "Measure word importance based on its frequency":
        st.success("✅ Correct! TF-IDF measures the importance of a word based on how often it appears and how rare it is across documents.")
    else:
        st.error("❌ Incorrect. TF-IDF measures word importance based on frequency and rarity.")

    # Quiz 5: Use Case of LDA
    st.markdown("### 5️⃣ In which scenario would you use LDA?")
    answer_lda_use = st.radio("Choose an answer:", ["", "To group similar news articles into topics", "To measure the frequency of common words like 'the'", "To manually tag documents with labels"], index=0)
    
    if answer_lda_use == "":
        st.warning("Please select an answer.")
    elif answer_lda_use == "To group similar news articles into topics":
        st.success("✅ Correct! LDA is great for grouping large collections of documents, like news articles, into topics based on word patterns.")
    else:
        st.error("❌ Incorrect. LDA is used for automatically grouping documents into topics based on patterns.")

if __name__ == '__main__':
    app()