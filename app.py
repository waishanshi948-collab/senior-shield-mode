import streamlit as st
import random
import time
from datetime import datetime, timedelta

# Page setup
st.set_page_config(page_title="Senior Shield Mode", page_icon="🛡️", layout="wide")

# Custom CSS for better styling
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
if 'knowledge_passed' not in st.session_state:
    st.session_state.knowledge_passed = False
if 'knowledge_failed' not in st.session_state:
    st.session_state.knowledge_failed = False
if 'family_approved' not in st.session_state:
    st.session_state.family_approved = False
if 'family_rejected' not in st.session_state:
    st.session_state.family_rejected = False
if 'auto_redirect' not in st.session_state:
    st.session_state.auto_redirect = False

# Title with logo
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
    st.subheader("🔐 Step 1: Security Verification")
    st.caption("Personalized security question - Only you know the answer")
    
    # Transaction form
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
            
            # Show transaction summary
            st.info(f"📋 Transaction Summary: Transfer HKD {amount:,} to {recipient}")
            
            # Security question
            st.markdown("---")
            st.markdown("### ❓ Security Verification Question")
            
            # Questions database
            questions = {
                "What is your wedding anniversary? (e.g., May 10)": "May 10",
                "What is your eldest child's birth month?": "May",
                "What year did you open your first bank account?": "1995",
                "What is your mother's maiden name?": "Smith",
                "What was your first pet's name?": "Lucky"
            }
            
            question = random.choice(list(questions.keys()))
            correct_answer = questions[question]
            
            st.markdown(f"**📌 {question}**")
            answer = st.text_input("Your answer:", key="security_answer")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Verify Identity", type="primary"):
                    if answer and answer.lower().strip() == correct_answer.lower():
                        # Show success message
                        st.markdown("""
                        <div class="success-box">
                            <h3>✅ Verification Passed!</h3>
                            <p>Identity confirmed successfully. Redirecting to Step 2...</p>
                        </div>
                        """, unsafe_allow_html=True)
                        st.session_state.knowledge_passed = True
                        st.session_state.step = 2
                        time.sleep(1.5)
                        st.rerun()
                    else:
                        # Show failure message
                        st.markdown("""
                        <div class="error-box">
                            <h3>❌ Verification Failed!</h3>
                            <p>Incorrect answer. Transaction has been cancelled for your security.</p>
                            <p>⚠️ Please contact your bank if you believe this is an error.</p>
                        </div>
                        """, unsafe_allow_html=True)
                        st.session_state.knowledge_failed = True
                        time.sleep(3)
                        # Reset form
                        st.session_state.step = 1
                        st.rerun()
            with col2:
                if st.button("❌ Cancel Transaction"):
                    st.markdown("""
                    <div class="warning-box">
                        <h3>⏸️ Transaction Cancelled</h3>
                        <p>You have cancelled this transaction.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    time.sleep(1.5)
                    st.rerun()

# ========== STEP 2: CareCircle Alert ==========
elif st.session_state.step == 2:
    st.subheader("👨‍👩‍👧 Step 2: CareCircle Alert")
    st.caption("Family verification for large transfers")
    
    # Check if amount exceeds limit
    if st.session_state.amount > 10000:
        st.markdown(f"""
        <div class="warning-box">
            <h3>⚠️ Large Transfer Detected</h3>
            <p>Amount: <strong>HKD {st.session_state.amount:,}</strong> exceeds preset limit <strong>HKD 10,000</strong></p>
            <p>CareCircle protection activated automatically.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("📱 Sending SMS alerts to family members...")
        
        # Show sent alerts with animation
        with st.spinner("Sending alerts..."):
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
        
        # Family approval options
        approval = st.radio(
            "Family member response:",
            ["⏳ Waiting for response...", "✅ Approved - Family confirmed", "❌ Rejected - Family denied"],
            index=0,
            horizontal=True
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📞 Call Family Member", use_container_width=True):
                st.info("📱 Dialing: +852 9123 4567 (David Chen)")
        with col2:
            if st.button("💬 Resend Alert", use_container_width=True):
                st.success("✅ Alert resent to all family members")
        
        st.markdown("---")
        
        # Submit confirmation
        if st.button("✅ Submit Family Confirmation", type="primary", use_container_width=True):
            if "Approved" in approval:
                st.markdown("""
                <div class="success-box">
                    <h3>✅ Family Approved!</h3>
                    <p>Transaction has been approved by family members. Redirecting to cooling period...</p>
                </div>
                """, unsafe_allow_html=True)
                st.session_state.family_approved = True
                st.session_state.step = 3
                time.sleep(1.5)
                st.rerun()
            elif "Rejected" in approval:
                st.markdown("""
                <div class="error-box">
                    <h3>❌ Transaction Rejected by Family</h3>
                    <p>Family members have rejected this transaction. The transfer has been cancelled.</p>
                    <p>Please contact your family before initiating another transfer.</p>
                </div>
                """, unsafe_allow_html=True)
                st.session_state.family_rejected = True
                time.sleep(3)
                # Reset to step 1
                for key in ['step', 'knowledge_passed', 'knowledge_failed', 'family_approved', 'family_rejected']:
                    if key in st.session_state:
                        if key == 'step':
                            st.session_state.step = 1
                        else:
                            st.session_state[key] = False
                st.rerun()
            else:
                st.warning("⚠️ Please wait for family response or contact them directly.")
    else:
        # Amount below limit - skip CareCircle
        st.markdown(f"""
        <div class="success-box">
            <h3>✅ Amount Below Limit</h3>
            <p>Transfer amount <strong>HKD {st.session_state.amount:,}</strong> is below the HKD 10,000 limit.</p>
            <p>CareCircle alert is not required for this transaction.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("➡️ Continue to Cooling Period", type="primary", use_container_width=True):
            st.session_state.family_approved = True
            st.session_state.step = 3
            time.sleep(0.5)
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
        
        # Display timer prominently
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; background: #1E3A8A; border-radius: 15px; margin: 20px 0;">
            <h2 style="color: white;">⏰ Time Remaining</h2>
            <h1 style="color: white; font-size: 48px;">{hours:02d}:{minutes:02d}:{seconds:02d}</h1>
            <p style="color: white;">Cooling period in progress</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bar
        total = 2 * 60 * 60
        elapsed = total - remaining.total_seconds()
        progress = elapsed / total
        st.progress(progress)
        
        st.caption(f"⏳ {int(progress * 100)}% complete")
        
        st.markdown("---")
        
        # Cancel button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("❌ Cancel Transaction", type="secondary", use_container_width=True):
                st.markdown("""
                <div class="success-box">
                    <h3>✅ Transaction Cancelled</h3>
                    <p>Your transaction has been successfully cancelled.</p>
                    <p>No funds have been transferred.</p>
                </div>
                """, unsafe_allow_html=True)
                # Reset all states
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                time.sleep(2)
                st.rerun()
        
        # Auto-refresh timer (every 1 second)
        time.sleep(1)
        st.rerun()
        
    else:
        # Cooling period complete
        st.markdown("""
        <div class="success-box">
            <h1>✅ Transaction Completed Successfully! 🎉</h1>
            <p>The cooling period has ended. Your transaction has been processed.</p>
            <hr>
            <h3>📊 Transaction Summary</h3>
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
    <p>🛡️ Senior Shield Mode | Three-Layer Protection: Knowledge Check → CareCircle Alert → Cooling Period</p>
    <p>Emergency Hotline: 18222 (ADCC) | Bank Support: 2233 3000</p>
    <p>© 2024 Senior Shield Technologies | All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
