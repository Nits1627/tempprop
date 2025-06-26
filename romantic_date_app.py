import streamlit as st
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time

# --- Page Configuration ---
# Sets the title, icon, and layout for the web app page.
st.set_page_config(
    page_title="A Very Special Invitation 💕",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Email Notification Function ---
# This function sends an email with the date responses.
# It securely accesses credentials stored in Streamlit's secrets management.
def send_response_email(responses):
    """Sends a summary of the responses to a predefined email address."""
    try:
        # --- Load Credentials from secrets.toml ---
        # It's crucial that the .streamlit/secrets.toml file exists and is correctly formatted.
        sender_email = st.secrets["email_credentials"]["sender_email"]
        sender_password = st.secrets["email_credentials"]["sender_password"]
        receiver_email = st.secrets["email_credentials"]["receiver_email"]

        # --- Email Content ---
        subject = f"💖 A Response to Your Movie Date Invitation! 💖"
        
        # The email body is created using HTML for better formatting and a romantic feel.
        body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #fef6f8; color: #333; }}
                .container {{ padding: 25px; margin: 20px; border: 2px solid #ff69b4; border-radius: 15px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
                h2 {{ color: #d63384; font-family: 'Georgia', serif; }}
                p {{ font-size: 16px; line-height: 1.6; }}
                ul {{ list-style-type: '💕'; padding-left: 20px; }}
                li {{ margin-bottom: 10px; }}
                strong {{ color: #ff1493; }}
                .footer {{ margin-top: 20px; font-size: 12px; color: #888; text-align: center;}}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>My Dearest,</h2>
                <p>You have received a response to your beautiful invitation. Here are the lovely details:</p>
                <ul>
                    <li><strong>Movie Time:</strong> {responses.get('time', 'Not yet chosen')}</li>
                    <li><strong>Dining Choice:</strong> {responses.get('dining', 'Not yet chosen')}</li>
                    <li><strong>Final Answer:</strong> {responses.get('final_answer', 'Awaiting response...')}</li>
                </ul>
        """
        if responses.get('message'):
            body += f"<p><strong>A special message was included:</strong></p><p style='font-style: italic; background-color: #fdf2f5; padding: 10px; border-radius: 8px;'>\"{responses['message']}\"</p>"
            
        body += """
                <p>How exciting! I hope you are looking forward to this special day! ✨</p>
                <div class="footer">
                    <p>With love,</p>
                    <p>Your Automated Romance Assistant 🤖💕</p>
                </div>
            </div>
        </body>
        </html>
        """

        # --- Setup Email Message ---
        msg = MIMEMultipart()
        msg['From'] = f"Your Romantic App <{sender_email}>"
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        # --- Send Email via SMTP (Gmail) ---
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection with TLS
            server.login(sender_email, sender_password)
            server.send_message(msg)
            
        return True # Indicate success
        
    except Exception as e:
        # This will show an error in the Streamlit app if secrets are missing or wrong
        st.error(f"Oh no! I couldn't send the email. Please check the secrets.toml file. Error: {e}")
        return False # Indicate failure

# --- Enhanced CSS Styling ---
# This block contains all the CSS for the app's romantic styling and animations.
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@400;500&display=swap');

    .main, .stApp {
        background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%);
    }

    /* --- Animations for a dynamic feel --- */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.15); }
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 20, 147, 0.7); }
        70% { box-shadow: 0 0 0 20px rgba(255, 20, 147, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 20, 147, 0); }
    }

    .st-emotion-cache-1y4p8pa { /* Main content container */
        animation: fadeIn 1s ease-out;
    }

    /* --- Typography & Headers --- */
    .romantic-header {
        text-align: center;
        color: #c72c41;
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem;
        text-shadow: 1px 1px 3px rgba(255,255,255,0.7);
        margin-bottom: 1rem;
    }

    h3 {
        color: #d63384;
        font-family: 'Playfair Display', serif;
    }

    /* --- Decorative Elements --- */
    .heart-decoration {
        text-align: center;
        font-size: 2.5rem;
        margin: 1rem 0;
        animation: heartbeat 1.5s ease-in-out infinite both;
        color: #ff1493;
    }

    /* --- Content Cards --- */
    .romantic-text, .movie-info, .cinema-info, .response-summary {
        background: rgba(255, 255, 255, 0.92);
        padding: 2rem;
        border-radius: 25px;
        border: 2px solid #ff85c0;
        margin: 1.5rem 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        color: #333;
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        animation: fadeIn 0.8s ease-out forwards;
    }
    
    .romantic-text:hover, .movie-info:hover, .cinema-info:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(255, 105, 180, 0.25);
    }
    
    .cinema-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
    }
    
    /* --- Buttons Styling --- */
    .stButton > button {
        background: linear-gradient(45deg, #ff69b4, #ff1493);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 1rem 2.5rem;
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
        width: 100%;
        margin-bottom: 10px;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) translateY(-3px);
        box-shadow: 0 8px 20px rgba(255, 105, 180, 0.6);
        background: linear-gradient(45deg, #ff1493, #c72c41);
    }
    
    /* Style for the final YES button to make it extra special and inviting */
    .stButton[data-testid$="stButton-yes_button"] > button {
         animation: pulse 2s infinite;
    }

    /* --- Form Elements Styling --- */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid #ff69b4;
        border-radius: 15px;
        color: #333;
        font-family: 'Poppins', sans-serif;
    }

</style>
""", unsafe_allow_html=True)

# --- Initialize Session State ---
# This ensures that the user's responses are saved as they interact with the app.
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'email_sent' not in st.session_state:
    st.session_state.email_sent = False


# ==============================================================================
# --- APPLICATION LAYOUT ---
# The app is built using containers to logically group sections.
# Sections are revealed progressively as the user makes choices.
# ==============================================================================

# --- Header ---
st.markdown('<div class="heart-decoration">💖 💝 💖</div>', unsafe_allow_html=True)
st.markdown('<h1 class="romantic-header">A Movie Date Invitation</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center; margin-top:-1rem;">Just For You... My Love</h3>', unsafe_allow_html=True)

# --- Step 1: The Invitation ---
with st.container():
    st.markdown("""
    <div class="romantic-text">
        <h3 style="text-align: center;">My Dearest,</h3>
        <p style="font-size: 1.2rem; line-height: 1.6; text-align: center;">
            Every moment with you feels like the best I have, and I want to create another happy memory together. 
            Would you honor me by accompanying me to see <strong>"F1"</strong> this Saturday at <strong>PVR Chakala</strong>? 
            I can't stop thinking about spending this special time with just you. 🥰
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- Step 2: Cinema & Movie Info ---
with st.container():
    st.markdown("""
    <div class="cinema-info">
        <h3>🎬 Our Cinema Destination 🎬</h3>
        <h4>PVR Chakala, Mumbai</h4>
        <p style="font-size: 1.1rem;">
            A perfect place for our movie date! Modern screens, comfy seating, and the best cinematic experience for us! 🍿
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="movie-info">
        <h3 style="text-align: center;">🏎️ About The Movie: "F1" 🏎️</h3>
        <p style="text-align: center; font-size: 1.2rem;">
            Get ready for high-speed thrills, heart-pounding action, and the pure adrenaline rush of Formula 1!
            It's going to be an incredible experience to share. 🏁
        </p>
        <p style="text-align: center; margin-top: 1.5rem;"><strong>Let's watch the trailer and get excited!</strong></p>
    """, unsafe_allow_html=True)
    
    st.video("https://youtu.be/8yh9BPUBbbQ?si=4mvFI0PXCN9AQwIw")
    st.markdown('<div class="heart-decoration">💕</div>', unsafe_allow_html=True)


# --- Step 3: Interactive Time Selection ---
with st.container():
    st.markdown("### ⏰ When would you love to go?")
    st.markdown("###### *Choose the time that feels perfect for our date...* 🥰")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌅 Afternoon Show (1:00 PM)", key="afternoon", help="Perfect for a lovely day date!"):
            st.session_state.responses['time'] = "🌅 Afternoon Show (1:00 PM)"
            st.session_state.responses['meal_type'] = "lunch"
            st.balloons()
    
    with col2:
        if st.button("🌙 Evening Show (7:00 PM)", key="evening", help="For a romantic night out!"):
            st.session_state.responses['time'] = "🌙 Evening Show (7:00 PM)"
            st.session_state.responses['meal_type'] = "dinner"
            st.balloons()
    
    if st.session_state.responses.get('time'):
        st.success(f"✨ Perfect! {st.session_state.responses['time']} it is! ✨")

# --- Step 4: Enhanced Dining Choices (Appears after time is chosen) ---
if st.session_state.responses.get('time'):
    with st.container():
        st.markdown('<div class="heart-decoration">🍽️ 💕 🍽️</div>', unsafe_allow_html=True)
        meal_type = st.session_state.responses.get('meal_type', 'meal')
        st.markdown(f"### 🍽️ And where shall we have our {meal_type}?")
        st.markdown(f"###### *Let's make our {meal_type} as special as you are.* �")
        
        st.markdown("--- \n #### 🥂 For a Fancy Date")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🍽️ Food Exchange", key="food_exchange"):
                st.session_state.responses['dining'] = "🥂 Food Exchange (Upscale dining)"
        with col2:
            if st.button("🌶️ Chimmi Churri", key="chimmi_churri"):
                st.session_state.responses['dining'] = "🌶️ Chimmi Churri (Delicious flavors)"

        st.markdown("#### 🏠 For a Cozy Date")
        col3, col4 = st.columns(2)
        with col3:
            if st.button("🥔 Pop Tates", key="pop_tates"):
                st.session_state.responses['dining'] = "🥔 Pop Tates (Casual & fun)"
        with col4:
            if st.button("🍔 Good Flippin Burgers", key="good_flippin"):
                st.session_state.responses['dining'] = "🍔 Good Flippin Burgers (Tasty & chill)"
        
        if st.session_state.responses.get('dining'):
            st.success(f"Excellent choice! I can't wait to dine with you at {st.session_state.responses['dining'].split('(')[0].strip()}! 💕")


# --- Step 5: Special Song Section (Appears after dining is chosen) ---
if st.session_state.responses.get('dining'):
    with st.container():
        st.markdown('<div class="heart-decoration">🎵 💖 🎵</div>', unsafe_allow_html=True)
        st.markdown("### 🎵 A Song That Reminds Me Of You")
        
        st.markdown("""
        <div class="romantic-text">
            <p style="text-align: center; font-size: 1.1rem;">
                Before you answer, I want you to listen to this song. It captures just a fraction of how I feel about you... Every single day. 💕
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.video("https://youtu.be/DwuJeGYlYyw?si=1ageI_8GZAEL85qx")


# --- Step 6: Final Question & Response Trigger ---
if st.session_state.responses.get('dining'):
    with st.container():
        st.markdown('<div class="heart-decoration">💝 ✨ 💝</div>', unsafe_allow_html=True)
        st.markdown("### 💖 So, my beautiful love...")
        
        st.markdown("""
        <div class="romantic-text" style="border-color: #c72c41; border-width: 3px;">
            <h3 style="color: #c72c41; text-align: center; font-size: 1.8rem;">Will you be my date?</h3>
            <p style="text-align: center; font-size: 1.3rem; font-weight: bold;">
                Please say yes to making another beautiful memory together! 🥰
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💕 YES! A thousand times, YES! 💕", key="yes_button"):
                st.session_state.responses['final_answer'] = "YES! A thousand times, YES! 💕"
                st.balloons()
                st.snow()
        
        with col2:
            if st.button("🤔 Let me think for a moment...", key="maybe_button"):
                st.session_state.responses['final_answer'] = "Let me think about it... 🤔"
                st.info("Take all the time you need, my love. My heart will be waiting! 💕")

# --- Step 7: Response Summary & Email Sending Logic (Appears after final answer) ---
if 'final_answer' in st.session_state.responses:
    with st.container():
        st.markdown("---")
        summary_title = "🎉 Our Perfect Date Is Set! 🎉" if "YES" in st.session_state.responses['final_answer'] else "💖 My Hopeful Date Plan... 💖"
        st.markdown(f"<h3 style='text-align:center;'>{summary_title}</h3>", unsafe_allow_html=True)
        
        if "YES" in st.session_state.responses['final_answer']:
            st.markdown("""
            <div class="romantic-text" style="background: linear-gradient(135deg, #a8e063, #56ab2f); color: white; border-color: #fff;">
                <h2 style="text-align: center; color: white;">You said YES! My heart is doing flips!</h2>
                <p style="text-align: center; font-size: 1.3rem; color: white;">
                    I am supoer duperr excited for our date! This is going to be the most wonderful day. 💕✨
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Display the summary of choices
        st.markdown(f"""
        <div class="response-summary">
            <p><strong>🎬 Movie:</strong> F1 at PVR Chakala</p>
            <p><strong>⏰ Time:</strong> {st.session_state.responses.get('time', 'Not selected')}</p>
            <p><strong>🍽️ Dining:</strong> {st.session_state.responses.get('dining', 'Not selected')}</p>
            <p><strong>💖 Your Answer:</strong> {st.session_state.responses.get('final_answer', 'Not selected')}</p>
        </div>
        """, unsafe_allow_html=True)

        # Interactive message section for an optional note
        st.markdown("### 💌 Want to add a special message for dumb niteesh?")
        st.session_state.responses['message'] = st.text_area(
            "Tell me what you're thinking... I'm listening with all my heart. 🥰",
            placeholder="Share your thoughts, excitement, or anything you want to tell me...",
            key="additional_message"
        )
        
        # This conditional logic prevents the email button from being shown until the form is complete.
        # It also hides the button after the email has been sent successfully.
        if not st.session_state.email_sent:
            if st.button("💌 Send My Response To You!", key="send_email"):
                with st.spinner('Sending your lovely response with care... ✨'):
                    if send_response_email(st.session_state.responses):
                        st.success("Sent! I'll be looking out for it. I'm so excited!")
                        st.session_state.email_sent = True
        else:
            st.markdown("✅ *Your beautiful response has been sent to me! Thank you, my love.*")


# --- Footer ---
st.markdown("---")
st.markdown('<div class="footer-hearts" style="font-family: \'Poppins\', sans-serif; font-size: 1rem; color: #c72c41;">💕 Made with all my love, just for you 💕</div>', unsafe_allow_html=True)
st.markdown('<div class="heart-decoration">🌹 💖 🌹</div>', unsafe_allow_html=True)
