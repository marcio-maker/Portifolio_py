# pages/6_Contato.py
import streamlit as st
from app import t, data

st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 class='section-title'>Vamos Conversar</h1>
    <p class='section-subtitle'>Pronto para transformar sua ideia em realidade?</p>
    <p style='color: var(--text-secondary); max-width: 600px; margin: 0 auto;'>
        Entre em contato e vamos criar algo extraordinário juntos.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    with st.form("contact_form"):
        st.markdown("### 📝 Envie uma Mensagem")
        
        name = st.text_input("Seu Nome", placeholder="Como gostaria de ser chamado?")
        email = st.text_input("Seu Email", placeholder="seu@email.com")
        message = st.text_area("Sua Mensagem", placeholder="Conte-me sobre seu projeto...", height=150)
        
        submitted = st.form_submit_button("Enviar Mensagem", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("🎉 Mensagem enviada! Retornarei em breve.")
            else:
                st.error("❌ Por favor, preencha todos os campos.")

with col2:
    st.markdown("### 📞 Informações de Contato")
    
    st.markdown("""
    <div class='modern-card'>
        <div style='display: flex; align-items: center; margin-bottom: 1.5rem;'>
            <div style='font-size: 1.5rem; margin-right: 1rem;'>📧</div>
            <div>
                <div style='font-weight: 600;'>Email</div>
                <div style='color: var(--text-secondary);'>marcio.maker@email.com</div>
            </div>
        </div>
        
        <div style='display: flex; align-items: center; margin-bottom: 1.5rem;'>
            <div style='font-size: 1.5rem; margin-right: 1rem;'>💼</div>
            <div>
                <div style='font-weight: 600;'>LinkedIn</div>
                <div style='color: var(--text-secondary);'>linkedin.com/in/marciomaker</div>
            </div>
        </div>
        
        <div style='display: flex; align-items: center; margin-bottom: 1.5rem;'>
            <div style='font-size: 1.5rem; margin-right: 1rem;'>🐙</div>
            <div>
                <div style='font-weight: 600;'>GitHub</div>
                <div style='color: var(--text-secondary);'>github.com/marciomaker</div>
            </div>
        </div>
        
        <div style='display: flex; align-items: center;'>
            <div style='font-size: 1.5rem; margin-right: 1rem;'>🎨</div>
            <div>
                <div style='font-weight: 600;'>Behance</div>
                <div style='color: var(--text-secondary);'>behance.net/marciomaker</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Disponibilidade
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>Disponibilidade</h2></div>", unsafe_allow_html=True)

avail_cols = st.columns(3)

with avail_cols[0]:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 2.5rem; margin-bottom: 1rem;'>⚡</div>
        <h4>Resposta Rápida</h4>
        <p style='color: var(--text-secondary);'>Retorno em até 24h</p>
    </div>
    """, unsafe_allow_html=True)

with avail_cols[1]:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 2.5rem; margin-bottom: 1rem;'>🌎</div>
        <h4>Atendimento Global</h4>
        <p style='color: var(--text-secondary);'>Clientes em todo mundo</p>
    </div>
    """, unsafe_allow_html=True)

with avail_cols[2]:
    st.markdown("""
    <div class='modern-card' style='text-align: center;'>
        <div style='font-size: 2.5rem; margin-bottom: 1rem;'>💬</div>
        <h4>Suporte Contínuo</h4>
        <p style='color: var(--text-secondary);'>Acompanhamento pós-projeto</p>
    </div>
    """, unsafe_allow_html=True)