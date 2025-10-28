# pages/1_Início.py
import streamlit as st
from app import t, data

st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 class='main-title'>Transformo Ideias em</h1>
    <h1 class='main-title' style='font-size: 4rem;'>Experiências Digitais</h1>
    <p class='section-subtitle' style='max-width: 600px; margin: 2rem auto;'>
        UX/UI Designer & Full Stack Developer com mais de 10 anos criando soluções que unem design elegante e tecnologia robusta.
    </p>
</div>
""", unsafe_allow_html=True)

# Botões funcionais
st.markdown("<div style='text-align: center; margin: 3rem 0;'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "**🚀 Ver Meus Projetos**", 
        use_container_width=True,
        type="primary"
    ):
        try:
            st.switch_page("pages/4_Projetos.py")
        except:
            st.success("🎯 Navegando para Projetos...")
            # Se a navegação não funcionar, mostra uma mensagem
            st.info("Use o menu lateral para acessar a página de Projetos")

with col2:
    if st.button(
        "**📖 Saber Mais**", 
        use_container_width=True,
        type="secondary"
    ):
        try:
            st.switch_page("pages/2_Sobre.py")
        except:
            st.success("👤 Navegando para Sobre...")
            st.info("Use o menu lateral para acessar a página Sobre")

st.markdown("</div>", unsafe_allow_html=True)

# Stats
st.markdown("---")

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
        <div class='stat-number'>95%</div>
        <div style='color: var(--text-secondary);'>Clientes Satisfeitos</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div class='stat-number'>10+</div>
        <div style='color: var(--text-secondary);'>Anos de Experiência</div>
    </div>
    """, unsafe_allow_html=True)

# Cards de Especialização
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>Minhas Especialidades</h2></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 3rem; margin-bottom: 1.5rem;'>🎨</div>
        <h3>Design UX/UI</h3>
        <p style='color: var(--text-secondary);'>
            Criação de interfaces intuitivas e experiências memoráveis com foco na jornada do usuário.
        </p>
        <div style='margin-top: 1.5rem;'>
            <span class='skill-tag'>Figma</span>
            <span class='skill-tag'>Adobe XD</span>
            <span class='skill-tag'>Prototipagem</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 3rem; margin-bottom: 1.5rem;'>💻</div>
        <h3>Desenvolvimento Full Stack</h3>
        <p style='color: var(--text-secondary);'>
            Desenvolvimento de aplicações completas com tecnologias modernas e arquitetura escalável.
        </p>
        <div style='margin-top: 1.5rem;'>
            <span class='skill-tag'>React</span>
            <span class='skill-tag'>Python</span>
            <span class='skill-tag'>Node.js</span>
        </div>
    </div>
    """, unsafe_allow_html=True)