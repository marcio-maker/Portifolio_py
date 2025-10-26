# pages/3_Serviços.py
import streamlit as st
from app import t, data

st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 class='section-title'>Serviços</h1>
    <p class='section-subtitle'>Soluções Completas para seu Projeto Digital</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='modern-card' style='text-align: center; height: 100%;'>
        <div style='font-size: 3rem; margin-bottom: 1.5rem;'>🎨</div>
        <h3 style='margin-bottom: 1rem;'>Design UX/UI</h3>
        <p style='color: var(--text-secondary); line-height: 1.6;'>
            Criação de interfaces intuitivas e experiências memoráveis com foco na jornada do usuário 
            e nas melhores práticas de usabilidade.
        </p>
        <div style='margin-top: 2rem;'>
            <span class='skill-tag'>User Research</span>
            <span class='skill-tag'>Wireframing</span>
            <span class='skill-tag'>Prototipagem</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='modern-card' style='text-align: center; height: 100%;'>
        <div style='font-size: 3rem; margin-bottom: 1.5rem;'>💻</div>
        <h3 style='margin-bottom: 1rem;'>Desenvolvimento Full Stack</h3>
        <p style='color: var(--text-secondary); line-height: 1.6;'>
            Desenvolvimento de aplicações web completas, do backend ao frontend, com tecnologias 
            modernas e arquitetura escalável.
        </p>
        <div style='margin-top: 2rem;'>
            <span class='skill-tag'>React</span>
            <span class='skill-tag'>Node.js</span>
            <span class='skill-tag'>Python</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='modern-card' style='text-align: center; height: 100%;'>
        <div style='font-size: 3rem; margin-bottom: 1.5rem;'>🚀</div>
        <h3 style='margin-bottom: 1rem;'>Consultoria & Mentoria</h3>
        <p style='color: var(--text-secondary); line-height: 1.6;'>
            Orientação técnica e estratégica para equipes e projetos, ajudando a tomar as melhores 
            decisões de arquitetura e produto.
        </p>
        <div style='margin-top: 2rem;'>
            <span class='skill-tag'>Arquitetura</span>
            <span class='skill-tag'>Best Practices</span>
            <span class='skill-tag'>Code Review</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Processo de Trabalho
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>Meu Processo de Trabalho</h2></div>", unsafe_allow_html=True)

process_cols = st.columns(4)

with process_cols[0]:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 2.5rem; margin-bottom: 1rem;'>🔍</div>
        <h4>Pesquisa</h4>
        <p style='color: var(--text-secondary); font-size: 0.9rem;'>
            Análise profunda do problema e do usuário
        </p>
    </div>
    """, unsafe_allow_html=True)

with process_cols[1]:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 2.5rem; margin-bottom: 1rem;'>✏️</div>
        <h4>Design</h4>
        <p style='color: var(--text-secondary); font-size: 0.9rem;'>
            Criação de interfaces e protótipos
        </p>
    </div>
    """, unsafe_allow_html=True)

with process_cols[2]:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 2.5rem; margin-bottom: 1rem;'>⚡</div>
        <h4>Desenvolvimento</h4>
        <p style='color: var(--text-secondary); font-size: 0.9rem;'>
            Implementação com código limpo
        </p>
    </div>
    """, unsafe_allow_html=True)

with process_cols[3]:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 2.5rem; margin-bottom: 1rem;'>📦</div>
        <h4>Entrega</h4>
        <p style='color: var(--text-secondary); font-size: 0.9rem;'>
            Deploy e suporte contínuo
        </p>
    </div>
    """, unsafe_allow_html=True)