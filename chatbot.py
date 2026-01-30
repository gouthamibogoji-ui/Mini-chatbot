import streamlit as st
from nltk.chat.util import Chat, reflections # type: ignore

# -------------------------------
# Chatbot patterns
# -------------------------------
pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, how are you today?"]],
    [r"(.*)help(.*)", ["I can help you. Please tell me your issue."]],
    [r"(.*) your name ?", ["My name is Chatbot, you can call me robot 🤖"]],
    [r"how are you (.*)\??", ["I'm doing very well!", "I am great!"]],
    [r"sorry (.*)", ["It's alright.", "No worries 🙂"]],
    [r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that!", "Great 👍"]],
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello 👋", "Hey there!"]],
    [r"who are you ?", ["I'm a rule-based chatbot built using Python and NLTK"]],
    [r"how old are you ?", ["I don't have an age. I was created recently 😄"]],
    [r"are you human ?", ["Nope! I'm a chatbot, but I try to sound friendly 🙂"]],
    [r"sorry (.*)", ["It's alright.", "No worries 🙂"]],
    [r"thank you(.*)", ["You're welcome!", "Happy to help 😄"]],
    [r"do you like me ?", ["Of course! I enjoy talking to you 😊"]],
    [r"can we be friends ?", ["Yes! I'm always happy to chat with you 🤝"]],
    [r"(.*)help(.*)", ["I can help you. Please tell me your issue."]],
    [r"what can you do ?", ["I can chat with you, answer simple questions."]],
    [r"do you sleep ?", ["I never sleep. I'm always available!"]],
    [r"(.*)python(.*)", ["Python is a powerful and beginner-friendly programming language 🐍"]],
    [r"(.*)machine learning(.*)", ["Machine learning allows systems to learn from data without explicit programming."]],
    [r"(.*)artificial intelligence(.*)", ["AI enables machines to mimic human intelligence 🤖"]],
    [r"(.*)nlp(.*)", ["NLP stands for Natural Language Processing. It helps computers understand text."]],
    [r"(.*)streamlit(.*)", ["Streamlit helps you build web apps for data science easily"]],
    [r"(.*)nltk(.*)", ["NLTK is a popular Python library for text processing."]],
    [r"(.*)error(.*)", ["Errors are common in coding. Please read the error message carefully."]],
    [r"(.*)debug(.*)", ["Try printing variables or using a debugger to find the issue."]],
    [r"(.*)(sports|game|sport)(.*)", ["I'm a big fan of Cricket 🏏"]],
    [r"who (.*) (cricketer|batsman)?", ["Virat Kohli 🏏"]],
    [r"tell me a joke", ["Why do programmers love Python? Because it's easy to *byte* 🐍😄"]],
    [r"tell me something interesting", ["Python was named after Monty Python, not the snake!"]],
    [r"do you like music ?", ["I like all kinds of music, especially digital beats 🎵"]],
    [r"(.*)career(.*)", ["Choose a career you enjoy and keep learning every day 🌱"]],
    [r"(.*)job(.*)", ["Upskill yourself regularly to grow in your career."]],
    [r"(.*)motivate(.*)", ["Believe in yourself. Consistency beats talent 💪"]],
    [r"(.*) (location|city) ?", ["Hyderabad, India"]],
    [r"(.*)created(.*)", ["Gouthami created me using Python's NLTK library.", "Top secret 😉"]],
    [r"today summer or winter", ["Hopes! Today is winter"]],
    [r"quit|bye|goodbye", ["Bye! See you soon 👋", "It was nice talking to you 😊"]],

    # -------------------------------
    # Fallback (ALWAYS LAST)
    # -------------------------------
    [r"(.*)", ["Our customer service will reach you."]]
]
chatbot = Chat(pairs, reflections)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Chatbot", page_icon="🎤")
st.title("🤖 Rule based chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Chat Bubble Styling
# -------------------------------

st.markdown("""
<style>
/* Full app background */
.stApp {
    background-image: url("assets/background.jpg");
    background-size: cover;        /* fill screen */
    background-position: center;
    background-repeat: no-repeat;
}

/* Optional: add soft overlay for readability */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(255, 255, 255, 0.6);  /* opacity */
    z-index: -1;
}

/* Chat bubbles */
.user {
    background-color: #DCF8C6;
    color: black;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    width: fit-content;
    max-width: 70%;
    align-self: flex-end;
}

.bot {
    background-color: #F1F0F0;
    color: black;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    width: fit-content;
    max-width: 70%;
}

.chat {
    display: flex;
    flex-direction: column;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Text Input
# -------------------------------
user_text = st.text_input("💬 Type your message")

if user_text:
    user_text = user_text.lower()
    bot_reply = chatbot.respond(user_text)

    st.session_state.messages.append(("user", user_text))
    st.session_state.messages.append(("bot", bot_reply))

# -------------------------------
# Display Chat Bubbles
# -------------------------------
st.markdown("<div class='chat'>", unsafe_allow_html=True)

for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"<div class='user'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>🤖 {msg}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
