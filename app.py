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
    .info-box {
        background-color: #EFF6FF;
        border-left: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .risk-low {
        background-color: #D1FAE5;
        border-left: 5px solid #10B981;
    }
    .risk-medium {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
    }
    .risk-high {
        background-color: #FEE2E2;
        border-left: 5px solid #EF4444;
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
    .sms-log {
        background-color: #1E3A8A;
        color: white;
        padding: 10px;
        border-radius: 8px;
        font-family: monospace;
        margin: 5px 0;
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
if 'risk_level' not in st.session_state:
    st.session_state.risk_level = None
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = 0
if 'sms_sent' not in st.session_state:
    st.session_state.sms_sent = False
if 'sms_logs' not in st.session_state:
    st.session_state.sms_logs = []
if 'transaction_count' not in st.session_state:
    st.session_state.transaction_count = 0

# Step 1 states
if 'show_step1_form' not in st.session_state:
    st.session_state.show_step1_form = True
if 'show_step1_result' not in st.session_state:
    st.session_state.show_step1_result = False
if 'step1_result' not in st.session_state:
    st.session_state.step1_result = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Step 2 states (Risk Engine)
if 'show_step2_form' not in st.session_state:
    st.session_state.show_step2_form = False
if 'show_step2_result' not in st.session_state:
    st.session_state.show_step2_result = False
if 'step2_result' not in st.session_state:
    st.session_state.step2_result = None

# Step 3 states (CareCircle)
if 'show_step3_form' not in st.session_state:
    st.session_state.show_step3_form = False
if 'show_step3_result' not in st.session_state:
    st.session_state.show_step3_result = False
if 'step3_result' not in st.session_state:
    st.session_state.step3_result = None

# Title
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://img.icons8.com/color/96/000000/elderly.png", width=80)
    st.title("🛡️ Senior Shield Mode")
    st.caption("4-Layer Protection for Elderly Banking")

st.markdown("---")

# Progress indicators (4 steps)
st.markdown("### 📊 Transaction Security Progress")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.session_state.step > 1:
        st.markdown('<div style="text-align:center">🔐<br><span class="step-completed">Step 1: Knowledge ✓</span></div>', unsafe_allow_html=True)
    elif st.session_state.step == 1:
        st.markdown('<div style="text-align:center">🔐<br><span class="step-active">Step 1: Knowledge</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center">🔐<br><span class="step-pending">Step 1</span></div>', unsafe_allow_html=True)

with col2:
    if st.session_state.step > 2:
        st.markdown('<div style="text-align:center">⚡<br><span class="step-completed">Step 2: Risk ✓</span></div>', unsafe_allow_html=True)
    elif st.session_state.step == 2:
        st.markdown('<div style="text-align:center">⚡<br><span class="step-active">Step 2: Risk Engine</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center">⚡<br><span class="step-pending">Step 2</span></div>', unsafe_allow_html=True)

with col3:
    if st.session_state.step > 3:
        st.markdown('<div style="text-align:center">👨‍👩‍👧<br><span class="step-completed">Step 3: CareCircle ✓</span></div>', unsafe_allow_html=True)
    elif st.session_state.step == 3:
        st.markdown('<div style="text-align:center">👨‍👩‍👧<br><span class="step-active">Step 3: CareCircle</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center">👨‍👩‍👧<br><span class="step-pending">Step 3</span></div>', unsafe_allow_html=True)

with col4:
    if st.session_state.step > 4:
        st.markdown('<div style="text-align:center">⏰<br><span class="step-completed">Step 4: Cooling ✓</span></div>', unsafe_allow_html=True)
    elif st.session_state.step == 4:
        st.markdown('<div style="text-align:center">⏰<br><span class="step-active">Step 4: Cooling</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center">⏰<br><span class="step-pending">Step 4</span></div>', unsafe_allow_html=True)

st.markdown("---")

# ==================== HELPER FUNCTIONS ====================

def send_sms(phone_number, message):
    """Simulate sending SMS"""
    sms_log = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "phone": phone_number,
        "message": message,
        "status": "Delivered"
    }
    st.session_state.sms_logs.append(sms_log)
    return True

def risk_engine_scan(amount, recipient, is_new_customer, is_international, is_card_not_present):
    """Risk engine scanning based on multiple factors"""
    
    risk_score = 0
    risk_factors = []
    
    # Check amount
    if amount > 10000:
        risk_score += 30
        risk_factors.append("Amount exceeds HKD 10,000")
    elif amount > 50000:
        risk_score += 50
        risk_factors.append("Amount exceeds HKD 50,000")
    
    # Check frequency (more than 5 times a day)
    st.session_state.transaction_count += 1
    if st.session_state.transaction_count > 5:
        risk_score += 40
        risk_factors.append(f"High frequency: {st.session_state.transaction_count} transactions today")
    
    # Check if first-time customer
    if is_new_customer:
        risk_score += 35
        risk_factors.append("First-time customer")
    
    # Check if international transfer
    if is_international:
        risk_score += 40
        risk_factors.append("International transfer")
    
    # Check if card-not-present
    if is_card_not_present:
        risk_score += 25
        risk_factors.append("Card-not-present transaction")
    
    # Determine risk level
    if risk_score >= 70:
        risk_level = "High"
        risk_color = "risk-high"
        action = "Funds temporarily locked. SMS alert sent to family."
    elif risk_score >= 40:
        risk_level = "Medium"
        risk_color = "risk-medium"
        action = "Additional verification required."
    else:
        risk_level = "Low"
        risk_color = "risk-low"
        action = "Transaction processing normally."
    
    return {
        "score": min(risk_score, 100),
        "level": risk_level,
        "color": risk_color,
        "action": action,
        "factors": risk_factors
    }

# ==================== STEP 1: Knowledge Check ====================
if st.session_state.step == 1:
    
    if st.session_state.show_step1_form:
        st.subheader("🔐 Step 1: Security Verification")
        st.caption("Personalized dynamic question - Only you know the answer")
        
        with st.form("transaction_form"):
            col1, col2 = st.columns(2)
            with col1:
                recipient = st.text_input("👤 Recipient Name", placeholder="Enter recipient's full name")
                is_new_customer = st.checkbox("🆕 First-time customer", help="Is this the first time you send money to this recipient?")
            with col2:
                amount = st.number_input("💰 Amount (HKD)", min_value=100, max_value=500000, value=10000, step=1000)
                is_international = st.checkbox("🌍 International transfer", help="Is this an international transfer?")
            
            is_card_not_present = st.checkbox("💳 Card-not-present transaction", help="Is this an online/card-not-present transaction?")
            
            submitted = st.form_submit_button("📝 Review Transaction", type="primary", use_container_width=True)
        
        if submitted:
            if not recipient:
                st.error("❌ Please enter recipient name")
            else:
                st.session_state.recipient = recipient
                st.session_state.amount = amount
                st.session_state.is_new_customer = is_new_customer
                st.session_state.is_international = is_international
                st.session_state.is_card_not_present = is_card_not_present
                st.session_state.show_step1_form = False
                st.session_state.show_step1_result = True
                st.session_state.attempts = 0
                st.rerun()
    
    elif st.session_state.show_step1_result:
        st.subheader("🔐 Step 1: Security Verification")
        
        st.info(f"📋 Transaction Summary: Transfer HKD {st.session_state.amount:,} to {st.session_state.recipient}")
        
        st.markdown("### ❓ Personalized Security Question")
        
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
            }
        }
        
        if 'current_question' not in st.session_state:
            question_text = random.choice(list(questions.keys()))
            st.session_state.current_question = question_text
            st.session_state.correct_answer = questions[question_text]["correct"]
            st.session_state.answer_aliases = questions[question_text]["aliases"]
        
        st.markdown(f"**📌 {st.session_state.current_question}**")
        answer = st.text_input("Your answer:", key="security_answer", placeholder="Type your answer here...")
        
        attempts_left = 3 - st.session_state.attempts
        st.caption(f"⚠️ Attempts remaining: {attempts_left}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Verify Identity", type="primary"):
                if answer:
                    user_answer = answer.lower().strip()
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
    
    elif st.session_state.step1_result == "passed":
        st.markdown("""
        <div class="success-box">
            <h3>✅ Verification Passed!</h3>
            <p>Identity confirmed successfully. Moving to Risk Engine Scan...</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.step = 2
        st.session_state.show_step2_form = True
        st.session_state.step1_result = None
        if 'current_question' in st.session_state:
            del st.session_state.current_question
        time.sleep(1)
        st.rerun()
        
    elif st.session_state.step1_result == "failed_max":
        st.markdown("""
        <div class="error-box">
            <h3>❌ Verification Failed - Too Many Attempts!</h3>
            <p>You have exceeded the maximum number of attempts (3).</p>
            <p>⚠️ Your transaction has been cancelled.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 Start Over"):
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
        if st.button("🔄 New Transaction"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# ==================== STEP 2: Risk Engine Scanning ====================
elif st.session_state.step == 2:
    
    if st.session_state.show_step2_form:
        st.subheader("⚡ Step 2: Risk Engine Scanning")
        st.caption("AI-powered risk assessment based on multiple factors")
        
        with st.spinner("🔍 Scanning transaction for risks..."):
            time.sleep(1.5)
        
        # Perform risk scan
        risk_result = risk_engine_scan(
            st.session_state.amount,
            st.session_state.recipient,
            st.session_state.is_new_customer,
            st.session_state.is_international,
            st.session_state.is_card_not_present
        )
        
        st.session_state.risk_score = risk_result["score"]
        st.session_state.risk_level = risk_result["level"]
        
        # Display risk assessment
        st.markdown(f"""
        <div class="{risk_result['color']}">
            <h3>📊 Risk Assessment Result</h3>
            <p><strong>Risk Score:</strong> {risk_result['score']}/100</p>
            <p><strong>Risk Level:</strong> {risk_result['level']}</p>
            <p><strong>Action:</strong> {risk_result['action']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if risk_result["factors"]:
            st.markdown("**⚠️ Risk Factors Detected:**")
            for factor in risk_result["factors"]:
                st.write(f"- {factor}")
        
        st.markdown("---")
        
        # Send SMS for high-risk transactions
        if risk_result["level"] == "High":
            st.warning("🚨 High-risk transaction detected! Sending SMS alerts to family members...")
            
            with st.spinner("📱 Sending SMS alerts..."):
                time.sleep(1)
            
            family_members = [
                {"name": "David Chen (Son)", "phone": "+852 9123 4567"},
                {"name": "Lisa Chen (Daughter)", "phone": "+852 9234 5678"},
                {"name": "Mary Chen (Spouse)", "phone": "+852 9345 6789"}
            ]
            
            for member in family_members:
                sms_message = f"[Senior Shield Alert] High-risk transaction detected! Amount: HKD {st.session_state.amount:,} to {st.session_state.recipient}. Risk score: {risk_result['score']}/100. Please verify immediately."
                send_sms(member["phone"], sms_message)
            
            st.markdown("**✅ SMS alerts sent to:**")
            for member in family_members:
                st.success(f"📲 {member['name']} - {member['phone']}")
            
            st.session_state.sms_sent = True
        
        st.markdown("---")
        
        if st.button("➡️ Continue to CareCircle", type="primary", use_container_width=True):
            st.session_state.step2_result = risk_result["level"]
            st.session_state.show_step2_form = False
            st.session_state.show_step3_form = True
            st.rerun()
    
    elif st.session_state.step2_result:
        st.markdown(f"""
        <div class="success-box">
            <h3>✅ Risk Scan Complete</h3>
            <p>Risk Level: {st.session_state.step2_result}</p>
            <p>Moving to CareCircle Verification...</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.step = 3
        st.session_state.step2_result = None
        time.sleep(1)
        st.rerun()

# ==================== STEP 3: CareCircle Alert ====================
elif st.session_state.step == 3:
    
    if st.session_state.show_step3_form:
        st.subheader("👨‍👩‍👧 Step 3: CareCircle Alert")
        st.caption("Social verification with family members")
        
        # Check if amount exceeds limit OR high risk
        if st.session_state.amount > 10000 or st.session_state.risk_level == "High":
            st.markdown(f"""
            <div class="warning-box">
                <h3>⚠️ Transaction Requires Family Verification</h3>
                <p>Amount: <strong>HKD {st.session_state.amount:,}</strong></p>
                <p>Risk Level: <strong>{st.session_state.risk_level}</strong></p>
                <p>CareCircle protection activated automatically.</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.spinner("📱 Sending CareCircle SMS alerts to family members..."):
                time.sleep(1)
            
            family_members = [
                {"name": "David Chen (Son)", "phone": "+852 9123 4567", "relation": "Son"},
                {"name": "Lisa Chen (Daughter)", "phone": "+852 9234 5678", "relation": "Daughter"},
                {"name": "Mary Chen (Spouse)", "phone": "+852 9345 6789", "relation": "Spouse"}
            ]
            
            for member in family_members:
                sms_message = f"[CareCircle Alert] Your family member is transferring HKD {st.session_state.amount:,} to {st.session_state.recipient}. Risk level: {st.session_state.risk_level}. Please reply YES to approve or NO to reject."
                send_sms(member["phone"], sms_message)
            
            st.markdown("**✅ CareCircle SMS alerts sent to:**")
            for member in family_members:
                st.success(f"📲 {member['name']} ({member['relation']}) - {member['phone']}")
            
            st.markdown("---")
            st.markdown("### 👪 Family Confirmation Required")
            
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
                if st.button("💬 Resend Alerts", use_container_width=True):
                    for member in family_members:
                        send_sms(member["phone"], sms_message)
                    st.success("✅ Alerts resent to all family members")
            
            if st.button("✅ Submit Family Confirmation", type="primary", use_container_width=True):
                if "Approved" in approval:
                    st.session_state.step3_result = "approved"
                    st.session_state.show_step3_form = False
                    st.rerun()
                elif "Rejected" in approval:
                    st.session_state.step3_result = "rejected"
                    st.session_state.show_step3_form = False
                    st.rerun()
                else:
                    st.warning("⚠️ Please wait for family response or contact them directly.")
        else:
            st.markdown(f"""
            <div class="success-box">
                <h3>✅ Amount Below Limit & Low Risk</h3>
                <p>Transfer amount <strong>HKD {st.session_state.amount:,}</strong> is below the HKD 10,000 limit.</p>
                <p>Risk level: <strong>{st.session_state.risk_level}</strong></p>
                <p>CareCircle alert is not required for this transaction.</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("➡️ Continue to Cooling Period", type="primary", use_container_width=True):
                st.session_state.step3_result = "skipped"
                st.session_state.show_step3_form = False
                st.rerun()
    
    elif st.session_state.step3_result == "approved":
        st.markdown("""
        <div class="success-box">
            <h3>✅ Family Approved!</h3>
            <p>Transaction has been approved by family members. Moving to cooling period...</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.step = 4
        st.session_state.step3_result = None
        time.sleep(1)
        st.rerun()
        
    elif st.session_state.step3_result == "rejected":
        st.markdown("""
        <div class="error-box">
            <h3>❌ Transaction Rejected by Family</h3>
            <p>Family members have rejected this transaction.</p>
            <p>Please contact your family before initiating another transfer.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 Start Over"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
    elif st.session_state.step3_result == "skipped":
        st.markdown("""
        <div class="success-box">
            <h3>✅ Proceeding to Cooling Period</h3>
            <p>Moving to Step 4...</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.step = 4
        st.session_state.step3_result = None
        time.sleep(1)
        st.rerun()

# ==================== STEP 4: Cooling Off Period ====================
elif st.session_state.step == 4:
    st.subheader("⏰ Step 4: Cooling Off Period")
    st.caption("2-hour waiting period for new payee verification")
    
    if not st.session_state.pending:
        st.markdown("""
        <div class="warning-box">
            <h3>⏰ 2-Hour Cooling Period Started</h3>
            <p>All transfers to new payees are placed in a 'Pending' status for 2 hours.</p>
            <p>This allows time to verify the transaction and prevent fraud.</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.pending_time = datetime.now() + timedelta(hours=2)
        st.session_state.pending = True
    
    st.markdown("### 📋 Transaction Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Recipient", st.session_state.recipient)
        st.metric("Amount", f"HKD {st.session_state.amount:,}")
        st.metric("Risk Level", st.session_state.risk_level)
    with col2:
        st.metric("Initiated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        st.metric("Will Complete", st.session_state.pending_time.strftime("%H:%M:%S"))
        st.metric("Status", "Pending")
    
    st.markdown("---")
    
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
            st.metric("Security Checks", "4/4 ✓")
        
        st.balloons()
        
        if st.button("🔄 Start New Transaction", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# ==================== SMS Log Display ====================
if st.session_state.sms_logs:
    with st.expander("📱 SMS Alert Log"):
        for log in st.session_state.sms_logs:
            st.markdown(f"""
            <div class="sms-log">
                [{log['timestamp']}] → {log['phone']}<br>
                📨 {log['message']}<br>
                ✅ Status: {log['status']}
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 12px;">
    <p>🛡️ Senior Shield Mode | 4-Layer Protection: Knowledge → Risk Engine → CareCircle → Cooling Period</p>
    <p>Emergency Hotline: 18222 (ADCC) | Bank Support: 2233 3000</p>
    <p>© 2024 Senior Shield Technologies</p>
</div>
""", unsafe_allow_html=True)
