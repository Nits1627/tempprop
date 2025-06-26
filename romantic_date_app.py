import streamlit as st
import datetime
import json
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time

# Page configuration
st.set_page_config(
    page_title="My Heart's Invitation 💕",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Advanced CSS with romantic animations and effects
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Poppins:wght@300;400;600;700&display=swap');
    
    .main {
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 25%, #fad0c4 50%, #ffd1ff 75%, #ff9a9e 100%);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        padding: 0;
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 25%, #fad0c4 50%, #ffd1ff 75%, #ff9a9e 100%);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating hearts animation */
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    }
    
    .heart {
        position: absolute;
        font-size: 20px;
        color: rgba(255, 105, 180, 0.8);
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }
    
    .romantic-header {
        text-align: center;
        color: #2c3e50;
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem;
        text-shadow: 3px 3px 6px rgba(255,255,255,0.8);
        margin: 2rem 0;
        font-weight: 700;
        position: relative;
        z-index: 10;
        animation: titleGlow 3s ease-in-out infinite alternate;
    }
    
    @keyframes titleGlow {
        0% { text-shadow: 3px 3px 6px rgba(255,255,255,0.8), 0 0 20px rgba(255, 105, 180, 0.3); }
        100% { text-shadow: 3px 3px 6px rgba(255,255,255,0.8), 0 0 30px rgba(255, 105, 180, 0.6); }
    }
    
    .heart-decoration {
        text-align: center;
        font-size: 2.5rem;
        margin: 2rem 0;
        animation: heartbeat 2s ease-in-out infinite;
        filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.5));
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        25% { transform: scale(1.1) rotate(-5deg); }
        50% { transform: scale(1.2); }
        75% { transform: scale(1.1) rotate(5deg); }
    }
    
    .romantic-text {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 2.5rem;
        border-radius: 25px;
        border: 3px solid transparent;
        background-image: linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)), 
                          linear-gradient(45deg, #ff69b4, #ff1493, #dc143c, #ff69b4);
        background-origin: border-box;
        background-clip: content-box, border-box;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(255, 105, 180, 0.3), 0 5px 15px rgba(0,0,0,0.1);
        color: #2c3e50;
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .romantic-text::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transform: rotate(45deg);
        transition: all 0.6s;
        opacity: 0;
    }
    
    .romantic-text:hover::before {
        animation: shimmer 0.8s ease-in-out;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) rotate(45deg); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateX(100%) rotate(45deg); opacity: 0; }
    }
    
    .romantic-text:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 25px 50px rgba(255, 105, 180, 0.4), 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .movie-info {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 240, 245, 0.95) 100%);
        backdrop-filter: blur(15px);
        padding: 2.5rem;
        border-radius: 25px;
        margin: 2rem 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        border: 2px solid rgba(255, 105, 180, 0.3);
        color: #2c3e50;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .movie-info::after {
        content: '🎬';
        position: absolute;
        top: 20px;
        right: 20px;
        font-size: 3rem;
        opacity: 0.1;
        animation: rotate 10s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .movie-info:hover {
        transform: scale(1.03);
        box-shadow: 0 25px 50px rgba(255, 105, 180, 0.3);
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #ff69b4, #ff1493, #dc143c) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 1rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.4) !important;
        animation: buttonGlow 3s ease-in-out infinite !important;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        background-position: 100% 0 !important;
        box-shadow: 0 15px 35px rgba(255, 105, 180, 0.6) !important;
    }
    
    .cinema-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 25px;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .cinema-info::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: cinemaGlow 4s ease-in-out infinite;
    }
    
    @keyframes cinemaGlow {
        0%, 100% { transform: rotate(0deg); }
        50% { transform: rotate(180deg); }
    }
    
    .progress-bar-container {
        text-align: center; 
        margin: 2rem 0;
    }

    .progress-bar-background {
        background: rgba(255, 255, 255, 0.5);
        border-radius: 6px;
        padding: 4px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
    }
    
    .progress-bar {
        background: linear-gradient(45deg, #ff69b4, #ff1493);
        height: 10px;
        border-radius: 3px;
        transition: width 0.5s ease-in-out;
        box-shadow: 0 2px 10px rgba(255, 105, 180, 0.4);
        animation: progressPulse 2s ease-in-out infinite;
    }
    
    @keyframes progressPulse {
        0%, 100% { box-shadow: 0 2px 10px rgba(255, 105, 180, 0.4); }
        50% { box-shadow: 0 2px 20px rgba(255, 105, 180, 0.8); }
    }
    
    .map-button {
        background: linear-gradient(45deg, #4CAF50, #45a049, #2E7D32);
        background-size: 200% 200%;
        color: white;
        padding: 15px 30px;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 600;
        display: inline-block;
        margin: 10px 5px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.4);
        font-family: 'Poppins', sans-serif;
    }
    
    .map-button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 35px rgba(76, 175, 80, 0.6);
        background-position: 100% 0;
        text-decoration: none;
        color: white;
    }
    
    .footer-hearts {
        text-align: center;
        font-size: 2rem;
        margin-top: 3rem;
        color: #ff69b4;
        animation: footerPulse 3s ease-in-out infinite;
        font-family: 'Dancing Script', cursive;
        font-weight: 700;
    }
    
    @keyframes footerPulse {
        0%, 100% { opacity: 0.8; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.1); }
    }
    
    .love-meter {
        width: 100%;
        height: 20px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        overflow: hidden;
        position: relative;
        margin: 1rem 0;
    }
    
    .love-meter-fill {
        height: 100%;
        background: linear-gradient(45deg, #ff69b4, #ff1493);
        width: 0%;
        border-radius: 10px;
        transition: width 0.8s ease-out;
        position: relative;
    }
        
    .stTextArea > div > div > textarea, .stSelectbox > div > div, .stRadio > div {
        background: rgba(255, 255, 255, 0.95) !important;
        border: 2px solid #ff69b4 !important;
        border-radius: 15px !important;
        color: #2c3e50 !important;
        font-family: 'Poppins', sans-serif !important;
    }
        
    .custom-success {
        background: linear-gradient(45deg, #4CAF50, #81C784);
        color: white;
        padding: 1rem 2rem;
        border-radius: 15px;
        text-align: center;
        font-weight: 600;
        margin: 1rem 0;
        animation: successPulse 0.5s ease-out;
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3);
    }

    .custom-error {
        background: linear-gradient(45deg, #f44336, #e57373);
        color: white;
        padding: 1rem 2rem;
        border-radius: 15px;
        text-align: center;
        font-weight: 600;
        margin: 1rem 0;
        animation: successPulse 0.5s ease-out;
        box-shadow: 0 8px 25px rgba(244, 67, 54, 0.3);
    }

    @keyframes successPulse {
        0% { transform: scale(0.9); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
</style>

<div class="floating-hearts" id="floating-hearts"></div>

<script>
// Function to create and remove hearts
function createFloatingHearts() {
    const heartsContainer = document.getElementById('floating-hearts');
    if (!heartsContainer) return;

    const hearts = ['💕', '💖', '💝', '🌹', '✨', '💗'];
    
    // Create a heart every 500ms
    const heartInterval = setInterval(() => {
        if (Math.random() > 0.7) {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
            heart.style.animationDelay = Math.random() * 2 + 's';
            heartsContainer.appendChild(heart);
            
            // Remove heart after animation ends
            setTimeout(() => {
                if (heart.parentNode) {
                    heart.parentNode.removeChild(heart);
                }
            }, 8000);
        }
    }, 500);
}

// Run the function
if (document.getElementById('floating-hearts')) {
    createFloatingHearts();
}
</script>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'love_level' not in st.session_state:
    st.session_state.love_level = 0
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'final_answer' not in st.session_state:
    st.session_state.final_answer = None
if 'notification_sent' not in st.session_state:
    st.session_state.notification_sent = False


# --- NOTIFICATION FUNCTIONS ---
def get_notification_message(responses):
    """Formats the notification message."""
    return f"""
    💕 YOUR LOVE HAS RESPONDED! 💕
    --------------------------------------
    Here are the details of your upcoming date:

    🎬 Movie Date Response:
    ⏰ Chosen Time: {responses.get('time', 'Not selected')}
    🍽️ Dining Plan: {responses.get('dining', 'Not selected')}
    🍦 Ice Cream?: {responses.get('ice_cream', 'Not selected')}
    💖 Final Answer: {responses.get('final_answer', 'Not selected')}
    
    💌 Special Message from Them:
    "{responses.get('message', 'No message, just pure love!')}"
    --------------------------------------
    
    📅 Response Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    💕 Final Love Level: {st.session_state.love_level}/100
    
    Get ready for a magical date! 💝
    """

def send_webhook_notification(message):
    """Sends a notification via a webhook (e.g., Zapier to Slack/Discord)."""
    try:
        # Check if webhook URL is configured in secrets
        if 'webhook' in st.secrets and 'url' in st.secrets.webhook:
            webhook_url = st.secrets.webhook.url
            payload = {"text": message}
            requests.post(webhook_url, json=payload)
            return True
    except Exception as e:
        # Silently fail if webhook isn't set up
        print(f"Webhook notification failed: {e}")
    return False

def send_email_notification(subject, message_body):
    """Sends an email notification using credentials from st.secrets."""
    try:
        # Check if email credentials are fully configured in secrets
        if 'email_credentials' in st.secrets and all(k in st.secrets.email_credentials for k in ['USER_EMAIL', 'USER_PASSWORD', 'RECIPIENT_EMAIL']):
            creds = st.secrets.email_credentials
            sender_email = creds.USER_EMAIL
            receiver_email = creds.RECIPIENT_EMAIL
            password = creds.USER_PASSWORD

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message_body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            return True
        else:
            # Silently fail if credentials are not set up
            print("Email credentials not found in st.secrets. Skipping email notification.")
            return False
    except Exception as e:
        st.error(f"Oh no! A little glitch in sending the email: {e}. But don't worry, your response is safe with me!")
        return False

# --- UI HELPER FUNCTIONS ---
def show_progress(current_step, total_steps):
    """Displays a custom animated progress bar."""
    progress_percent = (current_step / total_steps) * 100
    st.markdown(f'''
    <div class="progress-bar-container">
        <p style="font-family: 'Dancing Script', cursive; font-size: 1.5rem; color: #2c3e50; margin-bottom: 1rem;">
            Our Love Story's Next Chapter 💕
        </p>
        <div class="progress-bar-background">
            <div class="progress-bar" style="width: {progress_percent}%;"></div>
        </div>
        <p style="font-family: 'Poppins', sans-serif; color: #666; margin-top: 0.5rem;">
            Step {current_step} of {total_steps} Complete
        </p>
    </div>
    ''', unsafe_allow_html=True)

def update_love_level(increment):
    """Updates and displays the love level meter."""
    st.session_state.love_level = min(100, st.session_state.love_level + increment)
    st.markdown(f'''
    <div class="love-meter">
        <div class="love-meter-fill" style="width: {st.session_state.love_level}%;"></div>
    </div>
    ''', unsafe_allow_html=True)


# --- APP LAYOUT AND LOGIC ---

# 1. HEADER
st.markdown('''
<div style="text-align: center; margin: 2rem 0;">
    <div class="heart-decoration">💝 💖 💝</div>
    <h1 class="romantic-header">My Heart's Special Invitation</h1>
    <p style="font-family: 'Dancing Script', cursive; font-size: 1.8rem; color: #2c3e50; margin: 1rem 0;">
        For the most wonderful person in my universe ✨
    </p>
    <div class="heart-decoration">🌹 💕 🌹</div>
</div>
''', unsafe_allow_html=True)

# 2. THE INVITATION MESSAGE
show_progress(1, 7)
st.markdown("""
<div class="romantic-text">
    <h3 style="color: #d63384; text-align: center; font-family: 'Dancing Script', cursive; font-size: 2.2rem;">
        My Dearest Love 💕
    </h3>
    <p style="font-size: 1.3rem; line-height: 1.8; text-align: center; color: #2c3e50; font-family: 'Poppins', sans-serif;">
        You know that feeling when a simple thought of someone makes your whole day brighter? That's what you do to me. 
        I've been dreaming of creating another perfect memory with you...
    </p>
    <p style="font-size: 1.3rem; line-height: 1.8; text-align: center; color: #2c3e50; font-family: 'Poppins', sans-serif;">
        So, I was thinking... how about we go on the most amazing date? We could watch <strong>"F1"</strong> at <strong>PVR, Andheri (W)</strong> this Saturday.
        Afterward, we can find a cozy place for dinner and maybe even share some ice cream while we talk about everything and nothing. 
        Just you, me, and the wonderful feeling of being together... 🦋
    </p>
    <p style="font-size: 1.2rem; text-align: center; color: #d63384; font-style: italic; margin-top: 1.5rem;">
        Because every moment with you feels like a beautiful dream. 💖
    </p>
</div>
""", unsafe_allow_html=True)

if 'love_level_step1' not in st.session_state:
    st.session_state.love_level_step1 = False
if not st.session_state.love_level_step1:
     if st.button("💕 This is so sweet! It made me smile! 💕", key="smile_button"):
        st.session_state.love_level_step1 = True
        st.session_state.love_level = min(100, st.session_state.love_level + 15)
        st.markdown('<div class="custom-success">Your smile is my favorite thing in the world! 😊✨</div>', unsafe_allow_html=True)
        st.balloons()
        time.sleep(0.5)
        st.rerun()

update_love_level(0) # Display the meter

# 3. CINEMA INFORMATION
show_progress(2, 7)
st.markdown("""
<div class="cinema-info">
    <h3 style="font-family: 'Dancing Script', cursive; font-size: 2.5rem;">🎬 Our Movie Destination 🎬</h3>
    <h4 style="font-size: 1.8rem; margin: 1rem 0;">PVR Citi Mall, Andheri (W)</h4>
    <p style="font-size: 1.2rem; line-height: 1.6;">
        I picked this place because it's perfect for us to get lost in a story together. We can share popcorn, laugh at the funny parts, 
        and honestly... I'll probably be watching you more than the screen! 🍿✨
    </p>
</div>
<div style="text-align: center; margin: 2rem 0;">
    <a href="https://www.google.com/maps/search/?api=1&query=PVR+Citi+Mall+Andheri+West+Mumbai" target="_blank" class="map-button">
        📍 See Our Cinema on Map
    </a>
</div>
""", unsafe_allow_html=True)

# 4. CHOOSE THE TIME
show_progress(3, 7)
with st.container():
    st.markdown('<div class="romantic-text">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-family: \"Dancing Script\", cursive; font-size: 2.2rem; color: #d63384;'>⏰ What time works for you?</h3>", unsafe_allow_html=True)
    time_option = st.radio(
        "Select a time for our movie date:",
        ('6:00 PM - The Sunset Show 🌇', '7:30 PM - The Prime Time Romance 💖', '9:00 PM - The Late Night Magic ✨', "Let's decide this together!"),
        key='time',
        index=None,
    )
    if time_option and 'time' not in st.session_state.responses:
        st.session_state.responses['time'] = time_option
        st.session_state.love_level = min(100, st.session_state.love_level + 15)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# 5. DINING OPTIONS
if 'time' in st.session_state.responses:
    show_progress(4, 7)
    with st.container():
        st.markdown('<div class="romantic-text">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center; font-family: \"Dancing Script\", cursive; font-size: 2.2rem; color: #d63384;'>🍽️ And for dinner...?</h3>", unsafe_allow_html=True)
        dining_option = st.radio(
            "What about food after the movie?",
            ("Yes, I'm starving! Let's have a proper dinner! 🍝", "Just some cozy snacks would be perfect! 🥨", "Let's see how we feel after the movie!"),
            key='dining',
            index=None,
        )
        if dining_option and 'dining' not in st.session_state.responses:
            st.session_state.responses['dining'] = dining_option
            st.session_state.love_level = min(100, st.session_state.love_level + 15)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# 6. ICE CREAM
if 'dining' in st.session_state.responses:
    show_progress(5, 7)
    with st.container():
        st.markdown('<div class="romantic-text">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center; font-family: \"Dancing Script\", cursive; font-size: 2.2rem; color: #d63384;'>🍦 One more thing...</h3>", unsafe_allow_html=True)
        ice_cream_option = st.radio(
            "Can I treat you to some ice cream? It's the perfect way to end a date!",
            ("Absolutely! You know my favorite flavor! 🍨", "I'd love that! ❤️", "Surprise me! ✨"),
            key='ice_cream',
            index=None
        )
        if ice_cream_option and 'ice_cream' not in st.session_state.responses:
            st.session_state.responses['ice_cream'] = ice_cream_option
            st.session_state.love_level = min(100, st.session_state.love_level + 15)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# 7. THE FINAL QUESTION
if 'ice_cream' in st.session_state.responses and st.session_state.final_answer is None:
    show_progress(6, 7)
    st.markdown("""
    <div class="romantic-text">
        <h3 style="text-align:center; font-family: 'Dancing Script', cursive; font-size: 2.5rem; color: #d63384;">
            So... The big question...
        </h3>
        <p style="font-size: 1.5rem; text-align: center; color: #2c3e50; font-family: 'Poppins', sans-serif; margin: 2rem 0;">
            Will you make me the happiest person and go on this date with me?
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! A thousand times YES! 💖", key="yes"):
            st.session_state.final_answer = "YES! A thousand times YES! 💖"
            st.session_state.love_level = 100 # Max out the love!
            st.balloons()
            st.rerun()
    with col2:
        if st.button("I'm not sure... 😢", key="no"):
            st.session_state.final_answer = "No"
            st.markdown('<div class="custom-error">Oh... Okay. 💔 Well, my offer always stands if you change your mind!</div>', unsafe_allow_html=True)
            # You could add more logic here if you wanted.

# 8. FINAL SUBMISSION FORM (IF YES)
if st.session_state.final_answer == "YES! A thousand times YES! 💖" and not st.session_state.notification_sent:
    show_progress(7, 7)
    update_love_level(0)
    st.markdown("""
    <div class="custom-success">
        <h2>YAY! You said YES! 🎉</h2>
        <p>My heart is literally doing backflips right now! I'm so incredibly excited for our date.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("final_submission_form"):
        st.markdown("""
        <div class="romantic-text">
            <h3 style="text-align:center; font-family: 'Dancing Script', cursive; font-size: 2.2rem; color: #d63384;">
                One last thing...
            </h3>
            <p style="text-align:center; font-family: 'Poppins', sans-serif;">
                Leave me a little message to make me even more excited! (If you want to!)
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        message = st.text_area("Your message:", placeholder="e.g., 'I'm so excited! Can't wait! ❤️'")
        
        submitted = st.form_submit_button("💌 Send My Response & Make Your Day!")

        if submitted:
            with st.spinner('Sending your lovely response... Please wait a moment...'):
                st.session_state.responses['final_answer'] = st.session_state.final_answer
                st.session_state.responses['message'] = message or "No message, just pure excitement!"
                
                # Format the final message for notifications
                notification_text = get_notification_message(st.session_state.responses)
                
                # Send notifications
                email_sent = send_email_notification("💕 You Have a Date! 💕", notification_text)
                webhook_sent = send_webhook_notification(notification_text)

                time.sleep(2) # To simulate sending time

            st.session_state.notification_sent = True
            st.rerun()

# 9. FINAL CONFIRMATION MESSAGE
if st.session_state.notification_sent:
    show_progress(7, 7)
    update_love_level(0)
    st.markdown(f"""
    <div class="romantic-text">
        <h2 style="text-align:center; font-family: 'Dancing Script', cursive; font-size: 3rem; color: #d63384;">
            It's a Date! ❤️
        </h2>
        <p style="font-size: 1.3rem; text-align: center; color: #2c3e50; font-family: 'Poppins', sans-serif;">
            Your response has been sent! I'm already counting down the seconds until I see you.
            Thank you for making my day, my week, and my year!
        </p>
        <p style="font-size: 1.3rem; text-align: center; font-weight: 600; color: #d63384;">
            Get ready for the best date ever!
        </p>
        <hr>
        <h4 style="text-align:center; font-family: 'Poppins', sans-serif;">Your final choices:</h4>
        <ul>
            <li><b>Time:</b> {st.session_state.responses.get('time')}</li>
            <li><b>Dinner:</b> {st.session_state.responses.get('dining')}</li>
            <li><b>Ice Cream:</b> {st.session_state.responses.get('ice_cream')}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.success("I'll text you to confirm everything. I can't wait! 😊")


# --- FOOTER ---
st.markdown("""
<div class="footer-hearts">
    Made with Love, for the One I Love
</div>
""", unsafe_allow_html=True)