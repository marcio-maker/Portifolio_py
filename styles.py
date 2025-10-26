# styles.py
import streamlit as st

def apply_modern_styles():
    """Aplica todos os estilos CSS modernos"""
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <style>
    :root {
        --primary: #6366f1;
        --secondary: #8b5cf6;
        --accent: #06b6d4;
        --background: #0f172a;
        --surface: #1e293b;
        --text: #f8fafc;
        --text-secondary: #94a3b8;
        --gradient: linear-gradient(135deg, #6366f1, #8b5cf6);
    }
    
    [data-theme="light"] {
        --background: #ffffff;
        --surface: #f8fafc;
        --text: #1e293b;
        --text-secondary: #64748b;
    }
    
    .stApp {
        font-family: 'Inter', sans-serif;
        background: var(--background);
        color: var(--text);
        transition: all 0.3s ease;
    }
    
    /* Títulos Principais */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        line-height: 1.1;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: var(--text-secondary);
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Cards Modernos */
    .modern-card {
        background: var(--surface);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid rgba(99, 102, 241, 0.1);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .modern-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.2);
        border-color: rgba(99, 102, 241, 0.3);
    }
    
    /* Cards de Projeto */
    .project-card {
        background: var(--surface);
        border-radius: 16px;
        border: 1px solid rgba(99, 102, 241, 0.1);
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.2);
    }
    
    /* Cards de Aprendizagem */
    .learning-card {
        background: var(--surface);
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(99, 102, 241, 0.1);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .learning-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(99, 102, 241, 0.15);
    }
    
    /* Tags de Habilidade */
    .skill-tag {
        display: inline-block;
        background: rgba(99, 102, 241, 0.1);
        color: var(--primary);
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.2rem;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    /* Números Estatísticos */
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Botões */
    .download-btn {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .download-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    
    /* Quiz */
    .quiz-option {
        background: var(--surface);
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    /* Navegação Preview */
    .nav-preview-card {
        background: var(--surface);
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(99, 102, 241, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        text-align: center;
    }
    
    .nav-preview-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.2);
        border-color: rgba(99, 102, 241, 0.3);
    }
    
    /* Sidebar */
    .sidebar-section {
        background: var(--surface);
        padding: 1.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    /* Autenticação */
    .auth-container {
        max-width: 400px;
        margin: 100px auto;
        padding: 2rem;
        background: var(--surface);
        border-radius: 20px;
        border: 1px solid rgba(99, 102, 241, 0.3);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    
    .auth-title {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .auth-subtitle {
        text-align: center;
        color: var(--text-secondary);
        margin-bottom: 2rem;
    }
    
    /* Esconde elementos do Streamlit */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stDeployButton { display: none; }
    header { visibility: hidden; }
    
    /* Ajusta cores dos componentes Streamlit */
    .stTextInput > div > div > input {
        background: var(--surface);
        color: var(--text);
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    .stTextArea > div > div > textarea {
        background: var(--surface);
        color: var(--text);
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    .stSelectbox > div > div {
        background: var(--surface);
        color: var(--text);
    }
    
    /* Ajusta o sidebar */
    .css-1d391kg, .css-1lcbmhc {
        background: var(--surface);
    }
    
    [data-testid="stSidebar"] {
        background: var(--surface);
        border-right: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    </style>
    """, unsafe_allow_html=True)

def apply_theme():
    """Aplica o tema selecionado"""
    if "settings" in st.session_state:
        theme = st.session_state.settings.get("theme", "dark")
        st.markdown(f"""
        <script>
        document.documentElement.setAttribute('data-theme', '{theme}');
        </script>
        """, unsafe_allow_html=True)