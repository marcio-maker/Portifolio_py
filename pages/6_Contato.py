# pages/6_Contato.py
import streamlit as st
from app import t, data

# Título e introdução
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 class='section-title'>Vamos Conversar</h1>
    <p class='section-subtitle'>Pronto para transformar sua ideia em realidade?</p>
    <p style='color: var(--text-secondary); max-width: 600px; margin: 0 auto;'>
        Entre em contato e vamos criar algo extraordinário juntos.
    </p>
</div>
""", unsafe_allow_html=True)

# Layout de duas colunas
col1, col2 = st.columns([2, 1])

# Coluna 1 - Formulário de contato
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

# Coluna 2 - Informações de contato
with col2:
    st.markdown("### 📞 Informações de Contato")

    with st.container():
        st.write("**📧 Email**")
        st.caption("marcio.maker@email.com")

        st.write("**💼 LinkedIn**")
        st.link_button("linkedin.com/in/marciomaker", "https://linkedin.com/in/marciomaker")

        st.write("**🐙 GitHub**")
        st.link_button("github.com/marciomaker", "https://github.com/marciomaker")

        st.write("**🎨 Behance**")
        st.link_button("behance.net/marciomaker", "https://behance.net/marciomaker")

# Separador
st.markdown("---")

# Seção de Disponibilidade
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>Disponibilidade</h2></div>", unsafe_allow_html=True)

avail_cols = st.columns(3)

with avail_cols[0]:
    with st.container():
        st.markdown("### ⚡ Resposta Rápida")
        st.caption("Retorno em até 24h")

with avail_cols[1]:
    with st.container():
        st.markdown("### 🌎 Atendimento Global")
        st.caption("Clientes em todo o mundo")

with avail_cols[2]:
    with st.container():
        st.markdown("### 💬 Suporte Contínuo")
        st.caption("Acompanhamento pós-projeto")
