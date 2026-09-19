# -*- coding: utf-8 -*-
import os
import polib

LANGUAGES = ['es', 'en', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'zh_Hans', 'ar', 'ru', 'hi']

LANDING_TRANSLATIONS = {
    "100% Gratuito para candidatos": {
        "es": "100% Gratuito para candidatos", "en": "100% Free for candidates", "pt": "100% Gratuito para candidatos",
        "fr": "100% Gratuit pour les candidats", "de": "100% Kostenlos für Kandidaten", "it": "100% Gratuito per i candidati",
        "ja": "候補者は100%無料", "ko": "후보자 100% 무료", "zh_Hans": "求职者100%免费",
        "ar": "مجاني 100٪ للمرشحين", "ru": "100% бесплатно для кандидатов", "hi": "उम्मीदवारों के लिए 100% मुफ़्त"
    },
    "Afinidad con vacantes técnicas": {
        "es": "Afinidad con vacantes técnicas", "en": "Match score with technical vacancies", "pt": "Afinidade com vagas técnicas",
        "fr": "Affinité avec les postes techniques", "de": "Passgenauigkeit für technische Stellen", "it": "Affinità con le posizioni tecniche",
        "ja": "技術職とのマッチ度", "ko": "기술 직무 적합도", "zh_Hans": "与技术职位的契合度",
        "ar": "درجة التوافق مع الشواغر التقنية", "ru": "Соответствие техническим вакансиям", "hi": "तकनीकी रिक्तियों के साथ मिलान स्कोर"
    },
    "Alcance internacional": {
        "es": "Alcance internacional", "en": "International reach", "pt": "Alcance internacional",
        "fr": "Portée internationale", "de": "Internationale Reichweite", "it": "Portata internazionale",
        "ja": "国際的なリーチ", "ko": "국제적 도달 범위", "zh_Hans": "全球影响力",
        "ar": "وصول دولي", "ru": "Международный охват", "hi": "अंतर्राष्ट्रीय पहुंच"
    },
    "Arquitectura de microservicios y liderazgo de equipo técnico.": {
        "es": "Arquitectura de microservicios y liderazgo de equipo técnico.",
        "en": "Microservices architecture and technical team leadership.",
        "pt": "Arquitetura de microsserviços e liderança de equipe técnica.",
        "fr": "Architecture de microservices et direction d'équipe technique.",
        "de": "Microservices-Architektur und technische Teamleitung.",
        "it": "Architettura a microservizi e leadership del team tecnico.",
        "ja": "マイクロサービスアーキテクチャと技術チームのリーダーシップ。",
        "ko": "마이크로서비스 아키텍처 및 기술 팀 리더십.",
        "zh_Hans": "微服务架构与技术团队领导。",
        "ar": "هندسة الخدمات المصغرة وقيادة الفريق التقني.",
        "ru": "Микросервисная архитектура и руководство технической командой.",
        "hi": "माइक्रोसर्विस आर्किटेक्चर और तकनीकी टीम नेतृत्व।"
    },
    "Backend Python": {
        "es": "Backend Python", "en": "Python Backend", "pt": "Backend Python",
        "fr": "Backend Python", "de": "Python-Backend", "it": "Backend Python",
        "ja": "Python バックエンド", "ko": "Python 백엔드", "zh_Hans": "Python 后端",
        "ar": "باك إند بايثون", "ru": "Бэкенд на Python", "hi": "पायथन बैकएंड"
    },
    "Búsqueda y filtrado": {
        "es": "Búsqueda y filtrado", "en": "Search and filtering", "pt": "Busca e filtragem",
        "fr": "Recherche et filtrage", "de": "Suche und Filterung", "it": "Ricerca e filtri",
        "ja": "検索とフィルタリング", "ko": "검색 및 필터링", "zh_Hans": "搜索与筛选",
        "ar": "البحث والتصفية", "ru": "Поиск и фильтрация", "hi": "खोज और फ़िल्टरिंग"
    },
    "CV Tradicional (PDF)": {
        "es": "CV Tradicional (PDF)", "en": "Traditional CV (PDF)", "pt": "CV Tradicional (PDF)",
        "fr": "CV Traditionnel (PDF)", "de": "Traditioneller Lebenslauf (PDF)", "it": "CV Tradizionale (PDF)",
        "ja": "従来の履歴書 (PDF)", "ko": "전통적인 이력서 (PDF)", "zh_Hans": "传统简历 (PDF)",
        "ar": "السيرة الذاتية التقليدية (PDF)", "ru": "Традиционное резюме (PDF)", "hi": "पारंपरिक सीवी (PDF)"
    },
    "CV Tradicional en PDF": {
        "es": "CV Tradicional en PDF", "en": "Traditional PDF Resume", "pt": "Currículo Tradicional em PDF",
        "fr": "CV Traditionnel en PDF", "de": "Traditioneller PDF-Lebenslauf", "it": "CV Tradizionale in PDF",
        "ja": "従来のPDF履歴書", "ko": "전통적인 PDF 이력서", "zh_Hans": "传统 PDF 简历",
        "ar": "السيرة الذاتية التقليدية بصيغة PDF", "ru": "Традиционное резюме в формате PDF", "hi": "पारंपरिक PDF बायोडाटा"
    },
    "Cero métricas de visualización ni interés de empresas": {
        "es": "Cero métricas de visualización ni interés de empresas",
        "en": "Zero view metrics and no insight into employer interest",
        "pt": "Zero métricas de visualização ou interesse das empresas",
        "fr": "Zéro métrique de vue et aucun suivi de l'intérêt des entreprises",
        "de": "Keine Aufruf-Metriken oder Einblick in das Interesse von Unternehmen",
        "it": "Zero metriche di visualizzazione e nessun riscontro d'interesse aziendale",
        "ja": "閲覧指標ゼロ、企業からの関心度も不明",
        "ko": "조회수 지표 제로 및 기업 관심도 확인 불가",
        "zh_Hans": "零浏览数据，无法得知企业关注度",
        "ar": "صفر من مؤشرات المشاهدة وبدون معرفة باهتمام الشركات",
        "ru": "Ноль метрик просмотров и интереса компаний",
        "hi": "शून्य व्यू मेट्रिक्स और कंपनियों की रुचि की कोई जानकारी नहीं"
    },
    "Cero visibilidad": {
        "es": "Cero visibilidad", "en": "Zero visibility", "pt": "Zero visibilidade",
        "fr": "Zéro visibilité", "de": "Keine Sichtbarkeit", "it": "Zero visibilità",
        "ja": "視認性ゼロ", "ko": "가시성 제로", "zh_Hans": "零可见度",
        "ar": "انعدام الرؤية", "ru": "Нулевая видимость", "hi": "शून्य दृश्यता"
    },
    "Compara la experiencia": {
        "es": "Compara la experiencia", "en": "Compare the experience", "pt": "Compare a experiência",
        "fr": "Comparez l'expérience", "de": "Vergleichen Sie die Erfahrung", "it": "Confronta l'esperienza",
        "ja": "体験を比較する", "ko": "경험 비교하기", "zh_Hans": "对比使用体验",
        "ar": "قارن التجربة", "ru": "Сравните опыт", "hi": "अनुभव की तुलना करें"
    },
    "Contactar directamente": {
        "es": "Contactar directamente", "en": "Contact directly", "pt": "Entrar em contato diretamente",
        "fr": "Contacter directement", "de": "Direkt kontaktieren", "it": "Contatta direttamente",
        "ja": "直接連絡する", "ko": "직접 연락하기", "zh_Hans": "直接联系",
        "ar": "تواصل مباشرة", "ru": "Связаться напрямую", "hi": "सीधे संपर्क करें"
    },
    "Contacto directo": {
        "es": "Contacto directo", "en": "Direct contact", "pt": "Contato direto",
        "fr": "Contact direct", "de": "Direkter Kontakt", "it": "Contatto diretto",
        "ja": "ダイレクトコンタクト", "ko": "직접 문의", "zh_Hans": "直接联络",
        "ar": "اتصال مباشر", "ru": "Прямой контакт", "hi": "प्रत्यक्ष संपर्क"
    },
    "Contacto directo con reclutadores": {
        "es": "Contacto directo con reclutadores", "en": "Direct contact with recruiters", "pt": "Contato direto com recrutadores",
        "fr": "Contact direct avec les recruteurs", "de": "Direkter Kontakt zu Recruitern", "it": "Contatto diretto con i recruiter",
        "ja": "採用担当者との直接連絡", "ko": "채용 담당자와의 직접 연락", "zh_Hans": "与招聘人员直接沟通",
        "ar": "تواصل مباشر مع مسؤولي التوظيف", "ru": "Прямой контакт с рекрутерами", "hi": "भर्तीकर्ताओं से सीधा संपर्क"
    },
    "Contacto directo sin intermediarios": {
        "es": "Contacto directo sin intermediarios", "en": "Direct contact without middlemen", "pt": "Contato direto sem intermediários",
        "fr": "Contact direct sans intermédiaires", "de": "Direkter Kontakt ohne Zwischenhändler", "it": "Contatto diretto senza intermediari",
        "ja": "仲介者抜きの直接連絡", "ko": "중개자 없는 직접 연락", "zh_Hans": "无中介直接联络",
        "ar": "اتصال مباشر بدون وسطاء", "ru": "Прямой контакт без посредников", "hi": "बिचौलियों के बिना सीधा संपर्क"
    },
    "Contacto directo y seguro vía email": {
        "es": "Contacto directo y seguro vía email", "en": "Direct and secure contact via email", "pt": "Contato direto e seguro por e-mail",
        "fr": "Contact direct et sécurisé par e-mail", "de": "Direkter und sicherer Kontakt per E-Mail", "it": "Contatto diretto e sicuro via email",
        "ja": "安全なメールによる直接コンタクト", "ko": "이메일을 통한 안전하고 직접적인 연락", "zh_Hans": "通过邮件安全直接联络",
        "ar": "اتصال مباشر وآمن عبر البريد الإلكتروني", "ru": "Прямой и безопасный контакт по эл. почте", "hi": "ईमेल द्वारा सीधा और सुरक्षित संपर्क"
    },
    "Contacto y respuesta": {
        "es": "Contacto y respuesta", "en": "Contact and response", "pt": "Contato e resposta",
        "fr": "Contact et réponse", "de": "Kontakt und Rückmeldung", "it": "Contatto e risposta",
        "ja": "連絡とレスポンス", "ko": "연락 및 응답", "zh_Hans": "联系与响应",
        "ar": "الاتصال والاستجابة", "ru": "Контакт и отклик", "hi": "संपर्क और प्रतिक्रिया"
    },
    "Crea tu perfil en minutos, comparte tu enlace personalizado y haz visible tu potencial ante las mejores oportunidades.": {
        "es": "Crea tu perfil en minutos, comparte tu enlace personalizado y haz visible tu potencial ante las mejores oportunidades.",
        "en": "Create your profile in minutes, share your custom link, and make your potential visible to top opportunities.",
        "pt": "Crie seu perfil em minutos, compartilhe seu link personalizado e torne seu potencial visível para as melhores oportunidades.",
        "fr": "Créez votre profil en quelques minutes, partagez votre lien personnalisé et rendez votre potentiel visible aux meilleures opportunités.",
        "de": "Erstellen Sie Ihr Profil in wenigen Minuten, teilen Sie Ihren persönlichen Link und machen Sie Ihr Potenzial für beste Chancen sichtbar.",
        "it": "Crea il tuo profilo in pochi minuti, condividi il tuo link personalizzato e rendi visibile il tuo potenziale alle migliori opportunità.",
        "ja": "数分でプロフィールを作成し、カスタムリンクを共有して、最高の一歩へとポテンシャルを発揮しましょう。",
        "ko": "몇 분 만에 프로필을 만들고, 맞춤 링크를 공유하여 최고의 기회에 당신의 잠재력을 드러내세요.",
        "zh_Hans": "几分钟内创建您的个人资料，分享专属链接，向顶尖机遇展现您的全部潜力。",
        "ar": "أنشئ ملفك في دقائق، وشارك رابطك المخصص، واجعل إمكانياتك مرئية لأفضل الفرص.",
        "ru": "Создайте профиль за пару минут, делитесь персональной ссылкой и раскройте свой потенциал для лучших возможностей.",
        "hi": "मिनटों में अपनी प्रोफ़ाइल बनाएं, अपना कस्टम लिंक साझा करें और सर्वोत्तम अवसरों के सामने अपनी क्षमता को दृश्यमान बनाएं।"
    },
    "Crear mi cuenta gratuita": {
        "es": "Crear mi cuenta gratuita", "en": "Create my free account", "pt": "Criar minha conta gratuita",
        "fr": "Créer mon compte gratuit", "de": "Mein kostenloses Konto erstellen", "it": "Crea il mio account gratuito",
        "ja": "無料アカウントを作成", "ko": "무료 계정 생성", "zh_Hans": "创建我的免费账户",
        "ar": "إنشاء حسابي المجاني", "ru": "Создать бесплатный аккаунт", "hi": "मेरा मुफ़्त खाता बनाएं"
    },
    "Crear mi perfil interactivo": {
        "es": "Crear mi perfil interactivo", "en": "Create my interactive profile", "pt": "Criar meu perfil interativo",
        "fr": "Créer mon profil interactif", "de": "Mein interaktives Profil erstellen", "it": "Crea il mio profilo interattivo",
        "ja": "インタラクティブなプロフィールを作成", "ko": "대화형 프로필 만들기", "zh_Hans": "创建我的互动主页",
        "ar": "إنشاء ملفي التفاعلي", "ru": "Создать интерактивный профиль", "hi": "मेरी इंटरैक्टिव प्रोफ़ाइल बनाएं"
    },
    "Criterio": {
        "es": "Criterio", "en": "Criteria", "pt": "Critério",
        "fr": "Critère", "de": "Kriterium", "it": "Criterio",
        "ja": "評価項目", "ko": "기준", "zh_Hans": "评估维度",
        "ar": "المعيار", "ru": "Критерий", "hi": "मानदंड"
    },
    "Código fuente": {
        "es": "Código fuente", "en": "Source code", "pt": "Código-fonte",
        "fr": "Code source", "de": "Quellcode", "it": "Codice sorgente",
        "ja": "ソースコード", "ko": "소스 코드", "zh_Hans": "源码仓库",
        "ar": "الشفرة المصدرية", "ru": "Исходный код", "hi": "स्रोत कोड"
    },
    "Data & IA": {
        "es": "Data & IA", "en": "Data & AI", "pt": "Dados & IA",
        "fr": "Données & IA", "de": "Daten & KI", "it": "Dati & IA",
        "ja": "データ & AI", "ko": "데이터 & AI", "zh_Hans": "数据与人工智能",
        "ar": "البيانات والذكاء الاصطناعي", "ru": "Данные и ИИ", "hi": "डेटा और एआई"
    },
    "Demostración de habilidades": {
        "es": "Demostración de habilidades", "en": "Skills demonstration", "pt": "Demonstração de habilidades",
        "fr": "Démonstration des compétences", "de": "Nachweis von Fähigkeiten", "it": "Dimostrazione delle competenze",
        "ja": "スキルの実証", "ko": "기술 입증", "zh_Hans": "技能展示与验证",
        "ar": "إثبات المهارات", "ru": "Демонстрация навыков", "hi": "कौशल प्रदर्शन"
    },
    "Desactualizado el mismo día en que se descarga": {
        "es": "Desactualizado el mismo día en que se descarga",
        "en": "Outdated the very day it is downloaded",
        "pt": "Desatualizado no mesmo dia em que é baixado",
        "fr": "Obsolète le jour même de son téléchargement",
        "de": "Bereits am Tag des Downloads veraltet",
        "it": "Obsoleto lo stesso giorno in cui viene scaricato",
        "ja": "ダウンロードしたその日に時代遅れ",
        "ko": "다운로드하는 바로 그날 구식이 됨",
        "zh_Hans": "下载当天即告过时",
        "ar": "قديم وغير محدث في نفس يوم تحميله",
        "ru": "Устаревает в тот же день, когда скачан",
        "hi": "डाउनलोड होते ही पुराना हो जाता है"
    },
    "Desarrollo Web": {
        "es": "Desarrollo Web", "en": "Web Development", "pt": "Desenvolvimento Web",
        "fr": "Développement Web", "de": "Webentwicklung", "it": "Sviluppo Web",
        "ja": "ウェブ開発", "ko": "웹 개발", "zh_Hans": "Web 开发",
        "ar": "تطوير الويب", "ru": "Веб-разработка", "hi": "वेब विकास"
    },
    "Descargar resumen": {
        "es": "Descargar resumen", "en": "Download summary", "pt": "Baixar resumo",
        "fr": "Télécharger le résumé", "de": "Zusammenfassung herunterladen", "it": "Scarica riepilogo",
        "ja": "要約をダウンロード", "ko": "요약본 다운로드", "zh_Hans": "下载概览",
        "ar": "تحميل الملخص", "ru": "Скачать резюме", "hi": "सारांश डाउनलोड करें"
    },
    "Dinámico, responsivo y enriquecido con medios": {
        "es": "Dinámico, responsivo y enriquecido con medios",
        "en": "Dynamic, responsive, and media-rich",
        "pt": "Dinâmico, responsivo e rico em mídia",
        "fr": "Dynamique, réactif et enrichi de médias",
        "de": "Dynamisch, responsiv und medienreich",
        "it": "Dinamico, reattivo e arricchito di contenuti multimediali",
        "ja": "動的でレスポンシブ、豊かなメディア表現",
        "ko": "동적이고 반응형이며 다양한 미디어 지원",
        "zh_Hans": "动态、响应式且富有富媒体展现",
        "ar": "ديناميكي، متجاوب، وغني بالوسائط",
        "ru": "Динамичный, адаптивный и богатый медиа",
        "hi": "गतिशील, उत्तरदायी और मीडिया से समृद्ध"
    },
    "Diseñado para hacer destacar tu valor real en el mercado": {
        "es": "Diseñado para hacer destacar tu valor real en el mercado",
        "en": "Designed to highlight your true market value",
        "pt": "Projetado para destacar seu verdadeiro valor no mercado",
        "fr": "Conçu pour mettre en valeur votre véritable valeur marchande",
        "de": "Entwickelt, um Ihren wahren Marktwert hervorzuheben",
        "it": "Progettato per far risaltare il tuo vero valore sul mercato",
        "ja": "あなたの真の市場価値を際立たせる設計",
        "ko": "시장에서 당신의 실제 가치를 돋보이게 하도록 설계되었습니다",
        "zh_Hans": "专为凸显您在就业市场的真实价值而设计",
        "ar": "مصمم لإبراز قيمتك الحقيقية في السوق",
        "ru": "Создан, чтобы подчеркнуть вашу реальную ценность на рынке",
        "hi": "बाजार में आपके वास्तविक मूल्य को उजागर करने के लिए डिज़ाइन किया गया"
    },
    "Diseño & UX": {
        "es": "Diseño & UX", "en": "Design & UX", "pt": "Design & UX",
        "fr": "Design & UX", "de": "Design & UX", "it": "Design & UX",
        "ja": "デザイン & UX", "ko": "디자인 & UX", "zh_Hans": "设计与用户体验",
        "ar": "التصميم وتجربة المستخدم", "ru": "Дизайн и UX", "hi": "डिज़ाइन और यूएक्स"
    },
    "Disponible para nuevas ofertas": {
        "es": "Disponible para nuevas ofertas", "en": "Open to new opportunities", "pt": "Disponível para novas oportunidades",
        "fr": "À l'écoute de nouvelles opportunités", "de": "Offen für neue Angebote", "it": "Disponibile per nuove offerte",
        "ja": "新しいオファーを受付中", "ko": "새로운 기회에 열려 있음", "zh_Hans": "求职中 / 开放新机会",
        "ar": "متاح لعروض جديدة", "ru": "Открыт для предложений", "hi": "नए अवसरों के लिए उपलब्ध"
    },
    "Doble Ecosistema Conectado": {
        "es": "Doble Ecosistema Conectado", "en": "Dual Connected Ecosystem", "pt": "Ecossistema Duplo Conectado",
        "fr": "Double Écosystème Connecté", "de": "Duales Vernetztes Ökosystem", "it": "Doppio Ecosistema Connesso",
        "ja": "相互接続されたデュアルエコシステム", "ko": "연결된 듀얼 에코시스템", "zh_Hans": "双向联通生态",
        "ar": "نظام بيئي مزدوج متصل", "ru": "Двойная связанная экосистема", "hi": "जुड़ा हुआ दोहरा इकोसिस्टम"
    },
    "Documento estático de 2 páginas": {
        "es": "Documento estático de 2 páginas", "en": "Static 2-page document", "pt": "Documento estático de 2 páginas",
        "fr": "Document statique de 2 pages", "de": "Statisches 2-Seiten-Dokument", "it": "Documento statico di 2 pagine",
        "ja": "静的な2ページのドキュメント", "ko": "정적인 2페이지 문서", "zh_Hans": "死板的2页纸质文档",
        "ar": "وثيقة ثابتة من صفحتين", "ru": "Статичный документ на 2 страницы", "hi": "स्थैतिक 2-पृष्ठ दस्तावेज़"
    },
    "Dos tablones sincronizados: profesionales mostrando su talento y reclutadores publicando oportunidades con total transparencia.": {
        "es": "Dos tablones sincronizados: profesionales mostrando su talento y reclutadores publicando oportunidades con total transparencia.",
        "en": "Two synchronized walls: professionals showcasing their talent and recruiters posting opportunities with total transparency.",
        "pt": "Dois murais sincronizados: profissionais mostrando seu talento e recrutadores publicando oportunidades com total transparência.",
        "fr": "Deux tableaux synchronisés : des professionnels montrant leur talent et des recruteurs publiant des opportunités en toute transparence.",
        "de": "Zwei synchronisierte Boards: Fachkräfte präsentieren ihr Talent und Recruiter veröffentlichen Stellen mit voller Transparenz.",
        "it": "Due bacheche sincronizzate: professionisti che mostrano il loro talento e recruiter che pubblicano opportunità con totale trasparenza.",
        "ja": "同期された2つの掲示板：才能を披露するプロフェッショナルと、高い透明性で求人を掲載する採用担当者。",
        "ko": "두 개의 동기화된 보드: 자신의 재능을 선보이는 전문가들과 완전한 투명성으로 기회를 게시하는 채용 담당자.",
        "zh_Hans": "双重同步大厅：专业人才展示卓越能力，招聘方以极致透明度发布优质职位。",
        "ar": "لوحتان متزامنتان: محترفون يعرضون مواهبهم ومسؤولو توظيف ينشرون الفرص بشفافية تامة.",
        "ru": "Две синхронизированные доски: таланты демонстрируют навыки, а рекрутеры публикуют предложения с полной прозрачностью.",
        "hi": "दो समन्वयित बोर्ड: पेशेवर अपनी प्रतिभा का प्रदर्शन करते हैं और भर्तीकर्ता पूर्ण पारदर्शिता के साथ अवसर पोस्ट करते हैं।"
    },
    "El CV tradicional en PDF ha muerto. Construye un perfil dinámico con taxonomía en 4 niveles, portafolio multimedia y contacto directo con reclutadores globales.": {
        "es": "El CV tradicional en PDF ha muerto. Construye un perfil dinámico con taxonomía en 4 niveles, portafolio multimedia y contacto directo con reclutadores globales.",
        "en": "The traditional PDF resume is dead. Build a dynamic profile with 4-level taxonomy, multimedia portfolio, and direct contact with global recruiters.",
        "pt": "O currículo tradicional em PDF morreu. Construa um perfil dinâmico com taxonomia em 4 níveis, portfólio multimídia e contato direto com recrutadores globais.",
        "fr": "Le CV traditionnel en PDF est mort. Créez un profil dynamique avec une taxonomie en 4 niveaux, un portfolio multimédia et un contact direct avec les recruteurs du monde entier.",
        "de": "Der traditionelle PDF-Lebenslauf ist tot. Bauen Sie ein dynamisches Profil mit 4-stufiger Taxonomie, Multimedia-Portfolio und direktem Kontakt zu weltweiten Recruitern.",
        "it": "Il tradizionale CV in PDF è superato. Costruisci un profilo dinamico con tassonomia a 4 livelli, portfolio multimediale e contatto diretto con i recruiter globali.",
        "ja": "従来のPDF履歴書の時代は終わりました。4段階の分類、マルチメディアポートフォリオ、グローバル採用担当者との直接コンタクトを備えた動的プロフィールを構築しましょう。",
        "ko": "전통적인 PDF 이력서는 끝났습니다. 4단계 분류 체계, 멀티미디어 포트폴리오, 글로벌 채용 담당자와의 직접 소통이 가능한 동적 프로필을 만드세요.",
        "zh_Hans": "传统的 PDF 简历已成过往。构建具备4级精准分类、富媒体作品集并能与全球招聘官直接联络的动态主页。",
        "ar": "انتهى عهد السيرة الذاتية التقليدية بتنسيق PDF. ابنِ ملفًا شخصيًا ديناميكيًا بتصنيف من 4 مستويات ومعرض وسائط واتصال مباشر مع مسؤولي التوظيف حول العالم.",
        "ru": "Традиционное резюме в PDF устарело. Создайте динамичный профиль с 4-уровневой таксономией, мультимедийным портфолио и прямым контактом с рекрутерами со всего мира.",
        "hi": "पारंपरिक PDF बायोडाटा अब पुराना हो चुका है। 4-स्तरीय वर्गीकरण, मल्टीमीडिया पोर्टफोलियो और वैश्विक भर्तीकर्ताओं से सीधे संपर्क के साथ एक गतिशील प्रोफ़ाइल बनाएं।"
    },
    "El contraste entre el viejo modelo y la nueva era profesional": {
        "es": "El contraste entre el viejo modelo y la nueva era profesional",
        "en": "The contrast between the old model and the new professional era",
        "pt": "O contraste entre o modelo antigo e a nova era profissional",
        "fr": "Le contraste entre l'ancien modèle et la nouvelle ère professionnelle",
        "de": "Der Kontrast zwischen dem alten Modell und der neuen Arbeitswelt",
        "it": "Il contrasto tra il vecchio modello e la nuova era professionale",
        "ja": "旧モデルと新たなプロフェッショナル時代との鮮明な対比",
        "ko": "기존 모델과 새로운 전문직 시대 간의 극명한 대비",
        "zh_Hans": "旧模式与新职场时代的鲜明对比",
        "ar": "التباين بين النموذج القديم والعصر المهني الجديد",
        "ru": "Контраст между старой моделью и новой профессиональной эрой"
    },
    "Enlaces a proyectos y demos que nadie abre": {
        "es": "Enlaces a proyectos y demos que nadie abre",
        "en": "Project and demo links that no one opens",
        "pt": "Links de projetos e demos que ninguém abre",
        "fr": "Des liens vers des projets et des démos que personne n'ouvre",
        "de": "Projekt- und Demo-Links, die niemand anklickt",
        "it": "Link a progetti e demo che nessuno apre",
        "ja": "誰もクリックしないプロジェクトやデモのリンク",
        "ko": "아무도 열어보지 않는 프로젝트 및 데모 링크",
        "zh_Hans": "无人点击的项目和演示链接",
        "ar": "روابط مشاريع وعروض لا يفتحها أحد",
        "ru": "Ссылки на проекты и демо, которые никто не открывает",
        "hi": "परियोजना और डेमो लिंक जिन्हें कोई नहीं खोलता"
    },
    "Enlaces muertos": {
        "es": "Enlaces muertos", "en": "Dead links", "pt": "Links mortos",
        "fr": "Liens morts", "de": "Tote Links", "it": "Link non funzionanti",
        "ja": "機能しないリンク", "ko": "끊어진 링크", "zh_Hans": "失效无用链接",
        "ar": "روابط معطلة", "ru": "Мертвые ссылки", "hi": "मृत लिंक"
    },
    "Enterrado en la bandeja": {
        "es": "Enterrado en la bandeja", "en": "Buried in the inbox", "pt": "Enterrado na caixa de entrada",
        "fr": "Enterré dans la boîte de réception", "de": "Im Posteingang vergraben", "it": "Sepolto nella casella di posta",
        "ja": "受信トレイに埋もれる", "ko": "받은편지함에 파묻힘", "zh_Hans": "淹没在收件箱中",
        "ar": "مدفون في صندوق الوارد", "ru": "Погребено во входящих", "hi": "इनबॉक्स में दबा हुआ"
    },
    "Enterrado en un buzón junto a cientos de archivos idénticos": {
        "es": "Enterrado en un buzón junto a cientos de archivos idénticos",
        "en": "Buried in an inbox alongside hundreds of identical files",
        "pt": "Enterrado em uma caixa de entrada junto a centenas de arquivos idênticos",
        "fr": "Enterré dans une boîte de réception avec des centaines de fichiers identiques",
        "de": "Vergraben in einem Postfach neben Hunderten identischer Dateien",
        "it": "Sepolto in una casella di posta insieme a centinaia di file identici",
        "ja": "何百もの同じようなファイルと一緒に受信トレイに埋もれる",
        "ko": "수백 개의 동일한 파일과 함께 받은편지함에 묻힘",
        "zh_Hans": "与成百上千份千篇一律的文件一同沉睡在邮箱里",
        "ar": "مدفون في صندوق البريد بجانب مئات الملفات المتطابقة",
        "ru": "Погребено в почтовом ящике среди сотен одинаковых файлов",
        "hi": "सैकड़ों समान फ़ाइलों के साथ इनबॉक्स में दबा हुआ"
    },
    "Español (Nativo), Inglés (C1 Avanzado)": {
        "es": "Español (Nativo), Inglés (C1 Avanzado)",
        "en": "Spanish (Native), English (C1 Advanced)",
        "pt": "Espanhol (Nativo), Inglês (C1 Avançado)",
        "fr": "Espagnol (Natif), Anglais (C1 Avancé)",
        "de": "Spanisch (Muttersprache), Englisch (C1 Fortgeschritten)",
        "it": "Spagnolo (Madrelingua), Inglese (C1 Avanzato)",
        "ja": "スペイン語 (ネイティブ), 英語 (C1 上級)",
        "ko": "스페인어 (원어민), 영어 (C1 고급)",
        "zh_Hans": "西班牙语 (母语), 英语 (C1 高级)",
        "ar": "الإسبانية (لغة أم)، الإنجليزية (متقدم C1)",
        "ru": "Испанский (родной), Английский (C1 продвинутый)",
        "hi": "स्पैनिश (मूल), अंग्रेज़ी (C1 उन्नत)"
    },
    "Especialidades y tecnologías destacadas en este sector:": {
        "es": "Especialidades y tecnologías destacadas en este sector:",
        "en": "Featured specialties and technologies in this sector:",
        "pt": "Especialidades e tecnologias em destaque neste setor:",
        "fr": "Spécialités et technologies mises en avant dans ce secteur :",
        "de": "Wichtige Fachgebiete und Technologien in diesem Bereich:",
        "it": "Specializzazioni e tecnologie in evidenza in questo settore:",
        "ja": "この分野で注目の専門職とテクノロジー:",
        "ko": "이 분야의 주요 전문 분야 및 기술:",
        "zh_Hans": "该行业的热门专长与关键技术：",
        "ar": "التخصصات والتقنيات البارزة في هذا القطاع:",
        "ru": "Популярные специализации и технологии в этом секторе:",
        "hi": "इस क्षेत्र में प्रमुख विशेषताएं और प्रौद्योगिकियां:"
    },
    "Experiencia reciente": {
        "es": "Experiencia reciente", "en": "Recent experience", "pt": "Experiência recente",
        "fr": "Expérience récente", "de": "Aktuelle Erfahrung", "it": "Esperienza recente",
        "ja": "最近の経歴", "ko": "최근 경력", "zh_Hans": "近期经历",
        "ar": "الخبرة الأخيرة", "ru": "Недавний опыт", "hi": "हाल का अनुभव"
    },
    "Explorador de Talento en Tiempo Real": {
        "es": "Explorador de Talento en Tiempo Real", "en": "Real-Time Talent Explorer", "pt": "Explorador de Talentos em Tempo Real",
        "fr": "Explorateur de Talents en Temps Réel", "de": "Echtzeit-Talent-Explorer", "it": "Esploratore di Talenti in Tempo Reale",
        "ja": "リアルタイムタレントエクスプローラー", "ko": "실시간 인재 탐색기", "zh_Hans": "实时人才探索器",
        "ar": "مستكشف المواهب بالوقت الفعلي", "ru": "Поиск талантов в реальном времени", "hi": "वास्तविक समय प्रतिभा खोजकर्ता"
    },
    "Explorar tablón de empresas": {
        "es": "Explorar tablón de empresas", "en": "Explore company wall", "pt": "Explorar mural de empresas",
        "fr": "Explorer le tableau des entreprises", "de": "Unternehmens-Board erkunden", "it": "Esplora bacheca aziende",
        "ja": "企業掲示板を見る", "ko": "기업 게시판 둘러보기", "zh_Hans": "浏览企业招聘大厅",
        "ar": "استكشف لوحة الشركات", "ru": "Смотреть доску компаний", "hi": "कंपनी बोर्ड देखें"
    },
    "Explorar tablón de talento": {
        "es": "Explorar tablón de talento", "en": "Explore talent wall", "pt": "Explorar mural de talentos",
        "fr": "Explorer le tableau des talents", "de": "Talent-Board erkunden", "it": "Esplora bacheca talenti",
        "ja": "タレント掲示板を見る", "ko": "인재 게시판 둘러보기", "zh_Hans": "探索人才大厅",
        "ar": "استكشف لوحة المواهب", "ru": "Смотреть доску талантов", "hi": "प्रतिभा बोर्ड देखें"
    },
    "Explorar tablón público": {
        "es": "Explorar tablón público", "en": "Explore public wall", "pt": "Explorar mural público",
        "fr": "Explorer le tableau public", "de": "Öffentliches Board erkunden", "it": "Esplora bacheca pubblica",
        "ja": "公開掲示板を見る", "ko": "공개 게시판 둘러보기", "zh_Hans": "探索公开大厅",
        "ar": "استكشف اللوحة العامة", "ru": "Смотреть публичную доску", "hi": "सार्वजनिक बोर्ड देखें"
    },
    "Explorar todos los perfiles de este sector": {
        "es": "Explorar todos los perfiles de este sector", "en": "Explore all profiles in this sector", "pt": "Explorar todos os perfis deste setor",
        "fr": "Explorer tous les profils de ce secteur", "de": "Alle Profile in diesem Bereich erkunden", "it": "Esplora tutti i profili di questo settore",
        "ja": "この分野の全プロフィールを見る", "ko": "이 분야의 모든 프로필 둘러보기", "zh_Hans": "探索该领域的所有人才主页",
        "ar": "استكشف جميع الملفات في هذا القطاع", "ru": "Смотреть все профили этого сектора", "hi": "इस क्षेत्र के सभी प्रोफाइल देखें"
    },
    "Filtra por sector y descubre las especialidades más demandadas hoy": {
        "es": "Filtra por sector y descubre las especialidades más demandadas hoy",
        "en": "Filter by sector and discover today's most in-demand specialties",
        "pt": "Filtre por setor e descubra as especialidades mais demandadas hoje",
        "fr": "Filtrez par secteur et découvrez les spécialités les plus recherchées aujourd'hui",
        "de": "Nach Bereich filtern und heute gefragteste Spezialisierungen entdecken",
        "it": "Filtra per settore e scopri le specializzazioni più richieste oggi",
        "ja": "分野で絞り込み、今最も求められている専門職を発見",
        "ko": "분야별로 필터링하고 오늘날 가장 수요가 많은 전문 분야를 확인하세요",
        "zh_Hans": "按行业筛选，洞察当下最具市场需求的专业方向",
        "ar": "قم بالتصفية حسب القطاع واكتشف التخصصات الأكثر طلباً اليوم",
        "ru": "Фильтруйте по секторам и открывайте самые востребованные специальности",
        "hi": "क्षेत्र के अनुसार फ़िल्टर करें और आज की सबसे अधिक मांग वाली विशेषज्ञताओं की खोज करें"
    },
    "Finanzas": {
        "es": "Finanzas", "en": "Finance", "pt": "Finanças",
        "fr": "Finance", "de": "Finanzen", "it": "Finanza",
        "ja": "ファイナンス", "ko": "금융", "zh_Hans": "金融财务",
        "ar": "المالية", "ru": "Финансы", "hi": "वित्त"
    },
    "Formato y diseño": {
        "es": "Formato y diseño", "en": "Format and design", "pt": "Formato e design",
        "fr": "Format et design", "de": "Format und Design", "it": "Formato e design",
        "ja": "形式とデザイン", "ko": "형식 및 디자인", "zh_Hans": "格式与设计",
        "ar": "التنسيق والتصميم", "ru": "Формат и дизайн", "hi": "प्रारूप और डिज़ाइन"
    },
    "Haz visible tu talento con un": {
        "es": "Haz visible tu talento con un", "en": "Make your talent visible with an", "pt": "Torne seu talento visível com um",
        "fr": "Rendez votre talent visible avec un", "de": "Machen Sie Ihr Talent sichtbar mit einem", "it": "Rendi visibile il tuo talento con un",
        "ja": "あなたの才能を可視化する", "ko": "당신의 재능을 보여주는", "zh_Hans": "让您的才能脱颖而出：",
        "ar": "اجعل موهبتك مرئية من خلال", "ru": "Раскройте свой талант с помощью", "hi": "अपनी प्रतिभा को दृश्यमान बनाएं"
    },
    "Idiomas disponibles": {
        "es": "Idiomas disponibles", "en": "Languages available", "pt": "Idiomas disponíveis",
        "fr": "Langues disponibles", "de": "Verfügbare Sprachen", "it": "Lingue disponibili",
        "ja": "対応言語数", "ko": "지원 언어", "zh_Hans": "支持的语言",
        "ar": "اللغات المتاحة", "ru": "Доступные языки", "hi": "उपलब्ध भाषाएँ"
    },
    "Imágenes, links y repositorio directo": {
        "es": "Imágenes, links y repositorio directo", "en": "Images, links, and direct repository", "pt": "Imagens, links e repositório direto",
        "fr": "Images, liens et dépôt direct", "de": "Bilder, Links und direktes Repository", "it": "Immagini, link e repository diretto",
        "ja": "画像、リンク、直接リポジトリ連携", "ko": "이미지, 링크 및 직접 저장소 연결", "zh_Hans": "配图、在线链接与直接代码仓库",
        "ar": "صور وروابط ومستودع برمجيات مباشر", "ru": "Изображения, ссылки и прямой репозиторий", "hi": "छवियां, लिंक और प्रत्यक्ष रिपॉजिटरी"
    },
    "Ir a mi Dashboard": {
        "es": "Ir a mi Dashboard", "en": "Go to my Dashboard", "pt": "Ir para meu Dashboard",
        "fr": "Aller à mon Tableau de Bord", "de": "Zu meinem Dashboard", "it": "Vai alla mia Dashboard",
        "ja": "マイダッシュボードへ", "ko": "내 대시보드로 이동", "zh_Hans": "前往我的仪表盘",
        "ar": "الذهاب إلى لوحة التحكم الخاصة بي", "ru": "В мою панель управления", "hi": "मेरे डैशबोर्ड पर जाएं"
    },
    "La diferencia es contundente": {
        "es": "La diferencia es contundente", "en": "The difference is striking", "pt": "A diferença é contundente",
        "fr": "La différence est frappante", "de": "Der Unterschied ist eindeutig", "it": "La differenza è evidente",
        "ja": "違いは一目瞭然", "ko": "차이는 분명합니다", "zh_Hans": "优势一目了然",
        "ar": "الفرق واضح وجلي", "ru": "Разница очевидна", "hi": "अंतर स्पष्ट है"
    },
    "La evolución del currículum profesional": {
        "es": "La evolución del currículum profesional", "en": "The evolution of the professional resume", "pt": "A evolução do currículo profissional",
        "fr": "L'évolution du CV professionnel", "de": "Die Evolution des professionellen Lebenslaufs", "it": "L'evoluzione del curriculum professionale",
        "ja": "プロフェッショナル履歴書の進化形", "ko": "전문가 이력서의 진화", "zh_Hans": "专业职业履历的全面进化",
        "ar": "تطور السيرة الذاتية المهنية", "ru": "Эволюция профессионального резюме", "hi": "पेशेवर बायोडाटा का विकास"
    },
    "Lectura manual o filtros ATS opacos": {
        "es": "Lectura manual o filtros ATS opacos", "en": "Manual reading or opaque ATS filters", "pt": "Leitura manual ou filtros ATS opacos",
        "fr": "Lecture manuelle ou filtres ATS opaques", "de": "Manuelles Lesen oder undurchsichtige ATS-Filter", "it": "Lettura manuale o filtri ATS opachi",
        "ja": "手動での確認、または不透明なATS自動選考", "ko": "수동 검토 또는 불투명한 ATS 필터", "zh_Hans": "繁琐的人工初筛或黑盒 ATS 机器过滤",
        "ar": "قراءة يدوية أو فلاتر ATS غامضة", "ru": "Ручной просмотр или непрозрачные фильтры ATS", "hi": "मैन्युअल पढ़ना या अपारदर्शी ATS फ़िल्टर"
    },
    "Listas de texto sin verificación visual": {
        "es": "Listas de texto sin verificación visual", "en": "Plain text lists without visual proof", "pt": "Listas de texto sem comprovação visual",
        "fr": "Listes de texte sans preuve visuelle", "de": "Reine Textlisten ohne visuellen Nachweis", "it": "Elenchi testuali privi di riscontro visivo",
        "ja": "視覚的な実証のないテキストの箇条書き", "ko": "시각적 입증이 없는 단순 텍스트 목록", "zh_Hans": "毫无视觉实证的枯燥纯文本罗列",
        "ar": "قوائم نصية بدون إثبات بصري", "ru": "Текстовые списки без визуального подтверждения", "hi": "दृश्य प्रमाण के बिना सादे पाठ की सूचियाँ"
    },
    "Marketing & Growth": {
        "es": "Marketing & Growth", "en": "Marketing & Growth", "pt": "Marketing & Growth",
        "fr": "Marketing & Growth", "de": "Marketing & Growth", "it": "Marketing & Growth",
        "ja": "マーケティング & グロース", "ko": "마케팅 & 그로스", "zh_Hans": "市场营销与增长",
        "ar": "التسويق والنمو", "ru": "Маркетинг и рост", "hi": "मार्केटिंग और विकास"
    },
    "Matching Transparente y Cero Spam": {
        "es": "Matching Transparente y Cero Spam", "en": "Transparent Matching and Zero Spam", "pt": "Matching Transparente e Zero Spam",
        "fr": "Matching Transparent et Zéro Spam", "de": "Transparentes Matching und Kein Spam", "it": "Matching Trasparente e Zero Spam",
        "ja": "透明なマッチングとスパムゼロ", "ko": "투명한 매칭 및 스팸 제로", "zh_Hans": "透明匹配与零垃圾骚扰",
        "ar": "مطابقة شفافة وبدون إزعاج", "ru": "Прозрачный мэтчинг и ноль спама", "hi": "पारदर्शी मिलान और शून्य स्पैम"
    },
    "Muestra capturas de proyectos, demos funcionales y repositorios de código. Demuestra lo que sabes hacer.": {
        "es": "Muestra capturas de proyectos, demos funcionales y repositorios de código. Demuestra lo que sabes hacer.",
        "en": "Show project screenshots, live demos, and code repositories. Prove what you can do.",
        "pt": "Mostre capturas de projetos, demos funcionais e repositórios de código. Prove o que você sabe fazer.",
        "fr": "Présentez des captures d'écran de projets, des démos fonctionnelles et des dépôts de code. Prouvez votre savoir-faire.",
        "de": "Zeigen Sie Projekt-Screenshots, funktionierende Demos und Code-Repositories. Beweisen Sie Ihr Können.",
        "it": "Mostra screenshot di progetti, demo funzionanti e repository di codice. Dimostra cosa sai fare.",
        "ja": "プロジェクトのスクリーンショット、動作デモ、コードリポジトリを公開。あなたの実力を証明しましょう。",
        "ko": "프로젝트 스크린샷, 실제 작동하는 데모, 코드 저장소를 보여주세요. 당신의 역량을 증명하세요.",
        "zh_Hans": "展示项目实图截图、在线运行演示与代码仓库，用真实成果证明您的实力。",
        "ar": "اعرض لقطات شاشة للمشاريع، وعروضاً حية، ومستودعات برمجية. أثبت ما يمكنك فعله.",
        "ru": "Показывайте скриншоты проектов, рабочие демо и репозитории кода. Докажите свои навыки на деле.",
        "hi": "परियोजना स्क्रीनशॉट, कार्यात्मक डेमो और कोड रिपॉजिटरी दिखाएं। साबित करें कि आप क्या कर सकते हैं।"
    },
    "Niveles de clasificación": {
        "es": "Niveles de clasificación", "en": "Classification levels", "pt": "Níveis de classificação",
        "fr": "Niveaux de classification", "de": "Klassifizierungsebenen", "it": "Livelli di classificazione",
        "ja": "分類レベル", "ko": "분류 체계 단계", "zh_Hans": "分类层级",
        "ar": "مستويات التصنيف", "ru": "Уровня классификации", "hi": "वर्गीकरण स्तर"
    },
    "Obsoleto de inmediato": {
        "es": "Obsoleto de inmediato", "en": "Instantly obsolete", "pt": "Obsoleto de imediato",
        "fr": "Obsolète immédiatement", "de": "Sofort veraltet", "it": "Subito obsoleto",
        "ja": "すぐに陳腐化", "ko": "즉시 구식이 됨", "zh_Hans": "迅速过时",
        "ar": "يصبح قديماً على الفور", "ru": "Моментально устаревает", "hi": "तुरंत पुराना"
    },
    "Olvídate de palabras clave sueltas. Clasificamos perfiles mediante Sector, Rol, Especialidad y Tags para un matching quirúrgico.": {
        "es": "Olvídate de palabras clave sueltas. Clasificamos perfiles mediante Sector, Rol, Especialidad y Tags para un matching quirúrgico.",
        "en": "Forget loose keywords. We classify profiles through Sector, Role, Specialty, and Tags for surgical matching.",
        "pt": "Esqueça palavras-chave soltas. Classificamos perfis através de Setor, Cargo, Especialidade e Tags para um matching cirúrgico.",
        "fr": "Oubliez les mots-clés épars. Nous classons les profils par Secteur, Rôle, Spécialité et Tags pour un matching chirurgical.",
        "de": "Vergessen Sie lose Stichwörter. Wir klassifizieren Profile nach Branche, Rolle, Spezialisierung und Tags für chirurgische Treffergenauigkeit.",
        "it": "Dimentica le parole chiave sparse. Classifichiamo i profili tramite Settore, Ruolo, Specializzazione e Tag per un matching chirurgico.",
        "ja": "孤立したキーワード検索はもう不要。分野、役割、専門領域、タグの組み合わせで精密なマッチングを実現します。",
        "ko": "단순 키워드 나열은 잊으세요. 정확한 매칭을 위해 섹터, 역할, 전문 분야, 태그로 프로필을 정밀하게 분류합니다.",
        "zh_Hans": "告别散乱无序的关键词搜索。我们通过行业、角色、专长与标签精准分类，实现手术级精准契合。",
        "ar": "انسَ الكلمات المفتاحية العشوائية. نحن نصنف الملفات عبر القطاع والدور والتخصص والوسوم لمطابقة دقيقة كالجراحة.",
        "ru": "Забудьте о случайных ключевых словах. Мы классифицируем профили по сектору, роли, специальности и тегам для ювелирного совпадения.",
        "hi": "अलग-थलग कीवर्ड भूल जाइए। हम सटीक मिलान के लिए सेक्टर, भूमिका, विशेषता और टैग द्वारा प्रोफाइल को वर्गीकृत करते हैं।"
    },
    "Perfil Vivo TalentStack": {
        "es": "Perfil Vivo TalentStack", "en": "TalentStack Live Profile", "pt": "Perfil Vivo TalentStack",
        "fr": "Profil Vivant TalentStack", "de": "TalentStack Live-Profil", "it": "Profilo Dinamico TalentStack",
        "ja": "TalentStack ライブプロフィール", "ko": "TalentStack 라이브 프로필", "zh_Hans": "TalentStack 动态主页",
        "ar": "ملف TalentStack الحي", "ru": "Живой профиль TalentStack", "hi": "टैलेंटस्टैक लाइव प्रोफ़ाइल"
    },
    "Portafolio Multimedia Integrado": {
        "es": "Portafolio Multimedia Integrado", "en": "Integrated Multimedia Portfolio", "pt": "Portfólio Multimídia Integrado",
        "fr": "Portfolio Multimédia Intégré", "de": "Integriertes Multimedia-Portfolio", "it": "Portfolio Multimediale Integrato",
        "ja": "統合マルチメディアポートフォリオ", "ko": "통합 멀티미디어 포트폴리오", "zh_Hans": "一体化富媒体作品集",
        "ar": "معرض وسائط متكامل", "ru": "Интегрированное мультимедиа-портфолио", "hi": "एकीकृत मल्टीमीडिया पोर्टफोलियो"
    },
    "Portafolio en vivo con demos y repositorios": {
        "es": "Portafolio en vivo con demos y repositorios", "en": "Live portfolio with demos and repositories", "pt": "Portfólio ao vivo com demos e repositórios",
        "fr": "Portfolio en direct avec démos et dépôts", "de": "Live-Portfolio mit Demos und Repositories", "it": "Portfolio live con demo e repository",
        "ja": "デモやリポジトリを備えたライブポートフォリオ", "ko": "데모 및 저장소가 포함된 실시간 포트폴리오", "zh_Hans": "配有在线演示与代码仓库的活态作品集",
        "ar": "معرض أعمال حي مع عروض توضيحية ومستودعات", "ru": "Живое портфолио с демо и репозиториями", "hi": "डेमो और रिपॉजिटरी के साथ लाइव पोर्टफोलियो"
    },
    "Presencia Global en 12 Idiomas": {
        "es": "Presencia Global en 12 Idiomas", "en": "Global Presence in 12 Languages", "pt": "Presença Global em 12 Idiomas",
        "fr": "Présence Mondiale en 12 Langues", "de": "Globale Präsenz in 12 Sprachen", "it": "Presenza Globale in 12 Lingue",
        "ja": "12言語によるグローバル展開", "ko": "12개 언어로 글로벌 진출", "zh_Hans": "支持12种语言的全球影响力",
        "ar": "حضور عالمي بـ 12 لغة", "ru": "Глобальное присутствие на 12 языках", "hi": "12 भाषाओं में वैश्विक उपस्थिति"
    },
    "Profesionales conectados": {
        "es": "Profesionales conectados", "en": "Connected professionals", "pt": "Profissionais conectados",
        "fr": "Professionnels connectés", "de": "Vernetzte Fachkräfte", "it": "Professionisti connessi",
        "ja": "接続されたプロフェッショナル", "ko": "연결된 전문가", "zh_Hans": "入驻的专业人才",
        "ar": "محترفون متصلون", "ru": "Подключенных специалистов", "hi": "जुड़े हुए पेशेवर"
    },
    "Proyectos interactivos": {
        "es": "Proyectos interactivos", "en": "Interactive projects", "pt": "Projetos interativos",
        "fr": "Projets interactifs", "de": "Interaktive Projekte", "it": "Progetti interattivi",
        "ja": "インタラクティブなプロジェクト", "ko": "대화형 프로젝트", "zh_Hans": "互动项目展示",
        "ar": "مشاريع تفاعلية", "ru": "Интерактивные проекты", "hi": "इंटरैक्टिव परियोजनाएं"
    },
    "Rechazado por filtro ATS": {
        "es": "Rechazado por filtro ATS", "en": "Rejected by ATS filter", "pt": "Rejeitado pelo filtro ATS",
        "fr": "Rejeté par le filtre ATS", "de": "Vom ATS-Filter abgelehnt", "it": "Rifiutato dal filtro ATS",
        "ja": "ATS自動フィルターで不通過", "ko": "ATS 필터에 의해 탈락", "zh_Hans": "遭 ATS 筛选器直接过滤淘汰",
        "ar": "مرفوض بواسطة فلاتر ATS", "ru": "Отклонено фильтром ATS", "hi": "ATS फ़िल्टर द्वारा अस्वीकृत"
    },
    "Remoto / Disponible a nivel global": {
        "es": "Remoto / Disponible a nivel global", "en": "Remote / Available globally", "pt": "Remoto / Disponível globalmente",
        "fr": "Télétravail / Disponible dans le monde entier", "de": "Remote / Weltweit verfügbar", "it": "Remoto / Disponibile a livello globale",
        "ja": "リモート / グローバル対応可能", "ko": "원격 근무 / 전 세계 어디서나 가능", "zh_Hans": "远程 / 全球随时就绪",
        "ar": "عن بُعد / متاح عالمياً", "ru": "Удаленно / Доступен по всему миру", "hi": "रिमोट / विश्व स्तर पर उपलब्ध"
    },
    "Rígido, estático y limitado a 2 páginas": {
        "es": "Rígido, estático y limitado a 2 páginas", "en": "Rigid, static, and limited to 2 pages", "pt": "Rígido, estático e limitado a 2 páginas",
        "fr": "Rigide, statique et limité à 2 pages", "de": "Starr, statisch und auf 2 Seiten beschränkt", "it": "Rigido, statico e limitato a 2 pagine",
        "ja": "硬直的で静的、たった2ページに制限", "ko": "경직되고 정적이며 2페이지로 제한됨", "zh_Hans": "僵硬死板、形式静态且受限于2页纸",
        "ar": "جامد، ثابت ومحدود بصفحتين", "ru": "Жесткий, статичный и ограниченный 2 страницами", "hi": "कठोर, स्थिर और 2 पृष्ठों तक सीमित"
    },
    "Semanas de silencio por correo": {
        "es": "Semanas de silencio por correo", "en": "Weeks of email silence", "pt": "Semanas de silêncio por e-mail",
        "fr": "Des semaines de silence par e-mail", "de": "Wochenlanges Schweigen per E-Mail", "it": "Settimane di silenzio via email",
        "ja": "メール送信後の何週間もの沈黙", "ko": "몇 주간 이어지는 이메일 무응답", "zh_Hans": "投递后数周杳无音讯",
        "ar": "أسابيع من الصمت عبر البريد الإلكتروني", "ru": "Недели молчания по электронной почте", "hi": "ईमेल पर हफ़्तों की चुप्पी"
    },
    "Senior Full-Stack & Cloud Engineer": {
        "es": "Senior Full-Stack & Cloud Engineer", "en": "Senior Full-Stack & Cloud Engineer", "pt": "Senior Full-Stack & Cloud Engineer",
        "fr": "Ingénieur Senior Full-Stack & Cloud", "de": "Senior Full-Stack & Cloud Engineer", "it": "Senior Full-Stack & Cloud Engineer",
        "ja": "シニア フルスタック & クラウドエンジニア", "ko": "시니어 풀스택 & 클라우드 엔지니어", "zh_Hans": "资深全栈与云架构工程师",
        "ar": "مهندس أول فول ستاك وحوسبة سحابية", "ru": "Старший фулстек и облачный инженер", "hi": "वरिष्ठ फुल-स्टैक और क्लाउड इंजीनियर"
    },
    "Sin algoritmos opacos ni comisiones abusivas. Filtra perfiles por disponibilidad real y contacta sin rodeos.": {
        "es": "Sin algoritmos opacos ni comisiones abusivas. Filtra perfiles por disponibilidad real y contacta sin rodeos.",
        "en": "No opaque algorithms or unfair fees. Filter profiles by real availability and reach out directly.",
        "pt": "Sem algoritmos opacos ou taxas abusivas. Filtre perfis por disponibilidade real e entre em contato direto.",
        "fr": "Pas d'algorithmes opaques ni de frais abusifs. Filtrez les profils par disponibilité réelle et contactez directement.",
        "de": "Keine undurchsichtigen Algorithmen oder unfairen Gebühren. Profile nach echter Verfügbarkeit filtern und direkt ansprechen.",
        "it": "Nessun algoritmo opaco o commissione esagerata. Filtra i profili in base alla reale disponibilità e contatta direttamente.",
        "ja": "不透明なアルゴリズムや不当な手数料なし。実際の稼働状況で絞り込み、直接アプローチできます。",
        "ko": "불투명한 알고리즘이나 과도한 수수료가 없습니다. 실제 가용성으로 프로필을 필터링하고 바로 연락하세요.",
        "zh_Hans": "没有黑盒算法或不合理抽成。根据真实可用状态筛选人才，零障碍直接对接。",
        "ar": "بدون خوارزميات غامضة أو عمولات مجحفة. قم بتصفية الملفات حسب التوفر الفعلي وتواصل دون وسيط.",
        "ru": "Никаких непрозрачных алгоритмов или скрытых комиссий. Фильтруйте кандидатов по реальной занятости и общайтесь напрямую.",
        "hi": "कोई अपारदर्शी एल्गोरिदम या अनुचित शुल्क नहीं। वास्तविक उपलब्धता के आधार पर प्रोफाइल फ़िल्टर करें और सीधे संपर्क करें।"
    },
    "Sin coste para profesionales": {
        "es": "Sin coste para profesionales", "en": "No cost for professionals", "pt": "Sem custos para profissionais",
        "fr": "Sans frais pour les professionnels", "de": "Kostenlos für Fachkräfte", "it": "Senza costi per i professionisti",
        "ja": "プロフェッショナル利用料ゼロ", "ko": "전문가 이용료 무료", "zh_Hans": "专业人才完全免费",
        "ar": "بدون أي تكلفة على المهنيين", "ru": "Бесплатно для специалистов", "hi": "पेशेवरों के लिए कोई लागत नहीं"
    },
    "Superpoderes de TalentStack": {
        "es": "Superpoderes de TalentStack", "en": "TalentStack Superpowers", "pt": "Superpoderes do TalentStack",
        "fr": "Les Super-Pouvoirs de TalentStack", "de": "Superkräfte von TalentStack", "it": "Superpoteri di TalentStack",
        "ja": "TalentStack の強み", "ko": "TalentStack의 핵심 역량", "zh_Hans": "TalentStack 核心超能力",
        "ar": "مزايا TalentStack الفائقة", "ru": "Суперсилы TalentStack", "hi": "टैलेंटस्टैक की महाशक्तियाँ"
    },
    "Tablón de Candidatos": {
        "es": "Tablón de Candidatos", "en": "Candidates Wall", "pt": "Mural de Candidatos",
        "fr": "Tableau des Candidats", "de": "Kandidaten-Board", "it": "Bacheca Candidati",
        "ja": "候補者掲示板", "ko": "후보자 게시판", "zh_Hans": "人才大厅",
        "ar": "لوحة المرشحين", "ru": "Доска кандидатов", "hi": "उम्मीदवार बोर्ड"
    },
    "Tablón de Reclutadores": {
        "es": "Tablón de Reclutadores", "en": "Recruiters Wall", "pt": "Mural de Recrutadores",
        "fr": "Tableau des Recruteurs", "de": "Recruiter-Board", "it": "Bacheca Recruiter",
        "ja": "採用担当者掲示板", "ko": "채용 담당자 게시판", "zh_Hans": "企业招聘大厅",
        "ar": "لوحة مسؤولي التوظيف", "ru": "Доска рекрутеров", "hi": "भर्तीकर्ता बोर्ड"
    },
    "Taxonomía Estructurada en 4 Capas": {
        "es": "Taxonomía Estructurada en 4 Capas", "en": "Structured 4-Layer Taxonomy", "pt": "Taxonomia Estruturada em 4 Camadas",
        "fr": "Taxonomie Structurée en 4 Niveaux", "de": "Strukturierte 4-Stufen-Taxonomie", "it": "Tassonomia Strutturata a 4 Livelli",
        "ja": "4層構造の分類体系", "ko": "구조화된 4단계 분류 체계", "zh_Hans": "结构化4层精准分类",
        "ar": "تصنيف منظم من 4 طبقات", "ru": "Структурированная 4-уровневая таксономия", "hi": "संरचित 4-स्तरीय वर्गीकरण"
    },
    "Taxonomía de Precisión": {
        "es": "Taxonomía de Precisión", "en": "Precision Taxonomy", "pt": "Taxonomia de Precisão",
        "fr": "Taxonomie de Précision", "de": "Präzisions-Taxonomie", "it": "Tassonomia di Precisione",
        "ja": "高精度分類システム", "ko": "정밀 분류 체계", "zh_Hans": "高精度分类系统",
        "ar": "تصنيف فائق الدقة", "ru": "Высокоточная таксономия", "hi": "सटीक वर्गीकरण"
    },
    "Taxonomía de precisión en 4 capas": {
        "es": "Taxonomía de precisión en 4 capas", "en": "Precision 4-layer taxonomy", "pt": "Taxonomia de precisão em 4 camadas",
        "fr": "Taxonomie de précision en 4 niveaux", "de": "Präzise 4-Stufen-Taxonomie", "it": "Tassonomia di precisione a 4 livelli",
        "ja": "4層による高精度な分類", "ko": "4단계 정밀 분류 체계", "zh_Hans": "4层高精度技术分类",
        "ar": "تصنيف دقيق من 4 مستويات", "ru": "Высокоточная таксономия в 4 уровня", "hi": "4 परतों में सटीक वर्गीकरण"
    },
    "Taxonomía inteligente en 4 capas": {
        "es": "Taxonomía inteligente en 4 capas", "en": "Intelligent 4-layer taxonomy", "pt": "Taxonomia inteligente em 4 camadas",
        "fr": "Taxonomie intelligente en 4 niveaux", "de": "Intelligente 4-Stufen-Taxonomie", "it": "Tassonomia intelligente a 4 livelli",
        "ja": "インテリジェントな4層分類", "ko": "지능형 4단계 분류 체계", "zh_Hans": "智能4层精准分类",
        "ar": "تصنيف ذكي من 4 طبقات", "ru": "Умная таксономия в 4 слоя", "hi": "4 परतों में बुद्धिमान वर्गीकरण"
    },
    "Tecnología": {
        "es": "Tecnología", "en": "Technology", "pt": "Tecnologia",
        "fr": "Technologie", "de": "Technologie", "it": "Tecnologia",
        "ja": "テクノロジー", "ko": "기술", "zh_Hans": "科技技术",
        "ar": "التكنولوجيا", "ru": "Технологии", "hi": "प्रौद्योगिकी"
    },
    "Tecnologías y competencias destacadas": {
        "es": "Tecnologías y competencias destacadas", "en": "Featured skills and technologies", "pt": "Tecnologias e competências em destaque",
        "fr": "Technologies et compétences mises en avant", "de": "Hervorgehobene Fähigkeiten und Technologien", "it": "Competenze e tecnologie in evidenza",
        "ja": "注目のスキルとテクノロジー", "ko": "주요 기술 및 핵심 역량", "zh_Hans": "核心技能与重点技术",
        "ar": "التقنيات والمهارات البارزة", "ru": "Ключевые технологии и навыки", "hi": "प्रमुख प्रौद्योगिकियां और कौशल"
    },
    "Texto plano sin interactividad ni demostración práctica": {
        "es": "Texto plano sin interactividad ni demostración práctica",
        "en": "Plain text without interactivity or hands-on demonstration",
        "pt": "Texto simples sem interatividade ou demonstração prática",
        "fr": "Texte brut sans interactivité ni démonstration pratique",
        "de": "Reiner Text ohne Interaktivität oder praktischen Nachweis",
        "it": "Testo semplice senza interattività né dimostrazione pratica",
        "ja": "双方向性も実際のデモもない平坦なテキスト",
        "ko": "상호작용이나 실질적 증명이 없는 단순 텍스트",
        "zh_Hans": "缺乏互动与实操证明的纯文本",
        "ar": "نص عادي بدون تفاعلية أو إثبات عملي",
        "ru": "Простой текст без интерактивности и практических доказательств",
        "hi": "इंटरैक्टिविटी या व्यावहारिक प्रदर्शन के बिना सादा पाठ"
    },
    "Traducción automática a 12 idiomas": {
        "es": "Traducción automática a 12 idiomas", "en": "Automatic translation into 12 languages", "pt": "Tradução automática para 12 idiomas",
        "fr": "Traduction automatique en 12 langues", "de": "Automatische Übersetzung in 12 Sprachen", "it": "Traduzione automatica in 12 lingue",
        "ja": "12言語への自動翻訳", "ko": "12개 언어 자동 번역", "zh_Hans": "自动适配12种语言翻译",
        "ar": "ترجمة تلقائية إلى 12 لغة", "ru": "Автоматический перевод на 12 языков", "hi": "12 भाषाओं में स्वचालित अनुवाद"
    },
    "Traducción nativa en 12 idiomas": {
        "es": "Traducción nativa en 12 idiomas", "en": "Native translation in 12 languages", "pt": "Tradução nativa em 12 idiomas",
        "fr": "Traduction native en 12 langues", "de": "Native Übersetzung in 12 Sprachen", "it": "Traduzione nativa in 12 lingue",
        "ja": "12言語のネイティブ翻訳", "ko": "12개 언어 원어민급 번역 지원", "zh_Hans": "12种语言原生级翻译",
        "ar": "ترجمة أصلية بـ 12 لغة", "ru": "Нативный перевод на 12 языков", "hi": "12 भाषाओं में मूल अनुवाद"
    },
    "Tu perfil y su taxonomía se traducen automáticamente para conectar con oportunidades en todo el mundo sin barreras.": {
        "es": "Tu perfil y su taxonomía se traducen automáticamente para conectar con oportunidades en todo el mundo sin barreras.",
        "en": "Your profile and taxonomy translate automatically to connect with opportunities worldwide without barriers.",
        "pt": "Seu perfil e sua taxonomia são traduzidos automaticamente para conectar com oportunidades no mundo todo sem barreiras.",
        "fr": "Votre profil et sa taxonomie sont traduits automatiquement pour vous connecter aux opportunités mondiales sans obstacles.",
        "de": "Ihr Profil und Ihre Taxonomie werden automatisch übersetzt, um Hürden abzubauen und globale Chancen zu erschließen.",
        "it": "Il tuo profilo e la sua tassonomia si traducono automaticamente per connetterti con opportunità in tutto il mondo senza barriere.",
        "ja": "プロフィールと分類が自動翻訳され、言葉の壁を越えて世界中のチャンスとつながります。",
        "ko": "당신의 프로필과 분류 체계가 자동으로 번역되어 장벽 없이 전 세계의 기회와 연결됩니다.",
        "zh_Hans": "您的主页与技能分类将自动翻译，跨越语言障碍，畅联全球顶尖工作机遇。",
        "ar": "يتم ترجمة ملفك وتصنيفك تلقائيًا للتواصل مع الفرص في جميع أنحاء العالم دون أي حواجز.",
        "ru": "Ваш профиль и таксономия автоматически переводятся, открывая доступ к вакансиям по всему миру без языковых барьеров.",
        "hi": "आपकी प्रोफ़ाइल और उसका वर्गीकरण बाधाओं के बिना दुनिया भर के अवसरों से जुड़ने के लिए स्वचालित रूप से अनुवादित होता है।"
    },
    "Un PDF por cada idioma a traducir": {
        "es": "Un PDF por cada idioma a traducir", "en": "A separate PDF for each language to translate", "pt": "Um PDF para cada idioma a traduzir",
        "fr": "Un PDF pour chaque langue à traduire", "de": "Ein separates PDF für jede zu übersetzende Sprache", "it": "Un PDF diverso per ciascuna lingua da tradurre",
        "ja": "言語ごとに別々のPDFを用意する必要あり", "ko": "번역할 언어마다 별도의 PDF 필요", "zh_Hans": "每种语言都需单独维护一份 PDF",
        "ar": "ملف PDF منفصل لكل لغة تريد ترجمتها", "ru": "Отдельный PDF для каждого переводимого языка", "hi": "अनुवाद करने के लिए प्रत्येक भाषा के लिए एक अलग PDF"
    },
    "Ver demo en vivo": {
        "es": "Ver demo en vivo", "en": "View live demo", "pt": "Ver demonstração ao vivo",
        "fr": "Voir la démo en direct", "de": "Live-Demo ansehen", "it": "Guarda la demo dal vivo",
        "ja": "ライブデモを見る", "ko": "라이브 데모 보기", "zh_Hans": "查看在线演示",
        "ar": "مشاهدة العرض الحي", "ru": "Смотреть живое демо", "hi": "लाइव डेमो देखें"
    },
    "Vista interactiva": {
        "es": "Vista interactiva", "en": "Interactive view", "pt": "Visualização interativa",
        "fr": "Vue interactive", "de": "Interaktive Ansicht", "it": "Vista interattiva",
        "ja": "インタラクティブビュー", "ko": "대화형 보기", "zh_Hans": "交互式预览",
        "ar": "عرض تفاعلي", "ru": "Интерактивный вид", "hi": "इंटरैक्टिव दृश्य"
    },
    "perfil profesional interactivo": {
        "es": "perfil profesional interactivo", "en": "interactive professional profile", "pt": "perfil profissional interativo",
        "fr": "profil professionnel interactif", "de": "interaktiven beruflichen Profil", "it": "profilo professionale interattivo",
        "ja": "インタラクティブな専門プロフィール", "ko": "인터랙티브 전문 프로필", "zh_Hans": "互动式专业人才主页",
        "ar": "ملف مهني تفاعلي", "ru": "интерактивным профессиональным профилем", "hi": "इंटरैक्टिव पेशेवर प्रोफ़ाइल"
    },
    "¡Simulación interactiva! En un perfil real, este botón abre el canal de contacto directo con el candidato.": {
        "es": "¡Simulación interactiva! En un perfil real, este botón abre el canal de contacto directo con el candidato.",
        "en": "Interactive preview! In a live profile, this button opens direct communication with the candidate.",
        "pt": "Simulação interativa! Em um perfil real, este botão abre o canal de contato direto com o candidato.",
        "fr": "Simulation interactive ! Sur un profil réel, ce bouton ouvre le canal de contact direct avec le candidat.",
        "de": "Interaktive Vorschau! Bei einem echten Profil öffnet diese Schaltfläche den direkten Kontakt zum Kandidaten.",
        "it": "Simulazione interattiva! In un profilo reale, questo pulsante apre il canale di contatto diretto con il candidato.",
        "ja": "インタラクティブ体験！実際のプロフィールでは、このボタンから候補者に直接メッセージを送信できます。",
        "ko": "인터랙티브 시뮬레이션! 실제 프로필에서는 이 버튼으로 후보자와 직접 연락할 수 있습니다.",
        "zh_Hans": "交互模拟体验！在真实主页中，点击此按钮可直接与候选人建立联系。",
        "ar": "محاكاة تفاعلية! في الملف الحقيقي، يفتح هذا الزر قناة الاتصال المباشر مع المرشح.",
        "ru": "Интерактивная демонстрация! В реальном профиле эта кнопка открывает прямой контакт с кандидатом.",
        "hi": "इंटरैक्टिव पूर्वावलोकन! वास्तविक प्रोफ़ाइल में, यह बटन उम्मीदवार के साथ सीधा संपर्क खोलता है।"
    },
    "¿Buscas contratar talento?": {
        "es": "¿Buscas contratar talento?", "en": "Looking to hire talent?", "pt": "Procurando contratar talentos?",
        "fr": "Vous cherchez à recruter des talents ?", "de": "Möchten Sie Talente einstellen?", "it": "Cerchi talenti da assumere?",
        "ja": "優秀な人材の採用をお考えですか？", "ko": "인재를 채용하고 싶으신가요?", "zh_Hans": "正在寻找优秀人才？",
        "ar": "هل تبحث عن توظيف كفاءات؟", "ru": "Ищете талантливых сотрудников?", "hi": "क्या आप प्रतिभा को नियुक्त करना चाहते हैं?"
    },
    "¿Listo para dar el salto al perfil interactivo?": {
        "es": "¿Listo para dar el salto al perfil interactivo?", "en": "Ready to leap into the interactive profile era?", "pt": "Pronto para dar o salto para o perfil interativo?",
        "fr": "Prêt à franchir le pas vers le profil interactif ?", "de": "Bereit für den Sprung zum interaktiven Profil?", "it": "Pronto a fare il salto verso il profilo interattivo?",
        "ja": "インタラクティブなプロフィールへ進化しませんか？", "ko": "대화형 프로필로 한 단계 도약할 준비가 되셨나요?", "zh_Hans": "准备好跨入互动式主页时代了吗？",
        "ar": "هل أنت مستعد للانتقال إلى الملف التفاعلي؟", "ru": "Готовы сделать шаг к интерактивному профилю?", "hi": "क्या आप इंटरैक्टिव प्रोफ़ाइल की ओर कदम बढ़ाने के लिए तैयार हैं?"
    },
    "¿Por qué un perfil interactivo supera a cualquier PDF?": {
        "es": "¿Por qué un perfil interactivo supera a cualquier PDF?", "en": "Why does an interactive profile beat any PDF?", "pt": "Por que um perfil interativo supera qualquer PDF?",
        "fr": "Pourquoi un profil interactif surpasse-t-il n'importe quel PDF ?", "de": "Warum schlägt ein interaktives Profil jedes PDF?", "it": "Perché un profilo interattivo supera qualsiasi PDF?",
        "ja": "なぜインタラクティブなプロフィールはあらゆるPDFに勝るのか？", "ko": "왜 대화형 프로필이 기존 PDF를 압도할까요?", "zh_Hans": "为什么互动式主页彻底超越传统的 PDF？",
        "ar": "لماذا يتفوق الملف التفاعلي على أي ملف PDF؟", "ru": "Почему интерактивный профиль превосходит любой PDF?", "hi": "एक इंटरैक्टिव प्रोफ़ाइल किसी भी PDF से बेहतर क्यों है?"
    }
}

def apply_landing_translations():
    for lang in LANGUAGES:
        po_path = f"locale/{lang}/LC_MESSAGES/django.po"
        mo_path = f"locale/{lang}/LC_MESSAGES/django.mo"
        if not os.path.exists(po_path):
            continue

        po = polib.pofile(po_path)
        existing = {e.msgid: e for e in po}
        added = 0
        updated = 0

        for msgid, trans in LANDING_TRANSLATIONS.items():
            str_val = trans.get(lang, trans.get('en', msgid))
            if msgid in existing:
                e = existing[msgid]
                if 'fuzzy' in e.flags:
                    e.flags.remove('fuzzy')
                if not e.msgstr.strip() or lang != 'es':
                    e.msgstr = str_val
                    updated += 1
            else:
                new_e = polib.POEntry(msgid=msgid, msgstr=str_val)
                po.append(new_e)
                existing[msgid] = new_e
                added += 1

        po.save(po_path)
        po.save_as_mofile(mo_path)
        print(f"[{lang}] Landing Translations: {added} added, {updated} updated -> saved to {mo_path}")

if __name__ == '__main__':
    apply_landing_translations()
