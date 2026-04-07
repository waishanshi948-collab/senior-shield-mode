import streamlit as st
import random
import time
from datetime import datetime, timedelta

# Page setup
st.set_page_config(page_title="Senior Shield Mode", page_icon="🛡️", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .success-box {
        background-color: #D1FAE5;
        border-left: 5px solid #10B981;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .error-box {
        background-color: #FEE2E2;
        border-left: 5px solid #EF4444;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .warning-box {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .step-completed {
        background-color: #10B981;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        display: inline-block;
        font-size: 12px;
    }
    .step-active {
        background-color: #3B82F6;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        display: inline-block;
        font-size: 12px;
    }
    .step-pending {
        background-color: #9CA3AF;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        display: inline-block;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'pending' not in st.session_state:
    st.session_state.pending = False
if 'pending_time' not in st.session_state:
    st.session_state.pending_time = None
if 'amount' not in st.session_state:
    st.session_state.amount = 0
if 'recipient' not in st.session_state:
    st.session_state.recipient = ""
if 'show_step1_form' not in st.session_state:
    st.session_state.show_step1_form = True
if 'show_step1_result' not in st.session_state:
    st.session_state.show_step1_result = False
if 'step1_result' not in st.session_state:
    st.session_state.step1_result = None
if 'show_step2_form' not in st.session_state:
    st.session_state.show_step2_form = False
if 'show_step2_result' not in st.session_state:
    st.session_state.show_step2_result = False
if 'step2_result' not in st.session_state:
    st.session_state.step2_result = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Title
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://img.icons8.com/color/96/000000/elderly.png", width=80)
    st.title("🛡️ Senior Shield Mode")
    st.caption("Three-Layer Protection for Elderly Banking")

st.markdown("---")

# Progress indicators
st.markdown("### 📊 Transaction Security Progress")

col1, col2, col3 = st.columns(3)

with col1:
    if st.session_state.step > 1:
        st.markdown('<div style="text-align:center">🔐<br><span class="step-completed">Step 1: Completed ✓</span></div>', unsafe_allow_html=True)
    elif st.session_state.step == 1:
        st.markdown('<div style="text-align:center">🔐<br><span class="step-active">Step 1: In Progress</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center">🔐<br><span class="step-pending">Step 1: Pending</span></div>', unsafe_allow_html=True)

with col2:
    if st.session_state.step > 2:
        st.markdown('<div style="text-align:center">👨‍👩‍👧<br><span class="step-completed">Step 2: Completed ✓</span></div>', unsafe_allow_html=True)
    elif st.session_state.step == 2:
        st.markdown('<div style="text-align:center">👨‍👩‍👧<br><span class="step-active">Step 2: In Progress</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center">👨‍👩‍👧<br><span class="step-pending">Step 2: Pending</span></div>', unsafe_allow_html=True)

with col3:
    if st.session_state.step > 3:
        st.markdown('<div style="text-align:center">⏰<br><span class="step-completed">Step 3: Completed ✓</span></div>', unsafe_allow_html=True)
    elif st.session_state.step == 3:
        st.markdown('<div style="text-align:center">⏰<br><span class="step-active">Step 3: In Progress</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center">⏰<br><span class="step-pending">Step 3: Pending</span></div>', unsafe_allow_html=True)

st.markdown("---")

# ========== STEP 1: Knowledge Check ==========
if st.session_state.step == 1:
    
    # Show form
    if st.session_state.show_step1_form:
        st.subheader("🔐 Step 1: Security Verification")
        st.caption("Personalized security question - Only you know the answer")
        
        with st.form("transaction_form"):
            col1, col2 = st.columns(2)
            with col1:
                recipient = st.text_input("👤 Recipient Name", placeholder="Enter recipient's full name")
            with col2:
                amount = st.number_input("💰 Amount (HKD)", min_value=100, max_value=500000, value=10000, step=1000)
            
            submitted = st.form_submit_button("📝 Review Transaction", type="primary", use_container_width=True)
        
        if submitted:
            if not recipient:
                st.error("❌ Please enter recipient name")
            else:
                st.session_state.recipient = recipient
                st.session_state.amount = amount
                st.session_state.show_step1_form = False
                st.session_state.show_step1_result = True
                st.session_state.attempts = 0
                st.rerun()
    
    # Show security question
    elif st.session_state.show_step1_result:
        st.subheader("🔐 Step 1: Security Verification")
        
        # Show transaction summary
        st.info(f"📋 Transaction Summary: Transfer HKD {st.session_state.amount:,} to {st.session_state.recipient}")
        
        st.markdown("### ❓ Security Verification Question")
        
        # Questions with EXACT correct answers (case-insensitive)
        questions = {
            "What is your wedding anniversary? (e.g., May 10)": {
                "correct": "may 10",
                "aliases": ["may 10", "may 10th", "10 may", "may tenth"]
            },
            "What is your eldest child's birth month?": {
                "correct": "may",
                "aliases": ["may", "may."]
            },
            "What year did you open your first bank account?": {
                "correct": "1995",
                "aliases": ["1995", "1995."]
            },
            "What is your mother's maiden name?": {
                "correct": "smith",
                "aliases": ["smith", "smith."]
            },
            "What was your first pet's name?": {
                "correct": "lucky",
                "aliases": ["lucky", "lucky."]
            },
            "What is your favorite color?": {
                "correct": "blue",
                "aliases": ["blue", "blue."]
            },
            "What street did you grow up on?": {
                "correct": "main street",
                "aliases": ["main street", "main st", "main"]
            },
            "What was your first school name?": {
                "correct": "central elementary",
                "aliases": ["central elementary", "central", "central elementary school"]
            }
        }
        
        # Randomly select a question
        if 'current_question' not in st.session_state:
            question_text = random.choice(list(questions.keys()))
            st.session_state.current_question = question_text
            st.session_state.correct_answer = questions[question_text]["correct"]
            st.session_state.answer_aliases = questions[question_text]["aliases"]
        
        st.markdown(f"**📌 {st.session_state.current_question}**")
        answer = st.text_input("Your answer:", key="security_answer", placeholder="Type your answer here...")
        
        # Show remaining attempts
        attempts_left = 3 - st.session_state.attempts
        st.caption(f"⚠️ Attempts remaining: {attempts_left}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Verify Identity", type="primary"):
                if answer:
                    user_answer = answer.lower().strip()
                    
                    # Check if answer matches correct answer or any alias
                    is_correct = (user_answer == st.session_state.correct_answer or 
                                  user_answer in st.session_state.answer_aliases)
                    
                    if is_correct:
                        st.session_state.step1_result = "passed"
                        st.session_state.show_step1_result = False
                        st.rerun()
                    else:
                        st.session_state.attempts += 1
                        if st.session_state.attempts >= 3:
                            st.session_state.step1_result = "failed_max"
                            st.session_state.show_step1_result = False
                            st.rerun()
                        else:
                            st.error(f"❌ Incorrect answer! You have {3 - st.session_state.attempts} attempts remaining.")
                            st.rerun()
                else:
                    st.warning("⚠️ Please enter an answer")
        
        with col2:
            if st.button("❌ Cancel Transaction"):
                st.session_state.step1_result = "cancelled"
                st.session_state.show_step1_result = False
                st.rerun()
    
    # Show result and redirect
    elif st.session_state.step1_result == "passed":
        st.markdown("""
        <div class="success-box">
            <h3>✅ Verification Passed!</h3>
            <p>Identity confirmed successfully. Moving to Step 2...</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.step = 2
        st.session_state.show_step2_form = True
        st.session_state.step1_result = None
        # Clear stored question
        if 'current_question' in st.session_state:
            del st.session_state.current_question
        time.sleep(1)
        st.rerun()
        
    elif st.session_state.step1_result == "failed_max":
        st.markdown("""
        <div class="error-box">
            <h3>❌ Verification Failed - Too Many Attempts!</h3>
            <p>You have exceeded the maximum number of attempts (3).</p>
            <p>⚠️ Your transaction has been cancelled for security reasons.</p>
            <p>Please contact your bank if you believe this is an error.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 Start Over", type="primary"):
            # Reset all states
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
    elif st.session_state.step1_result == "cancelled":
        st.markdown("""
        <div class="warning-box">
            <h3>⏸️ Transaction Cancelled</h3>
            <p>You have cancelled this transaction.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 New Transaction", type="primary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# ========== STEP 2: CareCircle Alert ==========
elif st.session_state.step == 2:
    
    if st.session_state.show_step2_form:
        st.subheader("👨‍👩‍👧 Step 2: CareCircle Alert")
        st.caption("Family verification for large transfers")
        
        if st.session_state.amount > 10000:
            st.markdown(f"""
            <div class="warning-box">
                <h3>⚠️ Large Transfer Detected</h3>
                <p>Amount: <strong>HKD {st.session_state.amount:,}</strong> exceeds preset limit <strong>HKD 10,000</strong></p>
                <p>CareCircle protection activated automatically.</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.spinner("📱 Sending SMS alerts to family members..."):
                time.sleep(1)
            
            st.markdown("**✅ Alerts sent to:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.success("👨 David Chen (Son)\n+852 9123 4567")
            with col2:
                st.success("👩 Lisa Chen (Daughter)\n+852 9234 5678")
            with col3:
                st.success("👵 Mary Chen (Spouse)\n+852 9345 6789")
            
            st.markdown("---")
            st.markdown("### 👪 Family Confirmation Required")
            
            approval = st.radio(
                "Family member response:",
                ["✅ Approved - Family confirmed", "❌ Rejected - Family denied"],
                index=None,
                horizontal=True
            )
            
            if st.button("✅ Submit Family Confirmation", type="primary", use_container_width=True):
                if approval == "✅ Approved - Family confirmed":
                    st.session_state.step2_result = "approved"
                    st.session_state.show_step2_form = False
                    st.rerun()
                elif approval == "❌ Rejected - Family denied":
                    st.session_state.step2_result = "rejected"
                    st.session_state.show_step2_form = False
                    st.rerun()
                else:
                    st.warning("⚠️ Please select an option")
        else:
            st.markdown(f"""
            <div class="success-box">
                <h3>✅ Amount Below Limit</h3>
                <p>Transfer amount <strong>HKD {st.session_state.amount:,}</strong> is below the HKD 10,000 limit.</p>
                <p>CareCircle alert is not required for this transaction.</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("➡️ Continue to Cooling Period", type="primary", use_container_width=True):
                st.session_state.step2_result = "skipped"
                st.session_state.show_step2_form = False
                st.rerun()
    
    elif st.session_state.step2_result == "approved":
        st.markdown("""
        <div class="success-box">
            <h3>✅ Family Approved!</h3>
            <p>Transaction has been approved by family members. Moving to cooling period...</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.step = 3
        st.session_state.step2_result = None
        time.sleep(1)
        st.rerun()
        
    elif st.session_state.step2_result == "rejected":
        st.markdown("""
        <div class="error-box">
            <h3>❌ Transaction Rejected by Family</h3>
            <p>Family members have rejected this transaction.</p>
            <p>Please contact your family before initiating another transfer.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 Start Over", type="primary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
    elif st.session_state.step2_result == "skipped":
        st.markdown("""
        <div class="success-box">
            <h3>✅ Proceeding to Cooling Period</h3>
            <p>Moving to Step 3...</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.step = 3
        st.session_state.step2_result = None
        time.sleep(1)
        st.rerun()

# ========== STEP 3: Cooling Period ==========
elif st.session_state.step == 3:
    st.subheader("⏰ Step 3: Cooling Off Period")
    st.caption("2-hour waiting period for new payee verification")
    
    if not st.session_state.pending:
        st.markdown("""
        <div class="warning-box">
            <h3>⏰ Cooling Period Started</h3>
            <p>A 2-hour cooling period has been initiated for this transaction.</p>
            <p>This allows time to verify the transaction and prevent fraud.</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.pending_time = datetime.now() + timedelta(hours=2)
        st.session_state.pending = True
    
    # Show transaction details
    st.markdown("### 📋 Transaction Details")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Recipient", st.session_state.recipient)
        st.metric("Amount", f"HKD {st.session_state.amount:,}")
    with col2:
        st.metric("Initiated", datetime.now().strftime("%H:%M:%S"))
        st.metric("Will Complete", st.session_state.pending_time.strftime("%H:%M:%S"))
    
    st.markdown("---")
    
    # Show timer
    remaining = st.session_state.pending_time - datetime.now()
    if remaining.total_seconds() > 0:
        hours = int(remaining.total_seconds() // 3600)
        minutes = int((remaining.total_seconds() % 3600) // 60)
        seconds = int(remaining.total_seconds() % 60)
        
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; background: #1E3A8A; border-radius: 15px; margin: 20px 0;">
            <h2 style="color: white;">⏰ Time Remaining</h2>
            <h1 style="color: white; font-size: 48px;">{hours:02d}:{minutes:02d}:{seconds:02d}</h1>
            <p style="color: white;">Cooling period in progress</p>
        </div>
        """, unsafe_allow_html=True)
        
        total = 2 * 60 * 60
        elapsed = total - remaining.total_seconds()
        progress = elapsed / total
        st.progress(progress)
        
        st.caption(f"⏳ {int(progress * 100)}% complete")
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("❌ Cancel Transaction", type="secondary", use_container_width=True):
                st.markdown("""
                <div class="success-box">
                    <h3>✅ Transaction Cancelled</h3>
                    <p>Your transaction has been successfully cancelled.</p>
                </div>
                """, unsafe_allow_html=True)
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                time.sleep(1)
                st.rerun()
        
        # Auto refresh every second
        time.sleep(1)
        st.rerun()
        
    else:
        st.markdown("""
        <div class="success-box">
            <h1>✅ Transaction Completed Successfully! 🎉</h1>
            <p>The cooling period has ended. Your transaction has been processed.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Recipient", st.session_state.recipient)
            st.metric("Amount", f"HKD {st.session_state.amount:,}")
        with col2:
            st.metric("Completion Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            st.metric("Security Checks", "3/3 ✓")
        
        st.balloons()
        
        if st.button("🔄 Start New Transaction", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 12px;">
    <p>🛡️ Senior Shield Mode | Emergency Hotline: 18222 (ADCC)</p>
    <p>© 2024 Senior Shield Technologies</p>
</div>
""", unsafe_allow_html=True)
