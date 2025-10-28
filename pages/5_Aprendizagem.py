# pages/5_Aprendizagem.py
import streamlit as st

# ========== CABEÇALHO ==========
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 class='section-title'>📚 Centro de Aprendizagem</h1>
    <p class='section-subtitle'>Compartilhando conhecimento e recursos educacionais</p>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 1: VÍDEO PRINCIPAL ==========
st.markdown("### 🎥 Aula em Destaque")
video_col1, video_col2 = st.columns([2, 1])

with video_col1:
    st.markdown("""
    <div class='modern-card'>
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    height: 300px;
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-size: 1.5rem;
                    margin-bottom: 1rem;'>
            🎬 Player de Vídeo
        </div>
        <h3>Design Thinking na Prática</h3>
        <p style='color: var(--text-secondary);'>
            Aprenda a aplicar metodologias de Design Thinking em projetos reais.
            Esta aula aborda desde a imersão até a prototipagem.
        </p>
        <div style='display: flex; gap: 0.5rem; margin-top: 1rem;'>
            <span class='skill-tag'>🕒 45min</span>
            <span class='skill-tag'>📊 Intermediário</span>
            <span class='skill-tag'>🎨 Design</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with video_col2:
    st.markdown("### 📋 Sobre esta Aula")
    st.caption("**Conteúdo:** Design Thinking, UX Research, Prototipagem")
    st.caption("**Pré-requisitos:** Noções básicas de design")
    st.caption("**Material:** PDF + Arquivos Figma")

    if st.button("📥 Baixar Material", use_container_width=True):
        st.success("📥 Material baixado com sucesso!")

    if st.button("📖 Ver Transcrição", use_container_width=True, type="secondary"):
        st.info("📖 Transcrição da aula carregada...")

# ========== SEÇÃO 2: MATERIAIS DIDÁTICOS ==========
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>📂 Materiais Didáticos</h2></div>", unsafe_allow_html=True)

materiais = [
    {"icon": "📊", "titulo": "Guia de UX Research", "desc": "Metodologias completas para pesquisa com usuários", "tipo": "PDF", "tam": "2.4 MB"},
    {"icon": "🎨", "titulo": "Kit UI Design", "desc": "Componentes e templates para Figma", "tipo": "Figma", "tam": "5.1 MB"},
    {"icon": "💻", "titulo": "Código Fonte", "desc": "Exemplos de código e projetos práticos", "tipo": "ZIP", "tam": "8.7 MB"}
]

cols = st.columns(3)
for i, mat in enumerate(materiais):
    with cols[i]:
        st.markdown(f"### {mat['icon']} {mat['titulo']}")
        st.caption(mat['desc'])
        st.caption(f"{mat['tipo']} • {mat['tam']}")
        if st.button(f"📥 Baixar {mat['tipo']}", key=f"mat_{i}", use_container_width=True):
            st.success(f"{mat['icon']} {mat['titulo']} baixado com sucesso!")

# ========== SEÇÃO 3: QUIZ ==========
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>🧠 Teste Seu Conhecimento</h2></div>", unsafe_allow_html=True)

quiz_col1, quiz_col2 = st.columns([2, 1])

# QUIZ PRINCIPAL
with quiz_col1:
    st.markdown("### Quiz: Princípios de UX Design")

    q1 = st.radio("1️⃣ O que significa 'UX'?", ["User Experience", "User Example", "Ultra Experience"])
    q2 = st.radio("2️⃣ Qual é o objetivo principal do Design Thinking?", ["Resolver problemas complexos", "Criar designs bonitos", "Vender mais produtos"])
    q3 = st.radio("3️⃣ O que é um 'Wireframe'?", ["Estrutura visual básica", "Código fonte", "Imagem final do produto"])

    if st.button("✅ Verificar Respostas", use_container_width=True):
        score = sum([
            q1 == "User Experience",
            q2 == "Resolver problemas complexos",
            q3 == "Estrutura visual básica"
        ])
        st.success(f"🎯 Você acertou {score} de 3 questões!")
        if score == 3:
            st.balloons()

# PROGRESSO E CONQUISTAS
with quiz_col2:
    st.markdown("### 📈 Seu Progresso")
    progress = 0.75
    st.progress(progress)
    st.caption("Progresso no Curso: **75%**")

    st.markdown("### 🎯 Conquistas")
    st.write("✅ Quiz Iniciante")
    st.write("✅ Material Baixado")
    st.write("📚 3/5 Aulas Concluídas")

# ========== SEÇÃO 4: PRÓXIMAS AULAS ==========
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>🔄 Próximas Aulas</h2></div>", unsafe_allow_html=True)

aulas = [
    ("📱", "Mobile First", "Design para dispositivos móveis", "Próxima"),
    ("🎯", "Acessibilidade", "Design inclusivo para todos", "Em breve"),
    ("🚀", "Performance", "Otimização e métricas", "Em breve"),
    ("💼", "Case Study", "Projeto real passo a passo", "Final"),
]

cols = st.columns(4)
for i, (icon, titulo, desc, status) in enumerate(aulas):
    with cols[i]:
        st.markdown(f"### {icon} {titulo}")
        st.caption(desc)
        st.caption(f"📅 {status}")

# ========== SEÇÃO 5: CHAMADA FINAL ==========
st.markdown("---")
st.markdown("""
<div class='modern-card' style='text-align: center; background: linear-gradient(135deg, #6366f1, #8b5cf6); padding: 2rem; border-radius: 12px;'>
    <h2 style='color: white; margin-bottom: 1rem;'>🚀 Pronto para Aprender Mais?</h2>
    <p style='color: rgba(255,255,255,0.8); margin-bottom: 2rem;'>
        Junte-se à comunidade de aprendizes e tenha acesso a todos os recursos.
    </p>
</div>
""", unsafe_allow_html=True)

if st.button("📧 Entrar em Contato", use_container_width=True):
    st.success("📧 Redirecionando para a página de contato...")
