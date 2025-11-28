import streamlit as st
import json
from convert import intent_to_policy, detect_conflicts

st.set_page_config(page_title="Intent2Policy", layout="wide")
st.title("Intent2Policy — Convert Intents to Policy")
uploaded = st.file_uploader("Upload intent JSON file", type=["json"])
text_input = st.text_area("Or paste intent JSON here")

raw_json = None
if uploaded:
    try:
        raw_json = json.load(uploaded)
    except Exception as e:
        st.error("Invalid JSON file.")
elif text_input.strip():
    try:
        raw_json = json.loads(text_input)
    except Exception as e:
        st.error("Invalid JSON pasted.")

if raw_json:
    if isinstance(raw_json, dict):
        intents = [raw_json]
    else:
        intents = raw_json
    st.subheader("Generated Policies")
    policies = []
    for i in intents:
        p = intent_to_policy(i)
        policies.append({"intent": i, "policy_text": p})
        st.code(p)
    conflicts = detect_conflicts(intents)
    if conflicts:
        st.warning(f"Conflicts found: {conflicts}")
    else:
        st.success("No basic conflicts detected.")
