# pages/4_Projetos.py
import streamlit as st
from data import texts, data

def t(key):
    lang = st.session_state.settings["lang"]
    text_item = texts.get(key, {})
    if isinstance(text_item, dict) and lang in text_item:
        return text_item[lang]
    return key

st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 class='section-title'>Portfólio</h1>
    <p class='section-subtitle'>Trabalhos que Contam Histórias</p>
</div>
""", unsafe_allow_html=True)

# Abas
tab1, tab2 = st.tabs(["🎨 Design UX/UI", "💻 Desenvolvimento"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='project-card'>
            <div style='height: 200px; overflow: hidden; border-radius: 16px 16px 0 0;'>
                <img src='https://images.unsplash.com/photo-1561070791-2526d30994b5?w=400&h=300&fit=crop' 
                     style='width: 100%; height: 100%; object-fit: cover;'>
            </div>
            <div style='padding: 1.5rem;'>
                <h4 style='margin-bottom: 0.5rem;'>Plataforma SaaS B2B</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
                    Redesign completo de plataforma de análise de dados com foco em usabilidade e performance.
                </p>
                <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                    <span class='skill-tag'>Figma</span>
                    <span class='skill-tag'>Design System</span>
                    <span class='skill-tag'>UX Research</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button('🔍 Ver Detalhes', key='project1', use_container_width=True):
            st.success('📂 Abrindo detalhes do projeto SaaS B2B')
    
    with col2:
        st.markdown("""
        <div class='project-card'>
            <div style='height: 200px; overflow: hidden; border-radius: 16px 16px 0 0;'>
                <img src='https://images.unsplash.com/photo-1551650975-87deedd944c3?w=400&h=300&fit=crop' 
                     style='width: 100%; height: 100%; object-fit: cover;'>
            </div>
            <div style='padding: 1.5rem;'>
                <h4 style='margin-bottom: 0.5rem;'>App Fitness Mobile</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
                    Design de aplicativo mobile para rastreamento de atividades físicas e nutrição.
                </p>
                <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                    <span class='skill-tag'>Adobe XD</span>
                    <span class='skill-tag'>Mobile First</span>
                    <span class='skill-tag'>User Testing</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button('🔍 Ver Detalhes', key='project2', use_container_width=True):
            st.success('📂 Abrindo detalhes do App Fitness')

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='project-card'>
            <div style='height: 200px; overflow: hidden; border-radius: 16px 16px 0 0;'>
                <img src='https://images.unsplash.com/photo-1555066931-436e138a05c3?w=400&h=300&fit=crop' 
                     style='width: 100%; height: 100%; object-fit: cover;'>
            </div>
            <div style='padding: 1.5rem;'>
                <h4 style='margin-bottom: 0.5rem;'>API Microserviços</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
                    Arquitetura de microserviços escalável com Python, Django e Docker.
                </p>
                <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                    <span class='skill-tag'>Python</span>
                    <span class='skill-tag'>Django</span>
                    <span class='skill-tag'>Docker</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button('🔍 Ver Detalhes', key='project3', use_container_width=True):
            st.success('📂 Abrindo detalhes da API Microserviços')
    
    with col2:
        st.markdown("""
        <div class='project-card'>
            <div style='height: 200px; overflow: hidden; border-radius: 16px 16px 0 0;'>
                <img src='https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop' 
                     style='width: 100%; height: 100%; object-fit: cover;'>
            </div>
            <div style='padding: 1.5rem;'>
                <h4 style='margin-bottom: 0.5rem;'>Dashboard Analytics</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
                    Dashboard interativo para visualização de dados em tempo real.
                </p>
                <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                    <span class='skill-tag'>React</span>
                    <span class='skill-tag'>D3.js</span>
                    <span class='skill-tag'>TypeScript</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button('🔍 Ver Detalhes', key='project4', use_container_width=True):
            st.success('📂 Abrindo detalhes do Dashboard Analytics')

# Estatísticas
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>Impacto dos Projetos</h2></div>", unsafe_allow_html=True)

metric_cols = st.columns(4)

with metric_cols[0]:
    st.markdown("""
    <div style='text-align: center;'>
        <div class='stat-number'>50+</div>
        <p style='color: var(--text-secondary);'>Projetos Entregues</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[1]:
    st.markdown("""
    <div style='text-align: center;'>
        <div class='stat-number'>95%</div>
        <p style='color: var(--text-secondary);'>Satisfação do Cliente</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[2]:
    st.markdown("""
    <div style='text-align: center;'>
        <div class='stat-number'>40%</div>
        <p style='color: var(--text-secondary);'>Aumento de Eficiência</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[3]:
    st.markdown("""
    <div style='text-align: center;'>
        <div class='stat-number'>100%</div>
        <p style='color: var(--text-secondary);'>Entrega no Prazo</p>
    </div>
    """, unsafe_allow_html=True)