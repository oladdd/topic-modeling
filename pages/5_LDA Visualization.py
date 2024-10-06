import streamlit as st
import matplotlib.pyplot as plt
import gensim
from gensim import corpora
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Predefined datasets
DATASETS = {
        "Customer Reviews": [
        'The product is excellent and works as expected. I have been using it for a month now, and it has consistently performed well, making my life easier and more organized. Additionally, I appreciate the great customer support and the product’s durability, which is essential for long-term use.',
        'Terrible service, would not recommend. I ordered a product that arrived late, and when I contacted customer service, they were unhelpful and dismissive. Overall, my experience was frustrating, and I would advise others to look elsewhere for better service.',
        'Absolutely love this! Will buy again. The quality is top-notch, and it exceeded my expectations in every way. The product functions perfectly, and I was pleasantly surprised by how user-friendly it is. Highly recommend it to anyone looking for reliability.',
        'Not worth the price, poor quality. The item broke within a few days of use, and I feel like I wasted my money on something that was not durable at all. Despite the appealing advertisement, it did not live up to the hype and was a letdown.',
        'Shipping was quick and the product is decent. It functions well for basic tasks, but it lacks some of the features that I was hoping for based on the description. While it’s an acceptable choice, I believe there are better options available.',
        'Customer support was very helpful. They assisted me promptly with my inquiries and provided solutions that actually worked, which was refreshing. Their commitment to customer satisfaction made a significant difference in my overall experience.',
        'Received a faulty item, disappointing. The item did not work as advertised, and I had to go through a lengthy return process to get a replacement. This experience was very frustrating and made me hesitant to purchase again from this brand.',
        'Exceeded my expectations, fantastic! The quality and performance of this product are far superior to others I have tried in the past. The design is sleek and efficient, making it a great addition to my routine. Highly recommended!',
        'The app interface is user-friendly and intuitive. I found it easy to navigate, which made my experience enjoyable from start to finish. The features are well-organized, and I had no trouble figuring out how to utilize all the tools available.',
        'The worst experience I have ever had with this company. I faced numerous issues with my order, and their customer service was unresponsive throughout the process. I would not recommend them to anyone looking for reliable service.'
    ],
    "Tech Articles": [
        'Artificial Intelligence is the future of technology. It has the potential to transform industries by automating tasks, providing insights, and improving decision-making processes in real-time. As businesses adopt AI, they can achieve greater efficiency and innovation.',
        'Quantum computing will revolutionize industries, enabling computations that were previously thought to be impossible. Its impact on fields such as cryptography and data analysis will be profound, leading to breakthroughs that can reshape our understanding of technology.',
        'Virtual Reality offers a new way to experience entertainment, allowing users to immerse themselves in virtual environments that feel real. This technology is changing the way we interact with media, providing opportunities for enhanced engagement and interactivity.',
        'The rise of cloud computing in enterprise has provided businesses with the flexibility to scale their operations seamlessly. It has also fostered collaboration among teams located in different parts of the world, making remote work more efficient and effective.',
        'Machine learning improves data analysis accuracy by utilizing algorithms that learn from data. This enables organizations to derive actionable insights that were not possible with traditional methods, ultimately leading to better business outcomes.',
        'Blockchain is disrupting traditional finance by providing a decentralized ledger that enhances security and transparency in transactions. This technology is set to redefine how we think about money, ownership, and trust in digital interactions.',
        '5G technology boosts internet speed and connectivity, making it possible to support a greater number of devices. This advancement will facilitate the growth of smart cities and IoT applications, providing a foundation for future innovations.',
        'Edge computing is growing in importance as it allows data to be processed closer to the source. This reduces latency and improves response times for applications that require real-time data processing, making it essential for industries like healthcare and finance.',
        'Advances in cybersecurity are crucial in the digital age as threats continue to evolve. Organizations must adopt proactive measures to safeguard their data and systems from potential attacks, ensuring the integrity and confidentiality of information.',
        'The ethical concerns surrounding autonomous vehicles are significant as we consider the implications of machines making life-and-death decisions. Discussions about accountability and safety are paramount as we navigate the future of transportation.'
    ],
    "Sports News": [
        'The team played an excellent match and dominated the field with their strategic gameplay. Their coordinated efforts led to a thrilling victory, showcasing their skills and teamwork throughout the game, and their fans were ecstatic with the performance.',
        'The star player suffered a severe injury, putting them out for the season. This has raised concerns among fans about the team’s ability to perform without their key player in future matches, and many are speculating about the potential impacts on their strategy.',
        'A thrilling finish to the championship game left fans on the edge of their seats. The last-minute goal secured the team’s victory and solidified their status as champions, highlighting the importance of perseverance and teamwork in sports.',
        'Controversial referee decision costs team the game, leading to heated discussions among fans and analysts. Many believe the decision was unjust and could have changed the outcome of the match, stirring up debates in the sports community.',
        'The new coach is making a significant impact on the team’s performance, implementing innovative strategies that are paying off. Players have responded positively to his leadership and guidance, showcasing improvement in their skills and teamwork.',
        'Fans are eagerly awaiting the start of the new season, anticipating thrilling matches and showcasing new talent. The excitement is palpable as teams prepare for the challenges ahead, and supporters are hopeful for a successful year.',
        'The athlete broke the world record in the 100-meter race, delivering an impressive performance that left spectators in awe. This achievement highlights the athlete’s hard work and dedication, setting a new standard for excellence in the sport.',
        'A surprising upset in the tournament’s final round caught everyone off guard. The underdog team managed to defeat the favorite, proving that anything is possible in sports and creating a memorable moment for fans.',
        'The team’s defense strategy was flawless, preventing their opponents from scoring throughout the match. Their solid performance has set a new standard for defensive play in the league, and they are now regarded as a formidable opponent.',
        'The transfer market is heating up with big-name moves, sparking excitement among fans about potential changes in team dynamics. These trades could significantly influence the upcoming season and alter the competition landscape.'
    ]
}

def lda_visualization():
    st.title("🔍 Interactive LDA Visualization")

    st.markdown("""    
    ---    
    ### Explore LDA Topic Modeling    
    On this page, you'll interact with the **Latent Dirichlet Allocation (LDA)** model.    
    You can:    
    1. Select a **predefined dataset**.    
    2. Adjust the **number of topics** for the LDA model.    
    3. Control the **number of passes** for the model.    
    ---    
    """)

    # Dataset selection
    dataset_choice = st.selectbox("Choose a dataset", list(DATASETS.keys()))

    # Display documents from the selected dataset
    st.markdown(f"### 📄 Documents in the **{dataset_choice}** dataset:")
    documents = DATASETS[dataset_choice]
    
    for i, doc in enumerate(documents):
        st.write(f"**Document {i+1}:** {doc}")

    # Number of topics selection
    num_topics = st.slider("Select the number of topics", min_value=2, max_value=10, value=3)

    # Number of passes (iterations) selection
    passes = st.slider("Select the number of passes (training iterations)", min_value=1, max_value=20, value=10)

    # Remove stopwords using NLTK
    stop_words = set(stopwords.words('english'))
    texts = [[word for word in doc.lower().split() if word not in stop_words] for doc in documents]
    
    # Create a dictionary and corpus
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # LDA model
    lda_model = gensim.models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)

    # Visualization using Matplotlib
    st.markdown("### 📊 LDA Topics Visualization")
    
    # Explanation of the bar charts
    st.write("The following bar charts represent the topics identified by the LDA model. Each bar indicates the weight of a word in relation to the topic. A higher weight suggests a stronger connection between the word and the topic.")

    # Get the topics and their words
    topics = lda_model.show_topics(num_topics=num_topics, formatted=False)
    
    for topic_num, topic_words in topics:
        words, weights = zip(*topic_words)

        # Create a bar chart for each topic
        plt.figure(figsize=(8, 4))
        plt.barh(words, weights, color='skyblue')
        plt.xlabel('Weight')
        plt.title(f'Topic {topic_num}')
        plt.xlim(0, max(weights) + 0.1)  # Add some space to the right of the bars
        st.pyplot(plt)
        plt.close()  # Close the plot to avoid displaying it twice

    # Model summary
    st.markdown("### 🧠 LDA Model Summary")
    st.write(f"**Selected Dataset**: {dataset_choice}")
    st.write(f"**Number of Topics**: {num_topics}")
    st.write(f"**Number of Passes (Iterations)**: {passes}")

if __name__ == '__main__':
    lda_visualization()
