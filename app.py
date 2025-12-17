import streamlit as st

st.set_page_config(page_title="Student Grade Calculator", layout="centered")

st.title("📚 Student Grade Calculator")
st.markdown("---")

# Input for number of subjects
num_subjects = st.number_input(
    "Enter the number of subjects:",
    min_value=1,
    max_value=20,
    value=1,
    step=1
)

st.markdown("---")

# Input marks for each subject
marks = []
total_marks = 0

st.subheader(f"Enter marks for {num_subjects} subject(s):")

cols = st.columns(2)
for i in range(num_subjects):
    col = cols[i % 2]
    with col:
        mark = st.number_input(
            f"Subject {i+1} marks (out of 100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.5,
            key=f"subject_{i}"
        )
        marks.append(mark)
        total_marks += mark

st.markdown("---")

# Calculate percentage and grade
if st.button("Calculate Grade", type="primary"):
    percentage = (total_marks / (num_subjects * 100)) * 100
    
    # Determine grade
    if percentage >= 90:
        grade = "A+"
        emoji = "🌟"
    elif percentage >= 80:
        grade = "A"
        emoji = "⭐"
    elif percentage >= 70:
        grade = "B"
        emoji = "👍"
    elif percentage >= 60:
        grade = "C"
        emoji = "😊"
    elif percentage >= 50:
        grade = "D"
        emoji = "📝"
    else:
        grade = "F"
        emoji = "❌"
    
    # Display results
    st.markdown("---")
    st.subheader("📊 Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Marks", f"{total_marks:.1f}/{num_subjects * 100}")
    
    with col2:
        st.metric("Percentage", f"{percentage:.2f}%")
    
    with col3:
        st.metric("Grade", f"{grade} {emoji}")
    
    st.markdown("---")
    
    # Show marks breakdown
    st.subheader("Marks Breakdown:")
    for i, mark in enumerate(marks):
        st.write(f"**Subject {i+1}:** {mark:.1f}/100")
