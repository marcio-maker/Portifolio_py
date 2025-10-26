# pages/2_Sobre.py
import streamlit as st
from data import texts, data, icon_map

def t(key):
    lang = st.session_state.settings["lang"]
    text_item = texts.get(key, {})
    if isinstance(text_item, dict) and lang in text_item:
        return text_item[lang]
    return key

st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 class='section-title'>Sobre Mim</h1>
    <p class='section-subtitle'>Um Designer com Mentalidade de Engenheiro</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class='modern-card'>
        <h3 style='margin-bottom: 1.5rem;'>Minha Jornada</h3>
        <p style='color: var(--text-secondary); line-height: 1.8; font-size: 1.1rem;'>
            Com mais de uma década de experiência, especializo-me em criar soluções digitais que não apenas 
            impressionam visualmente, mas também resolvem problemas reais de negócio.
        </p>
        <p style='color: var(--text-secondary); line-height: 1.7; margin-top: 1.5rem;'>
            Minha abordagem única combina a sensibilidade artística do design com a precisão técnica da 
            engenharia, garantindo que cada projeto seja tanto bonito quanto funcional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills
    st.markdown("""
    <div class='modern-card'>
        <h3 style='margin-bottom: 1.5rem;'>🛠️ Tecnologias & Ferramentas</h3>
        <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
            <span class='skill-tag'>Figma</span>
            <span class='skill-tag'>Adobe XD</span>
            <span class='skill-tag'>React</span>
            <span class='skill-tag'>Vue.js</span>
            <span class='skill-tag'>TypeScript</span>
            <span class='skill-tag'>Python</span>
            <span class='skill-tag'>Django</span>
            <span class='skill-tag'>Node.js</span>
            <span class='skill-tag'>PostgreSQL</span>
            <span class='skill-tag'>MongoDB</span>
            <span class='skill-tag'>Docker</span>
            <span class='skill-tag'>AWS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='
            width: 200px; 
            height: 200px; 
            border-radius: 50%; 
            background: linear-gradient(135deg, #6366f1, #8b5cf6); 
            margin: 0 auto 2rem; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-size: 3rem; 
            color: white;
        '>
            👨‍💻
        </div>
        <h3 style='margin-bottom: 0.5rem;'>Marcio Maker</h3>
        <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
            Senior UX/UI Designer & Full Stack Developer
        </p>
        
        <div style='display: flex; justify-content: center; gap: 1rem;'>
            <button style='
                background: var(--primary); 
                color: white; 
                border: none; 
                border-radius: 50%; 
                width: 40px; 
                height: 40px; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                cursor: pointer;
            '>📧</button>
            <button style='
                background: var(--primary); 
                color: white; 
                border: none; 
                border-radius: 50%; 
                width: 40px; 
                height: 40px; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                cursor: pointer;
            '>💼</button>
            <button style='
                background: var(--primary); 
                color: white; 
                border: none; 
                border-radius: 50%; 
                width: 40px; 
                height: 40px; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                cursor: pointer;
            '>🐙</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Estatísticas
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>Minha Jornada em Números</h2></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div class='stat-number'>50+</div>
        <div style='color: var(--text-secondary);'>Projetos Entregues</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div class='stat-number'>10+</div>
        <div style='color: var(--text-secondary);'>Anos de Experiência</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div class='stat-number'>100%</div>
        <div style='color: var(--text-secondary);'>Clientes Satisfeitos</div>
    </div>
    """, unsafe_allow_html=True)