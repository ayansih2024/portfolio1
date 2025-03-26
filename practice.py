import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Portfolio", layout="wide", initial_sidebar_state="collapsed")

# CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #0d1117;
        color: white;
        font-family: 'Arial', sans-serif;
    }

    .header {
        text-align: center;
        padding: 50px;
    }

    .header h1 {
        font-size: 3.5em;
        font-weight: bold;
        margin-bottom: 10px;
        color: #58a6ff;
    }

    .header p {
        font-size: 1.2em;
        color: #8b949e;
    }

    .section {
        padding: 40px;
    }

    .section h2 {
        font-size: 2em;
        margin-bottom: 20px;
        color: #58a6ff;
    }

    .project-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .project-card:hover {
        transform: scale(1.02);
        transition: transform 0.3s ease;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        background-color: #161b22;
        color: #8b949e;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown(
    """
    <div class="header">
        <h1>My Portfolio</h1>
        <p>Welcome to my portfolio! Explore my projects, skills, and achievements below.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# About Section
st.markdown(
    """
    <div class="section">
        <h2>About Me</h2>
        <p>
            Hi! I'm Ayan Gantayat, a passionate developer, 8th-grade student at Army Public School Kirkee, and tech enthusiast. I love building applications, exploring
            new technologies, and solving real-world problems through code. Let's work together to create something
            amazing!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Projects Section
st.markdown(
    """
    <div class="section">
        <h2>Projects</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# Project Cards
projects = [
    {
        "title": "Social Cosmos",
        "description": "A futuristic social networking platform to connect users globally.",
        "link": "https://socialcosmos-g8ps.onrender.com",
    },
    {
        "title": "Book Rental System",
        "description": "An online book rental platform that helps users borrow books conveniently.",
        "link": "https://example.com/book-rental",
    },
    {
        "title": "AI Chatbot",
        "description": "An intelligent chatbot built for the Smart India Hackathon.",
        "link": "https://example.com/ai-chatbot",
    },
    {
        "title": "Projekt-S.A.N.A",
        "description": "An intelligent chatbot built for daily use and a free model of chatGPT.",
        "link": "https://projekt-sana.streamlit.app/~/+/"
    },
]

for project in projects:
    st.markdown(
        f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p>{project['description']}</p>
            <a href="{project['link']}" target="_blank" style="color: #58a6ff; text-decoration: none;">View Project</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Skills Section
st.markdown(
    """
    <div class="section">
        <h2>Skills</h2>
        <ul>
            <li>Programming Languages: Python, JavaScript, HTML, CSS</li>
            <li>Frameworks: Streamlit, React, Flask</li>
            <li>Tools: Git, Docker, Figma</li>
            <li>Other: Machine Learning, AI, Web Development</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Achievements Section
st.markdown(
    """
    <div class="section">
        <h2>Achievements</h2>
        <ul>
            <li>AIT Quiz - 1st Place</li>
            <li>CBSE Regional Science Exhibition - 2nd Place</li>
            <li>IBM Skill Internship - Top 100</li>
            <li>VSSF SPOT - 4th Place</li>
            <li>IGKO - 1st Place</li>
            <li>IMO - 4th Place</li>
            <li>ICSO - 1st Place</li>
            <li>One Act Play - 1st Place</li>
            <li>Hindi Debate - 1st Place</li>
            <li>Poem Recitation - 2nd Place</li>
            <li>IUCAA Pune NSD Quiz - 5th Place</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Contact Section
st.markdown(
    """
    <div class="section">
        <h2>Contact</h2>
        <p>
            Feel free to reach out to me for collaborations or inquiries! You can contact me at:
            <a href="ayangantayat095@gmail.com" style="color: #58a6ff; text-decoration: none;">your.email@example.com</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer Section
st.markdown(
    """
    <div class="footer">
        <p>Made with ❤️ By Ayan Gantayat using Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True,
)
