# data.py
import streamlit as st

def get_settings():
    """Configuração inicial de estado."""
    return {"theme": "dark", "lang": "pt"}

def t(key):
    """Retorna o texto na linguagem selecionada."""
    if "settings" not in st.session_state:
        st.session_state.settings = get_settings()
    
    lang = st.session_state.settings["lang"]
    text_item = texts.get(key, {})
    if isinstance(text_item, dict) and lang in text_item:
        return text_item[lang]
    return key

def initialize_session_state():
    """Inicializa o session_state se não existir."""
    if "settings" not in st.session_state:
        st.session_state.settings = get_settings()

# --- TEXTOS MULTILÍNGUES ---
texts = {
    # Textos Gerais
    "theme_title": {"pt": "🎨 Tema", "en": "🎨 Theme", "es": "🎨 Tema"},
    "theme_dark": {"pt": "Escuro", "en": "Dark", "es": "Oscuro"},
    "theme_light": {"pt": "Claro", "en": "Light", "es": "Claro"},
    "lang_title": {"pt": "🌍 Idioma", "en": "🌍 Language", "es": "🌍 Idioma"},
    "main_title": {"pt": "Portfólio Interativo | Marcio Maker", "en": "Interactive Portfolio | Marcio Maker", "es": "Portafolio Interactivo | Marcio Maker"},
    "select_page_info": {"pt": "Selecione uma seção no menu lateral (Páginas) para começar.", "en": "Select a section in the sidebar menu (Pages) to start.", "es": "Seleccione una sección en el menú lateral (Páginas) para empezar."},
    "sidebar_footer": {"pt": "Desenvolvido em Streamlit e Python.", "en": "Developed with Streamlit and Python.", "es": "Desarrollado con Streamlit y Python."},
    
    # Textos da Seção INÍCIO
    "summary_sections": {"pt": "Este portfólio interativo apresenta meu trabalho em Design UX/UI e Desenvolvimento Full Stack, divido nas seções: Início, Sobre Mim, Serviços, Portfólio (Projetos), Aprendizagem e Contato.", "en": "This interactive portfolio showcases my work in UX/UI Design and Full Stack Development, divided into sections: Home, About Me, Services, Portfolio (Projects), Learning, and Contact.", "es": "Este portafolio interactivo presenta mi trabajo en Diseño UX/UI y Desarrollo Full Stack, dividido en secciones: Inicio, Sobre Mí, Servicios, Portafolio (Proyectos), Aprendizaje y Contacto."},
    "home_tag": {"pt": "Design UX/UI | Programação", "en": "UX/UI Design | Programming", "es": "Diseño UX/UI | Programación"},
    "home_title_1": {"pt": "UX/UI Design &", "en": "UX/UI Design &", "es": "Diseño UX/UI &"},
    "home_title_2": {"pt": "Criatividade", "en": "Creativity", "es": "Creatividad"},
    "home_title_3": {"pt": "Desenvolvimento &", "en": "Development &", "es": "Desarrollo &"},
    "home_title_4": {"pt": "Engenharia", "en": "Engineering", "es": "Ingeniería"},
    "home_subtitle": {"pt": "Criação de soluções digitais intuitivas e robustas.", "en": "Creation of intuitive and robust digital solutions.", "es": "Creación de soluciones digitales intuitivas y robustas."},
    "home_cta_1": {"pt": "Ver Projetos de Design", "en": "View Design Projects", "es": "Ver Proyectos de Diseño"},
    "home_cta_2": {"pt": "Ver Projetos de Código", "en": "View Code Projects", "es": "Ver Proyectos de Código"},
    
    # Textos da Seção SOBRE
    "about_title": {"pt": "Sobre Mim", "en": "About Me", "es": "Sobre Mí"},
    "about_heading": {"pt": "Um Designer com Mente de Engenheiro", "en": "A Designer with an Engineer's Mind", "es": "Un Diseñador con Mente de Ingeniero"},
    "about_p1": {"pt": "Meu nome é Márcio, e sou um **UX/UI Designer e Desenvolvedor Full Stack** apaixonado por transformar ideias complexas em soluções digitais elegantes e intuitivas.", "en": "My name is Márcio, and I am a **UX/UI Designer and Full Stack Developer** passionate about transforming complex ideas into elegant and intuitive digital solutions.", "es": "Mi nombre es Márcio, y soy un **Diseñador UX/UI y Desarrollador Full Stack** apasionado por transformar ideas complejas en soluciones digitales elegantes e intuitivas."},
    "about_p2": {"pt": "Com mais de 10 anos de experiência, minha abordagem combina design centrado no usuário com a robustez técnica da engenharia de software. Não apenas crio interfaces bonitas, mas também codifico o backend e o frontend para garantir uma execução perfeita.", "en": "With over 10 years of experience, my approach combines user-centered design with the technical robustness of software engineering. I not only create beautiful interfaces but also code the backend and frontend to ensure perfect execution.", "es": "Con más de 10 años de experiencia, mi enfoque combina diseño centrado en el usuario con la solidez técnica de la ingeniería de software. No solo creo interfaces bonitas, sino que también codifico el backend y el frontend para garantizar una ejecución perfecta."},
    "skills_title": {"pt": "Minhas Habilidades", "en": "My Skills", "es": "Mis Habilidades"},
    
    # Textos da Seção SERVIÇOS
    "services_title": {"pt": "Serviços", "en": "Services", "es": "Servicios"},
    "services_subtitle": {"pt": "O que eu ofereço para o seu projeto", "en": "What I offer for your project", "es": "Lo que ofrezco para tu proyecto"},
    "Design Estratégico de Produto": {"pt": "Design Estratégico de Produto", "en": "Strategic Product Design", "es": "Diseño Estratégico de Producto"},
    "Crio produtos digitais do zero, focando na jornada do usuário e na otimização de conversão. Transformo requisitos de negócio em interfaces eficazes.": {"pt": "Crio produtos digitais do zero, focando na jornada do usuário e na otimização de conversão. Transformo requisitos de negócio em interfaces eficazes.", "en": "I create digital products from scratch, focusing on the user journey and conversion optimization. I translate business requirements into effective interfaces.", "es": "Creo productos digitales desde cero, centrándome en el viaje del usuario y la optimización de la conversión. Traduzco requisitos de negocio en interfaces efectivas."},
    "Desenvolvimento Full Stack": {"pt": "Desenvolvimento Full Stack", "en": "Full Stack Development", "es": "Desarrollo Full Stack"},
    "Desenvolvimento de aplicações web completas com Python (Django/Streamlit) e JavaScript (React/Node.js), garantindo escalabilidade e performance.": {"pt": "Desenvolvimento de aplicações web completas com Python (Django/Streamlit) e JavaScript (React/Node.js), garantindo escalabilidade e performance.", "en": "Development of complete web applications with Python (Django/Streamlit) and JavaScript (React/Node.js), ensuring scalability and performance.", "es": "Desarrollo de aplicaciones web completas con Python (Django/Streamlit) y JavaScript (React/Node.js), garantizando escalabilidad y rendimiento."},
    "Otimização de Performance": {"pt": "Otimização de Performance", "en": "Performance Optimization", "es": "Optimización del Rendimiento"},
    "Análise e otimização de performance de código e design, focando em velocidade, acessibilidade e SEO para máxima eficiência.": {"pt": "Análise e otimização de performance de código e design, focando em velocidade, acessibilidade e SEO para máxima eficiência.", "en": "Analysis and optimization of code and design performance, focusing on speed, accessibility, and SEO for maximum efficiency.", "es": "Análisis y optimización del rendimiento de código y diseño, centrándose en la velocidad, accesibilidad y SEO para una máxima eficiencia."},

    # Textos da Seção PROJETOS
    "projects_title": {"pt": "Portfólio", "en": "Portfolio", "es": "Portafolio"},
    "projects_subtitle": {"pt": "Trabalhos Recentes", "en": "Recent Works", "es": "Trabajos Recientes"},
    "tab_design": {"pt": "Design UX/UI", "en": "UX/UI Design", "es": "Diseño UX/UI"},
    "tab_code": {"pt": "Desenvolvimento", "en": "Development", "es": "Desarrollo"},
    "see_more": {"pt": "Ver Detalhes", "en": "See Details", "es": "Ver Detalles"},
    "Plataforma SaaS B2B": {"pt": "Plataforma SaaS B2B", "en": "B2B SaaS Platform", "es": "Plataforma SaaS B2B"},
    "Projeto de redesign complexo para uma plataforma de análise de dados, focando na simplificação do fluxo de trabalho.": {"pt": "Projeto de redesign complexo para uma plataforma de análise de dados, focando na simplificação do fluxo de trabalho.", "en": "Complex redesign project for a data analysis platform, focusing on simplifying the workflow.", "es": "Proyecto de rediseño complejo para una plataforma de análisis de datos, centrado en simplificar el flujo de trabajo."},
    "Aplicativo Mobile Fitness": {"pt": "Aplicativo Mobile Fitness", "en": "Mobile Fitness App", "es": "Aplicación Móvil Fitness"},
    "Desenvolvimento completo da interface e experiência de usuário para um novo app de rastreamento de atividades físicas.": {"pt": "Desenvolvimento completo da interface e experiência de usuário para um novo app de rastreamento de atividades físicas.", "en": "Complete interface and user experience development for a new fitness activity tracking app.", "es": "Desarrollo completo de la interfaz y experiencia de usuario para una nueva aplicación de seguimiento de actividad física."},
    "API de Microserviços Python": {"pt": "API de Microserviços Python", "en": "Python Microservices API", "es": "API de Microservicios Python"},
    "Criação de um backend escalável com Django e PostgreSQL, utilizando arquitetura de microserviços e Docker.": {"pt": "Criação de um backend escalável com Django e PostgreSQL, utilizando arquitetura de microserviços e Docker.", "en": "Creation of a scalable backend with Django and PostgreSQL, using microservices architecture and Docker.", "es": "Creación de un backend escalable con Django y PostgreSQL, utilizando arquitectura de microservicios y Docker."},
    "Dashboard Interativo Streamlit": {"pt": "Dashboard Interativo Streamlit", "en": "Streamlit Interactive Dashboard", "es": "Panel Interactivo Streamlit"},
    "Desenvolvimento de um dashboard de visualização de dados em tempo real, utilizando Streamlit para o frontend.": {"pt": "Desenvolvimento de um dashboard de visualização de dados em tempo real, utilizando Streamlit para o frontend.", "en": "Development of a real-time data visualization dashboard, using Streamlit for the frontend.", "es": "Desarrollo de un panel de visualización de datos en tiempo real, utilizando Streamlit para el frontend."},
    
    # Textos da Seção APRENDIZAGEM
    "learning_title": {"pt": "Aprendizagem", "en": "Learning", "es": "Aprendizaje"},
    "learning_subtitle": {"pt": "Cursos e Conhecimentos", "en": "Courses & Knowledge", "es": "Cursos y Conocimientos"},
    "learning_description": {"pt": "Comprometido com aprendizado contínuo e desenvolvimento de novas habilidades.", "en": "Committed to continuous learning and development of new skills.", "es": "Comprometido con el aprendizaje continuo y desarrollo de nuevas habilidades."},
    "course_completed": {"pt": "Concluído", "en": "Completed", "es": "Completado"},
    "course_in_progress": {"pt": "Em Andamento", "en": "In Progress", "es": "En Progreso"},
    "see_certificate": {"pt": "Ver Certificado", "en": "View Certificate", "es": "Ver Certificado"},
    
    # Textos da Seção CONTATO
    "contact_title": {"pt": "Contato", "en": "Contact", "es": "Contacto"},
    "contact_subtitle": {"pt": "Fale Comigo", "en": "Get In Touch", "es": "Contacta Conmigo"},
    "contact_message": {"pt": "Envie uma mensagem direta ou use os links abaixo.", "en": "Send a direct message or use the links below.", "es": "Envía un mensaje directo o utiliza los enlaces a continuación."},
    "form_name": {"pt": "Seu Nome", "en": "Your Name", "es": "Tu Nombre"},
    "form_email": {"pt": "Seu Email", "en": "Your Email", "es": "Tu Correo"},
    "form_message": {"pt": "Mensagem", "en": "Message", "es": "Mensaje"},
    "form_submit": {"pt": "Enviar Mensagem", "en": "Send Message", "es": "Enviar Mensaje"},
    "form_success": {"pt": "Mensagem enviada com sucesso! Em breve entrarei em contato.", "en": "Message sent successfully! I will get in touch shortly.", "es": "¡Mensaje enviado con éxito! Me pondré en contacto contigo pronto."},
    "form_error": {"pt": "Por favor, preencha todos os campos.", "en": "Please fill in all fields.", "es": "Por favor, rellena todos los campos."},
    "links_title": {"pt": "Links Diretos", "en": "Direct Links", "es": "Enlaces Directos"},
    "link_email": {"pt": "Email", "en": "Email", "es": "Correo"},
    "link_linkedin": {"pt": "LinkedIn", "en": "LinkedIn", "es": "LinkedIn"},
    "link_github": {"pt": "GitHub", "en": "GitHub", "es": "GitHub"},
    "link_behance": {"pt": "Behance", "en": "Behance", "es": "Behance"},
}

# --- MAPEAMENTO DE ÍCONES PARA SKILLS ---
icon_map = {
    "Figma": "fab fa-figma",
    "Design System": "fas fa-object-group",
    "Prototipagem": "fas fa-cube",
    "UX Research": "fas fa-search",
    "Análise de Dados": "fas fa-chart-bar",
    "Sketch": "fas fa-vector-square",
    "Adobe XD": "fas fa-pen-nib",
    
    "React": "fab fa-react",
    "Streamlit": "fas fa-stream",
    "JavaScript (ES6+)": "fab fa-js-square",
    "Python": "fab fa-python",
    "HTML5": "fab fa-html5",
    "CSS3/SASS": "fab fa-css3-alt",
    "GSAP (Animações)": "fas fa-magic",
    
    "Python / Django": "fab fa-python",
    "Node.js/Express": "fab fa-node-js",
    "SQL (PostgreSQL)": "fas fa-database",
    "Docker": "fab fa-docker",
    "REST APIs": "fas fa-exchange-alt",
    "Cloud (AWS/GCP)": "fas fa-cloud",
}

# --- ESTRUTURA DE DADOS PRINCIPAL ---
data = {
    "general": {
        "page_title": "Portfólio Interativo | Marcio Maker",
        "logo_url": "https://img.icons8.com/color/48/000000/code.png",
        "logo_text": "Marcio Maker",
        "languages": ["pt", "en", "es"],
    },
    "images": {
        # Fotos Pessoais
        "about_photo": "https://i.pinimg.com/736x/67/02/7f/67027ffe40c4fd2051055d1f449d2f07.jpg",
        "profile_photo": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=face",
        
        # Home Page
        "home": {
            "image_ux": "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=800&h=500&fit=crop",
            "image_dev": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=800&h=500&fit=crop",
            "hero_background": "https://images.unsplash.com/photo-1555066931-4365d4ad806d?w=1200&h=600&fit=crop",
            "welcome_image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&h=400&fit=crop"
        },
        
        # Página Sobre
        "about": {
            "skills_banner": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1000&h=400&fit=crop",
            "experience_image": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&h=400&fit=crop",
            "education_image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600&h=400&fit=crop"
        },
        
        # Página Serviços
        "services": {
            "design_service": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=400&h=300&fit=crop",
            "development_service": "https://images.unsplash.com/photo-1555066931-4365d4ad806d?w=400&h=300&fit=crop",
            "optimization_service": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400&h=300&fit=crop",
            "services_banner": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1000&h=400&fit=crop"
        },
        
        # Página Projetos
        "projects": {
            "design": [
                {
                    "image": "https://images.unsplash.com/photo-1581291518633-83b4d4e4a68e?w=400&h=300&fit=crop",
                    "title_key": "Plataforma SaaS B2B",
                    "description_key": "Projeto de redesign complexo para uma plataforma de análise de dados, focando na simplificação do fluxo de trabalho.",
                    "tags": ["UX Design", "Figma", "Design System", "Prototipagem"]
                },
                {
                    "image": "https://images.unsplash.com/photo-1605379250365-2747190b2304?w=400&h=300&fit=crop",
                    "title_key": "Aplicativo Mobile Fitness",
                    "description_key": "Desenvolvimento completo da interface e experiência de usuário para um novo app de rastreamento de atividades físicas.",
                    "tags": ["UI Design", "Mobile", "Pesquisa UX", "Adobe XD"]
                },
            ],
            "code": [
                {
                    "image": "https://images.unsplash.com/photo-1555066931-4365d4ad806d?w=400&h=300&fit=crop",
                    "title_key": "API de Microserviços Python",
                    "description_key": "Criação de um backend escalável com Django e PostgreSQL, utilizando arquitetura de microserviços e Docker.",
                    "tags": ["Python", "Django", "Docker", "REST API"]
                },
                {
                    "image": "https://images.unsplash.com/photo-1547658719-da2b51155566?w=400&h=300&fit=crop",
                    "title_key": "Dashboard Interativo Streamlit",
                    "description_key": "Desenvolvimento de um dashboard de visualização de dados em tempo real, utilizando Streamlit para o frontend.",
                    "tags": ["Streamlit", "Python", "Data Viz", "CSS Custom"]
                },
            ],
            "projects_banner": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1000&h=400&fit=crop"
        },
        
        # Página Aprendizagem
        "learning": {
            "courses_banner": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1000&h=400&fit=crop",
            "certificates_image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600&h=400&fit=crop",
            "skills_image": "https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=600&h=400&fit=crop"
        },
        
        # Página Contato
        "contact": {
            "contact_banner": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1000&h=400&fit=crop",
            "office_image": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=600&h=400&fit=crop",
            "meeting_image": "https://images.unsplash.com/photo-1551836026-d5c88ac5c73d?w=600&h=400&fit=crop"
        },
        
        # Header e Navegação
        "navigation": {
            "inicio": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=300&h=150&fit=crop",
            "sobre": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=150&fit=crop",
            "servicos": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=300&h=150&fit=crop",
            "projetos": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=300&h=150&fit=crop",
            "aprendizagem": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=300&h=150&fit=crop",
            "contato": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=300&h=150&fit=crop"
        }
    },
    "about": {
        "skills_data": [
            {
                "category": "Design e UX",
                "tags": ["Figma", "Design System", "Prototipagem", "UX Research", "Análise de Dados", "Sketch", "Adobe XD"]
            },
            {
                "category": "Desenvolvimento (Frontend)",
                "tags": ["React", "Streamlit", "JavaScript (ES6+)", "Python", "HTML5", "CSS3/SASS", "GSAP (Animações)"]
            },
            {
                "category": "Desenvolvimento (Backend)",
                "tags": ["Python / Django", "Node.js/Express", "SQL (PostgreSQL)", "Docker", "REST APIs", "Cloud (AWS/GCP)"]
            },
        ]
    },
    "services": [
        {
            "icon": "fas fa-drafting-compass",
            "title_key": "Design Estratégico de Produto",
            "description_key": "Crio produtos digitais do zero, focando na jornada do usuário e na otimização de conversão. Transformo requisitos de negócio em interfaces eficazes.",
            "image": "design_service"
        },
        {
            "icon": "fas fa-code",
            "title_key": "Desenvolvimento Full Stack",
            "description_key": "Desenvolvimento de aplicações web completas com Python (Django/Streamlit) e JavaScript (React/Node.js), garantindo escalabilidade e performance.",
            "image": "development_service"
        },
        {
            "icon": "fas fa-tachometer-alt",
            "title_key": "Otimização de Performance",
            "description_key": "Análise e otimização de performance de código e design, focando em velocidade, acessibilidade e SEO para máxima eficiência.",
            "image": "optimization_service"
        },
    ],
    "projects": {
        "design": [
            {
                "image": "https://images.unsplash.com/photo-1581291518633-83b4d4e4a68e?w=400&h=300&fit=crop",
                "title_key": "Plataforma SaaS B2B",
                "description_key": "Projeto de redesign complexo para uma plataforma de análise de dados, focando na simplificação do fluxo de trabalho.",
                "tags": ["UX Design", "Figma", "Design System", "Prototipagem"]
            },
            {
                "image": "https://images.unsplash.com/photo-1605379250365-2747190b2304?w=400&h=300&fit=crop",
                "title_key": "Aplicativo Mobile Fitness",
                "description_key": "Desenvolvimento completo da interface e experiência de usuário para um novo app de rastreamento de atividades físicas.",
                "tags": ["UI Design", "Mobile", "Pesquisa UX", "Adobe XD"]
            },
        ],
        "code": [
            {
                "image": "https://images.unsplash.com/photo-1555066931-4365d4ad806d?w=400&h=300&fit=crop",
                "title_key": "API de Microserviços Python",
                "description_key": "Criação de um backend escalável com Django e PostgreSQL, utilizando arquitetura de microserviços e Docker.",
                "tags": ["Python", "Django", "Docker", "REST API"]
            },
            {
                "image": "https://images.unsplash.com/photo-1547658719-da2b51155566?w=400&h=300&fit=crop",
                "title_key": "Dashboard Interativo Streamlit",
                "description_key": "Desenvolvimento de um dashboard de visualização de dados em tempo real, utilizando Streamlit para o frontend.",
                "tags": ["Streamlit", "Python", "Data Viz", "CSS Custom"]
            },
        ]
    },
    # SEÇÃO APRENDIZAGEM
    "learning": {
        "courses": [
            {
                "title": "UX Design Avançado",
                "platform": "Coursera",
                "status": "completed",
                "duration": "40h",
                "certificate_url": "https://example.com/certificate1",
                "skills": ["UX Research", "Prototipagem", "Figma"],
                "image": "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=300&h=200&fit=crop"
            },
            {
                "title": "Python para Data Science",
                "platform": "Alura",
                "status": "completed", 
                "duration": "60h",
                "certificate_url": "https://example.com/certificate2",
                "skills": ["Python", "Pandas", "Data Analysis"],
                "image": "https://images.unsplash.com/photo-1526379879527-8559ecfcaec0?w=300&h=200&fit=crop"
            },
            {
                "title": "React e TypeScript",
                "platform": "Udemy",
                "status": "in_progress",
                "duration": "45h",
                "certificate_url": None,
                "skills": ["React", "TypeScript", "Frontend"],
                "image": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=300&h=200&fit=crop"
            },
            {
                "title": "Docker e Kubernetes",
                "platform": "Pluralsight",
                "status": "in_progress",
                "duration": "35h",
                "certificate_url": None,
                "skills": ["Docker", "Kubernetes", "DevOps"],
                "image": "https://images.unsplash.com/photo-1627398242454-45a1465c2479?w=300&h=200&fit=crop"
            }
        ]
    },
    "contact": {
        "email": "marcio.maker@example.com",
        "linkedin": {"url": "https://linkedin.com/in/marciomaker", "display": "linkedin.com/in/marciomaker"},
        "github": {"url": "https://github.com/marcio-maker", "display": "github.com/marcio-maker"},
        "behance": {"url": "https://www.behance.net/0faa6a9e", "display": "behance.net/0faa6a9e"},
    }
}

# Mescla os textos dos dados específicos (title_key, description_key) no dicionário 'texts'
def populate_texts_from_data():
    for section in data["services"]:
        if section["title_key"] not in texts:
            texts[section["title_key"]] = {"pt": section["title_key"], "en": section["title_key"], "es": section["title_key"]}
        if section["description_key"] not in texts:
            texts[section["description_key"]] = {"pt": section["description_key"], "en": section["description_key"], "es": section["description_key"]}
            
    for project_list in data["projects"].values():
        for project in project_list:
            if project["title_key"] not in texts:
                texts[project["title_key"]] = {"pt": project["title_key"], "en": project["title_key"], "es": project["title_key"]}
            if project["description_key"] not in texts:
                texts[project["description_key"]] = {"pt": project["description_key"], "en": project["description_key"], "es": project["description_key"]}

populate_texts_from_data()