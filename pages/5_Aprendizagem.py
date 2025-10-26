# pages/5_Aprendizagem.py
import streamlit as st

st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 class='section-title'>📚 Centro de Aprendizagem</h1>
    <p class='section-subtitle'>Compartilhando conhecimento e recursos educacionais</p>
</div>
""", unsafe_allow_html=True)

# Vídeo Principal
st.markdown("### 🎥 Aula em Destaque")
col1, col2 = st.columns([2, 1])

with col1:
    # Vídeo placeholder - você pode substituir por um vídeo real
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

with col2:
    st.markdown("""
    <div class='modern-card'>
        <h4 style='margin-bottom: 1rem;'>📋 Sobre esta Aula</h4>
        <div style='margin-bottom: 1rem;'>
            <p style='color: var(--text-secondary); font-size: 0.9rem;'>
                <strong>Conteúdo:</strong> Design Thinking, UX Research, Prototipagem
            </p>
            <p style='color: var(--text-secondary); font-size: 0.9rem;'>
                <strong>Pré-requisitos:</strong> Noções básicas de design
            </p>
            <p style='color: var(--text-secondary); font-size: 0.9rem;'>
                <strong>Material:</strong> PDF + Arquivos Figma
            </p>
        </div>
        <button class='download-btn' style='width: 100%; margin-bottom: 0.5rem;'>
            📥 Baixar Material
        </button>
        <button style='
            background: transparent;
            color: var(--primary);
            border: 2px solid var(--primary);
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 500;
            cursor: pointer;
            width: 100%;
        '>
            📖 Ver Transcrição
        </button>
    </div>
    """, unsafe_allow_html=True)

# Materiais para Download
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>📂 Materiais Didáticos</h2></div>", unsafe_allow_html=True)

materiais_cols = st.columns(3)

with materiais_cols[0]:
    st.markdown("""
    <div class='learning-card'>
        <div style='font-size: 3rem; text-align: center; margin-bottom: 1rem;'>📊</div>
        <h4 style='text-align: center;'>Guia de UX Research</h4>
        <p style='color: var(--text-secondary); text-align: center; font-size: 0.9rem;'>
            Metodologias completas para pesquisa com usuários
        </p>
        <div style='text-align: center; margin: 1rem 0;'>
            <span class='skill-tag'>PDF</span>
            <span class='skill-tag'>2.4 MB</span>
        </div>
        <button class='download-btn' style='width: 100%;'>
            📥 Baixar Guia
        </button>
    </div>
    """, unsafe_allow_html=True)

with materiais_cols[1]:
    st.markdown("""
    <div class='learning-card'>
        <div style='font-size: 3rem; text-align: center; margin-bottom: 1rem;'>🎨</div>
        <h4 style='text-align: center;'>Kit UI Design</h4>
        <p style='color: var(--text-secondary); text-align: center; font-size: 0.9rem;'>
            Componentes e templates para Figma
        </p>
        <div style='text-align: center; margin: 1rem 0;'>
            <span class='skill-tag'>Figma</span>
            <span class='skill-tag'>5.1 MB</span>
        </div>
        <button class='download-btn' style='width: 100%;'>
            📥 Baixar Kit
        </button>
    </div>
    """, unsafe_allow_html=True)

with materiais_cols[2]:
    st.markdown("""
    <div class='learning-card'>
        <div style='font-size: 3rem; text-align: center; margin-bottom: 1rem;'>💻</div>
        <h4 style='text-align: center;'>Código Fonte</h4>
        <p style='color: var(--text-secondary); text-align: center; font-size: 0.9rem;'>
            Exemplos de código e projetos práticos
        </p>
        <div style='text-align: center; margin: 1rem 0;'>
            <span class='skill-tag'>ZIP</span>
            <span class='skill-tag'>8.7 MB</span>
        </div>
        <button class='download-btn' style='width: 100%;'>
            📥 Baixar Código
        </button>
    </div>
    """, unsafe_allow_html=True)

# Quiz Interativo
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>🧠 Teste Seu Conhecimento</h2></div>", unsafe_allow_html=True)

quiz_col1, quiz_col2 = st.columns([2, 1])

with quiz_col1:
    st.markdown("""
    <div class='modern-card'>
        <h3 style='margin-bottom: 1.5rem;'>Quiz: Princípios de UX Design</h3>
        
        <div class='quiz-option'>
            <strong>1. O que significa a sigla "UX"?</strong>
            <div style='margin-top: 0.5rem;'>
                <input type='radio' name='q1' id='q1a'> <label for='q1a'>User Experience</label><br>
                <input type='radio' name='q1' id='q1b'> <label for='q1b'>User Example</label><br>
                <input type='radio' name='q1' id='q1c'> <label for='q1c'>Ultra Experience</label>
            </div>
        </div>
        
        <div class='quiz-option'>
            <strong>2. Qual é o objetivo principal do Design Thinking?</strong>
            <div style='margin-top: 0.5rem;'>
                <input type='radio' name='q2' id='q2a'> <label for='q2a'>Resolver problemas complexos</label><br>
                <input type='radio' name='q2' id='q2b'> <label for='q2b'>Criar designs bonitos</label><br>
                <input type='radio' name='q2' id='q2c'> <label for='q2c'>Vender mais produtos</label>
            </div>
        </div>
        
        <div class='quiz-option'>
            <strong>3. O que é um "Wireframe"?</strong>
            <div style='margin-top: 0.5rem;'>
                <input type='radio' name='q3' id='q3a'> <label for='q3a'>Estrutura visual básica</label><br>
                <input type='radio' name='q3' id='q3b'> <label for='q3b'>Código fonte</label><br>
                <input type='radio' name='q3' id='q3c'> <label for='q3c'>Imagem final do produto</label>
            </div>
        </div>
        
        <button class='download-btn' style='width: 100%; margin-top: 1rem;'>
            ✅ Verificar Respostas
        </button>
    </div>
    """, unsafe_allow_html=True)

with quiz_col2:
    st.markdown("""
    <div class='modern-card'>
        <h4 style='margin-bottom: 1rem;'>📈 Seu Progresso</h4>
        <div style='text-align: center; margin-bottom: 2rem;'>
            <div style='
                width: 100px;
                height: 100px;
                border-radius: 50%;
                background: conic-gradient(var(--primary) 75%, var(--surface) 0);
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 1rem;
                font-size: 1.5rem;
                font-weight: bold;
                color: var(--text);
            '>
                75%
            </div>
            <p style='color: var(--text-secondary);'>Progresso no Curso</p>
        </div>
        
        <div style='margin-bottom: 1.5rem;'>
            <p style='color: var(--text-secondary); font-size: 0.9rem;'>
                <strong>🎯 Conquistas:</strong>
            </p>
            <div style='display: flex; flex-direction: column; gap: 0.5rem;'>
                <span style='background: rgba(34, 197, 94, 0.2); color: #22c55e; padding: 4px 8px; border-radius: 12px; font-size: 0.8rem;'>✅ Quiz Iniciante</span>
                <span style='background: rgba(34, 197, 94, 0.2); color: #22c55e; padding: 4px 8px; border-radius: 12px; font-size: 0.8rem;'>✅ Material Baixado</span>
                <span style='background: rgba(99, 102, 241, 0.2); color: var(--primary); padding: 4px 8px; border-radius: 12px; font-size: 0.8rem;'>📚 3/5 Aulas</span>
            </div>
        </div>
        
        <button style='
            background: var(--gradient);
            color: white;
            border: none;
            padding: 10px;
            border-radius: 8px;
            font-weight: 500;
            cursor: pointer;
            width: 100%;
        '>
            🏆 Ver Certificado
        </button>
    </div>
    """, unsafe_allow_html=True)

# Próximas Aulas
st.markdown("---")
st.markdown("<div style='text-align: center; margin: 3rem 0;'><h2 class='section-title'>🔄 Próximas Aulas</h2></div>", unsafe_allow_html=True)

aulas_cols = st.columns(4)

with aulas_cols[0]:
    st.markdown("""
    <div class='learning-card'>
        <div style='font-size: 2.5rem; text-align: center; margin-bottom: 1rem;'>📱</div>
        <h5 style='text-align: center;'>Mobile First</h5>
        <p style='color: var(--text-secondary); text-align: center; font-size: 0.8rem;'>
            Design para dispositivos móveis
        </p>
        <div style='text-align: center; margin-top: 1rem;'>
            <span class='skill-tag' style='font-size: 0.7rem;'>Próxima</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with aulas_cols[1]:
    st.markdown("""
    <div class='learning-card'>
        <div style='font-size: 2.5rem; text-align: center; margin-bottom: 1rem;'>🎯</div>
        <h5 style='text-align: center;'>Acessibilidade</h5>
        <p style='color: var(--text-secondary); text-align: center; font-size: 0.8rem;'>
            Design inclusivo para todos
        </p>
        <div style='text-align: center; margin-top: 1rem;'>
            <span class='skill-tag' style='font-size: 0.7rem;'>Em breve</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with aulas_cols[2]:
    st.markdown("""
    <div class='learning-card'>
        <div style='font-size: 2.5rem; text-align: center; margin-bottom: 1rem;'>🚀</div>
        <h5 style='text-align: center;'>Performance</h5>
        <p style='color: var(--text-secondary); text-align: center; font-size: 0.8rem;'>
            Otimização e métricas
        </p>
        <div style='text-align: center; margin-top: 1rem;'>
            <span class='skill-tag' style='font-size: 0.7rem;'>Em breve</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with aulas_cols[3]:
    st.markdown("""
    <div class='learning-card'>
        <div style='font-size: 2.5rem; text-align: center; margin-bottom: 1rem;'>💼</div>
        <h5 style='text-align: center;'>Case Study</h5>
        <p style='color: var(--text-secondary); text-align: center; font-size: 0.8rem;'>
            Projeto real passo a passo
        </p>
        <div style='text-align: center; margin-top: 1rem;'>
            <span class='skill-tag' style='font-size: 0.7rem;'>Final</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Call to Action
st.markdown("---")
st.markdown("""
<div class='modern-card' style='text-align: center; background: linear-gradient(135deg, var(--primary), var(--secondary));'>
    <h2 style='color: white; margin-bottom: 1rem;'>🚀 Pronto para Aprender Mais?</h2>
    <p style='color: rgba(255,255,255,0.8); margin-bottom: 2rem;'>
        Junte-se à comunidade de aprendizes e tenha acesso a todos os recursos
    </p>
    <button style='
        background: white;
        color: var(--primary);
        border: none;
        padding: 12px 32px;
        border-radius: 12px;
        font-weight: 600;
        cursor: pointer;
        font-size: 1.1rem;
    '>
        📧 Entrar em Contato
    </button>
</div>
""", unsafe_allow_html=True)