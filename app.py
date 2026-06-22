import streamlit as st
from groq import Groq

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

st.set_page_config(page_title="Interview Preparation Assistant")

st.title("🎯 Interview Preparation Assistant")

role = st.selectbox(
"Select Job Role",
[
"Software Engineer",
"Data Analyst",
"Frontend Developer",
"AI/ML Engineer"
]
)

difficulty = st.selectbox(
"Select Difficulty",
[
"Beginner",
"Intermediate",
"Advanced"
]
)

question_count = st.slider(
"Number of Questions",
min_value=1,
max_value=20,
value=3
)

    
if st.button("Generate Questions"):

    prompt_questions = f"""
    Generate {question_count} {difficulty} level interview questions for a {role} position.

    Requirements:
    - Only generate questions
    - Number them properly
    - Do not provide answers
    - Questions should be placement-oriented
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt_questions
            }
        ]
    )

    st.subheader("📋 Generated Interview Questions")
    questions_text = response.choices[0].message.content

if "questions_text" in locals():
    st.write(questions_text)

st.subheader("✍️ Write Your Answers")

for i in range(question_count):

    answer = st.text_area(
        f"Answer for Question {i+1}",
        height=150,
        key=f"answer_{i}"
    )
    
    
    
if st.button("Evaluate Answers"):

       st.success("AI Evaluation Started")

       for i in range(question_count):    

           user_answer = st.session_state[f"answer_{i}"]

           evaluation_prompt = f"""
           Evaluate this interview answer.

           Give:
           1. Score out of 10
           2. Strengths
           3. Weaknesses
           4. Better Answer

           Candidate Answer:
           {user_answer}
           """

           evaluation = client.chat.completions.create(
               model="llama-3.3-70b-versatile",
               messages=[
                   {
                       "role": "user",
                       "content": evaluation_prompt
                    }
                ]
           )

           st.write(f"### Feedback for Answer {i+1}")
           st.info(evaluation.choices[0].message.content)
           
   
  



   


   

tips = [
    "Revise core concepts regularly.",
    "Practice coding problems daily.",
    "Explain answers with real examples.",
    "Focus on problem-solving approach.",
    "Communicate confidently during interviews."
]

for tip in tips:
    st.write("✅", tip)

st.subheader("📊 Practice Progress")

st.progress(question_count / 10)

st.write(f"You practiced {question_count} questions today.")

st.subheader("🏆 Practice Level")

if difficulty == "Beginner":
    st.success("Foundation Building Level")

elif difficulty == "Intermediate":
    st.success("Placement Preparation Level")

else:
    st.success("Advanced Interview Level")








