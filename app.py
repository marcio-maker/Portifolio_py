# app.py
import streamlit as st
import hashlib
import json
import os
from data import texts, data, get_settings, t, initialize_session_state
from styles import apply_modern_styles, apply_theme

# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(
    page_title=data["general"]["page_title"],
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SISTEMA DE AUTENTICAÇÃO ---
USER_DATA_FILE = "users.json"

def load_users():
    """Carrega os usuários do arquivo JSON"""
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users):
    """Salva os usuários no arquivo JSON"""
    try:
        with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False

def hash_password(password):
    """Cria hash da senha"""
    return hashlib.sha256(password.encode()).hexdigest()

def init_auth():
    """Inicializa o sistema de autenticação"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'show_login' not in st.session_state:
        st.session_state.show_login = True
    if 'show_register' not in st.session_state:
        st.session_state.show_register = False

def register_user(username, email, password):
    """Registra um novo usuário"""
    users = load_users()
    
    if username in users:
        return False, "Usuário já existe!"
    
    if len(password) < 6:
        return False, "Senha deve ter pelo menos 6 caracteres!"
    
    users[username] = {
        'email': email,
        'password': hash_password(password),
        'created_at': st.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    if save_users(users):
        return True, "Usuário registrado com sucesso!"
    else:
        return False, "Erro ao salvar usuário!"

def login_user(username, password):
    """Faz login do usuário"""
    users = load_users()
    
    if username not in users:
        return False, "Usuário não encontrado!"
    
    if users[username]['password'] == hash_password(password):
        st.session_state.authenticated = True
        st.session_state.current_user = username
        st.session_state.show_login = False
        return True, "Login realizado com sucesso!"
    else:
        return False, "Senha incorreta!"

def render_auth_page():
    """Renderiza a página de autenticação"""
    st.markdown("""
    <style>
    .auth-container {
        max-width: 400px;
        margin: 100px auto;
        padding: 2rem;
        background: rgba(30, 41, 59, 0.9);
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
        color: #94a3b8;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Container principal de autenticação
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    
    # Logo e título
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div style="text-align: center; font-size: 3rem; margin-bottom: 1rem;">🔐</div>', unsafe_allow_html=True)
        st.markdown('<h1 class="auth-title">Portfólio Maker</h1>', unsafe_allow_html=True)
        st.markdown('<p class="auth-subtitle">Acesse seu portfólio profissional</p>', unsafe_allow_html=True)
    
    # Abas de Login e Cadastro
    if st.session_state.show_register:
        tab1, tab2 = st.tabs(["📝 Cadastro", "🔐 Login"])
    else:
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Cadastro"])
    
    # TAB LOGIN
    with tab1:
        with st.form("login_form"):
            st.subheader("Login")
            login_username = st.text_input("👤 Usuário", placeholder="Digite seu usuário")
            login_password = st.text_input("🔒 Senha", type="password", placeholder="Digite sua senha")
            
            col1, col2 = st.columns([2, 1])
            with col1:
                login_btn = st.form_submit_button("🚀 Entrar", use_container_width=True)
            with col2:
                if st.form_submit_button("🔄 Limpar", use_container_width=True):
                    st.rerun()
            
            if login_btn and login_username and login_password:
                success, message = login_user(login_username, login_password)
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
    
    # TAB CADASTRO
    with tab2:
        with st.form("register_form"):
            st.subheader("Cadastro")
            reg_username = st.text_input("👤 Nome de usuário", placeholder="Escolha um usuário")
            reg_email = st.text_input("📧 Email", placeholder="seu@email.com")
            reg_password = st.text_input("🔒 Senha", type="password", placeholder="Mínimo 6 caracteres")
            reg_confirm = st.text_input("✅ Confirmar senha", type="password", placeholder="Digite novamente")
            
            col1, col2 = st.columns([2, 1])
            with col1:
                reg_btn = st.form_submit_button("✨ Criar Conta", use_container_width=True)
            with col2:
                if st.form_submit_button("🔄 Limpar", use_container_width=True):
                    st.rerun()
            
            if reg_btn:
                if not all([reg_username, reg_email, reg_password, reg_confirm]):
                    st.error("Por favor, preencha todos os campos!")
                elif reg_password != reg_confirm:
                    st.error("As senhas não coincidem!")
                else:
                    success, message = register_user(reg_username, reg_email, reg_password)
                    if success:
                        st.success(message)
                        st.session_state.show_register = False
                        st.rerun()
                    else:
                        st.error(message)
    
    # Rodapé
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #64748b; font-size: 0.8rem;'>
        <p>💡 <strong>Dica:</strong> Use o mesmo usuário e senha para futuros acessos</p>
        <p>🔒 Seus dados estão seguros e são armazenados localmente</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- HEADER COM USUÁRIO ---
def render_header():
    """Renderiza o header com informações do usuário"""
    with st.container():
        col1, col2, col3 = st.columns([2, 3, 2])
        
        with col1:
            button_type = "primary" if st.session_state.get('show_preview', False) else "secondary"
            if st.button("☰", help="Abrir menu rápido", use_container_width=True, type=button_type):
                st.session_state.show_preview = not st.session_state.get('show_preview', False)
                st.rerun()
        
        with col2:
            st.markdown(
                "<h2 style='text-align: center; margin: 0; color: #f8fafc;'>Marcio Maker</h2>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<p style='text-align: center; margin: 0; color: #94a3b8; font-size: 0.9rem;'>Bem-vindo, {st.session_state.current_user}! 👋</p>",
                unsafe_allow_html=True
            )
        
        with col3:
            if st.button("🚪 Sair", use_container_width=True):
                st.session_state.authenticated = False
                st.session_state.current_user = None
                st.session_state.show_login = True
                st.rerun()

# --- FUNÇÕES DO PORTFÓLIO ---
def render_navigation_preview():
    """Renderiza a prévia de navegação"""
    if st.session_state.get('show_preview', False):
        st.markdown("### 🧭 Navegação Rápida")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🏠 Início", use_container_width=True):
                st.switch_page("app.py")
        
        with col2:
            if st.button("👤 Sobre", use_container_width=True):
                try:
                    st.switch_page("pages/2_Sobre.py")
                except:
                    st.info("Página Sobre em desenvolvimento")
        
        with col3:
            if st.button("💼 Projetos", use_container_width=True):
                try:
                    st.switch_page("pages/4_Projetos.py")
                except:
                    st.info("Página Projetos em desenvolvimento")

def render_sidebar():
    """Renderiza a sidebar com controles de tema e idioma"""
    with st.sidebar:
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        
        # Controle de Tema
        st.markdown("### 🎨 Tema")
        current_theme = st.session_state.settings.get("theme", "dark")
        
        # Toggle de tema usando radio buttons
        theme_options = ["🌙 Escuro", "☀️ Claro"]
        theme_display = "🌙 Escuro" if current_theme == "dark" else "☀️ Claro"
        
        new_theme = st.radio(
            "Selecione o tema:",
            options=theme_options,
            index=0 if current_theme == "dark" else 1,
            key="theme_selector",
            label_visibility="collapsed"
        )
        
        # Atualizar tema se mudou
        if "🌙 Escuro" in new_theme and current_theme != "dark":
            st.session_state.settings["theme"] = "dark"
            st.rerun()
        elif "☀️ Claro" in new_theme and current_theme != "light":
            st.session_state.settings["theme"] = "light"
            st.rerun()
        
        # Indicador visual do tema atual
        theme_icon = "🌙" if current_theme == "dark" else "☀️"
        theme_text = "Modo Escuro" if current_theme == "dark" else "Modo Claro"
        st.markdown(f"<p style='color: var(--text-secondary); font-size: 0.9rem;'>{theme_icon} {theme_text}</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Controle de Idioma
        st.markdown("### 🌍 Idioma")
        lang = st.session_state.settings["lang"]
        lang_options = {"pt": "🇧🇷 Português", "en": "🇺🇸 English", "es": "🇪🇸 Español"}
        
        selected_lang = st.radio(
            "Selecione o idioma:",
            options=list(lang_options.values()),
            index=["pt", "en", "es"].index(lang),
            key="lang_selector",
            label_visibility="collapsed"
        )
        
        # Encontrar a chave do idioma selecionado
        for key, value in lang_options.items():
            if value == selected_lang:
                if key != lang:
                    st.session_state.settings["lang"] = key
                    st.rerun()
                break
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Footer da sidebar
        st.markdown("---")
        st.markdown(f'<div style="text-align: center; color: var(--text-muted); font-size: 0.8rem;">{t("sidebar_footer")}</div>', unsafe_allow_html=True)

def main_portfolio():
    """Função principal do portfólio (após login)"""
    try:
        # Inicializar session state se necessário
        initialize_session_state()
        
        # Aplicar estilos e tema
        apply_modern_styles()
        apply_theme()
        
        # Renderizar componentes
        render_header()
        render_navigation_preview()
        
        # Linha divisória
        st.markdown("---")
        
        # Conteúdo principal
        st.markdown('<div class="main-title">Bem-vindo ao Meu Portfólio</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">Explore meu trabalho em UX/UI Design e Desenvolvimento Full Stack</div>', unsafe_allow_html=True)
        
        # Seção de introdução
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.markdown("### 🎨 Design & Criatividade")
                st.markdown("""
                Crio experiências digitais intuitivas e visualmente atraentes, 
                focando na jornada do usuário e na otimização de conversão.
                """)
                if st.button("Ver Projetos de Design", use_container_width=True, key="design_btn"):
                    try:
                        st.switch_page("pages/4_Projetos.py")
                    except:
                        st.info("Navegue para a página de Projetos pelo menu")
        
        with col2:
            with st.container():
                st.markdown("### 💻 Desenvolvimento & Engenharia")
                st.markdown("""
                Desenvolvimento de aplicações web completas com tecnologias modernas,
                garantindo escalabilidade, performance e código limpo.
                """)
                if st.button("Ver Projetos de Código", use_container_width=True, key="code_btn"):
                    try:
                        st.switch_page("pages/4_Projetos.py")
                    except:
                        st.info("Navegue para a página de Projetos pelo menu")
        
        # Demonstração do tema
        st.markdown("---")
        st.markdown("### 🎭 Demonstração do Tema")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            with st.container():
                st.markdown('<div class="modern-card">', unsafe_allow_html=True)
                st.markdown("#### Card Exemplo")
                st.markdown("Este card se adapta automaticamente ao tema selecionado.")
                st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            with st.container():
                st.markdown('<div class="project-card">', unsafe_allow_html=True)
                st.markdown("#### Projeto")
                st.markdown("Design responsivo que funciona em ambos os temas.")
                st.markdown("</div>", unsafe_allow_html=True)
        
        with col3:
            with st.container():
                st.markdown('<div class="learning-card">', unsafe_allow_html=True)
                st.markdown("#### Aprendizado")
                st.markdown("Interface consistente em qualquer condição de luz.")
                st.markdown("</div>", unsafe_allow_html=True)
        
        # Renderizar sidebar
        render_sidebar()
        
    except Exception as e:
        st.error(f"Erro ao carregar o portfólio: {e}")

# --- APLICAÇÃO PRINCIPAL ---
def main():
    """Função principal que controla o fluxo da aplicação"""
    # Inicializar autenticação
    init_auth()
    
    # Inicializar session state
    initialize_session_state()
    
    # Verificar se está autenticado
    if not st.session_state.authenticated:
        render_auth_page()
    else:
        main_portfolio()

# Executar aplicação
if __name__ == "__main__":
    main()