import streamlit as st
import random

# Make the app look clean and scale nicely on an iPhone screen
st.set_page_config(page_title="Project Glow-Up Sandbox", layout="centered")

st.title("✨ The Project: Content Sandbox")
st.write("Test your hooks, track your visual style, and simulate the algorithm.")

# 1. Video Meta Logging Section
st.subheader("1. Log Your Private Vlog File")
video_title = st.text_input("Video Working Title (e.g., 'DITL Gym & House Progress')")
video_hook = st.text_area("What is the first 3-second hook?")
caption = st.text_area("Caption & Target Hashtags")

# 2. Strategic Quality Scoring (Self-Assessment)
st.subheader("2. Visual & Engagement Grading")
visual_aesthetic = st.slider("Visual Curation / Lighting (1-10)", 1, 10, 5)
pacing_score = st.slider("Pacing & Editing Cleanliness (1-10)", 1, 10, 5)

# 3. The Simulated Algorithm Engine
if st.button("🚀 Run Algorithm Simulation"):
    st.divider()
    st.subheader("📊 Private Performance Projection")
    
    # Calculate a baseline score out of 100 based on your curation inputs
    base_score = (visual_aesthetic * 5) + (pacing_score * 5)
    
    # Simulate realistic lifestyle niche metrics using standard industry benchmarks
    simulated_views = int((base_score * random.randint(15, 30)) + random.randint(200, 500))
    like_rate = round((simulated_views * random.uniform(0.08, 0.12))) # ~10% standard engagement
    save_rate = round((like_rate * random.uniform(0.05, 0.15)))
    
    # Display the simulated metrics in clean dashboard blocks
    col1, col2, col3 = st.columns(3)
    col1.metric("Projected Views", f"{simulated_views:,}")
    col2.metric("Simulated Likes", f"{like_rate:,}")
    col3.metric("Simulated Saves", f"{save_rate:,}")
    
    # Give automated tactical feedback based on your inputs
    if base_score > 75:
        st.success("🔥 High Aesthetic Rating: The algorithm predicts strong retention. This visual style matches the 'Ours' agency target aesthetic perfectly.")
    else:
        st.warning("💡 Strategy Note: Consider tightening the pacing or optimizing the lighting in the first 3 seconds to boost the projected watch time.")
