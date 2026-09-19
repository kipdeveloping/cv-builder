# -*- coding: utf-8 -*-
import os
import polib

LANGUAGES = ['es', 'en', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'zh_Hans', 'ar', 'ru', 'hi']

WALL_TRANSLATIONS = {
    "Aumentan el score de afinidad": {
        "es": "Aumentan el score de afinidad", "en": "Boost the affinity score", "pt": "Aumentam o score de afinidade",
        "fr": "Augmentent le score d'affinité", "de": "Erhöhen den Passungs-Score", "it": "Aumentano il punteggio di affinità",
        "ja": "適合スコアを加算", "ko": "적합도 점수 증가", "zh_Hans": "提高契合度评分",
        "ar": "تزيد من درجة التوافق", "ru": "Повышают показатель соответствия", "hi": "समानता स्कोर बढ़ाते हैं"
    },
    "Buscando empresas y reclutadores...": {
        "es": "Buscando empresas y reclutadores...", "en": "Searching for companies and recruiters...",
        "pt": "Buscando empresas e recrutadores...", "fr": "Recherche d'entreprises et de recruteurs...",
        "de": "Suche nach Unternehmen und Recruitern...", "it": "Ricerca di aziende e recruiter...",
        "ja": "企業と採用担当者を検索中...", "ko": "기업 및 채용 담당자 검색 중...", "zh_Hans": "正在搜索企业与招聘人员...",
        "ar": "جاري البحث عن شركات ومسؤولي توظيف...", "ru": "Поиск компаний и рекрутеров...", "hi": "कंपनियों और भर्तीकर्ताओं की खोज की जा रही है..."
    },
    "Buscando profesionales...": {
        "es": "Buscando profesionales...", "en": "Searching for professionals...", "pt": "Buscando profissionais...",
        "fr": "Recherche de professionnels...", "de": "Suche nach Fachkräften...", "it": "Ricerca di professionisti...",
        "ja": "プロフェッショナルを検索中...", "ko": "전문가 검색 중...", "zh_Hans": "正在搜索专业人才...",
        "ar": "جاري البحث عن مهنيين...", "ru": "Поиск специалистов...", "hi": "पेशेवरों की खोज की जा रही है..."
    },
    "Buscar sector (ej: Tecnología, Salud)...": {
        "es": "Buscar sector (ej: Tecnología, Salud)...", "en": "Search sector (e.g. Technology, Health)...",
        "pt": "Buscar setor (ex: Tecnologia, Saúde)...", "fr": "Rechercher un secteur (ex : Technologie, Santé)...",
        "de": "Branche suchen (z.B. Technologie, Gesundheit)...", "it": "Cerca settore (es: Tecnologia, Salute)...",
        "ja": "分野を検索 (例: テクノロジー、医療)...", "ko": "섹터 검색 (예: 기술, 헬스케어)...", "zh_Hans": "搜索行业 (例: 科技技术、医疗健康)...",
        "ar": "ابحث عن قطاع (مثل: التكنولوجيا، الصحة)...", "ru": "Искать сектор (напр. Технологии, Здравоохранение)...", "hi": "क्षेत्र खोजें (उदा: प्रौद्योगिकी, स्वास्थ्य)..."
    },
    "Cargando empresas...": {
        "es": "Cargando empresas...", "en": "Loading companies...", "pt": "Carregando empresas...",
        "fr": "Chargement des entreprises...", "de": "Unternehmen laden...", "it": "Caricamento aziende...",
        "ja": "企業を読み込み中...", "ko": "기업 목록 불러오는 중...", "zh_Hans": "正在加载企业...",
        "ar": "جاري تحميل الشركات...", "ru": "Загрузка компаний...", "hi": "कंपनियां लोड हो रही हैं..."
    },
    "Cargando perfiles...": {
        "es": "Cargando perfiles...", "en": "Loading profiles...", "pt": "Carregando perfis...",
        "fr": "Chargement des profils...", "de": "Profile laden...", "it": "Caricamento profili...",
        "ja": "プロフィールを読み込み中...", "ko": "프로필 불러오는 중...", "zh_Hans": "正在加载个人资料...",
        "ar": "جاري تحميل الملفات...", "ru": "Загрузка профилей...", "hi": "प्रोफ़ाइल लोड हो रही हैं..."
    },
    "Descubre organizaciones y reclutadores que buscan talento activamente con total transparencia.": {
        "es": "Descubre organizaciones y reclutadores que buscan talento activamente con total transparencia.",
        "en": "Discover organizations and recruiters actively seeking talent with total transparency.",
        "pt": "Descubra organizações e recrutadores que buscam talentos ativamente com total transparência.",
        "fr": "Découvrez des organisations et des recruteurs recherchant activement des talents en toute transparence.",
        "de": "Entdecken Sie Unternehmen und Recruiter, die mit voller Transparenz aktiv nach Talenten suchen.",
        "it": "Scopri organizzazioni e recruiter che cercano attivamente talenti con totale trasparenza.",
        "ja": "完全な透明性のもとで積極的に人材を募集している企業や採用担当者を見つけましょう。",
        "ko": "완전한 투명성으로 인재를 적극적으로 찾는 기업과 채용 담당자를 발견하세요.",
        "zh_Hans": "在极致透明的生态中，探索正在积极招揽人才的优质企业与招聘官。",
        "ar": "اكتشف المؤسسات ومسؤولي التوظيف الذين يبحثون بنشاط عن الكفاءات بشفافية كاملة.",
        "ru": "Открывайте для себя компании и рекрутеров, активно ищущих таланты с полной прозрачностью.",
        "hi": "पूर्ण पारदर्शिता के साथ सक्रिय रूप से प्रतिभा की तलाश कर रहे संगठनों और भर्तीकर्ताओं की खोज करें।"
    },
    "Disponible": {
        "es": "Disponible", "en": "Available", "pt": "Disponível", "fr": "Disponible",
        "de": "Verfügbar", "it": "Disponibile", "ja": "対応可能", "ko": "가능",
        "zh_Hans": "可联系", "ar": "متاح", "ru": "Доступен", "hi": "उपलब्ध"
    },
    "El perfil debe tener todos": {
        "es": "El perfil debe tener todos", "en": "The profile must have all", "pt": "O perfil deve ter todos",
        "fr": "Le profil doit tous les avoir", "de": "Das Profil muss alle enthalten", "it": "Il profilo deve possederli tutti",
        "ja": "プロフィールの必須項目", "ko": "프로필이 모두 갖추어야 함", "zh_Hans": "个人资料必须全部具备",
        "ar": "يجب أن يتضمن الملف جميعها", "ru": "Профиль должен содержать все", "hi": "प्रोफ़ाइल में सभी होने चाहिए"
    },
    "Encuentra empresas por sector, modalidad de trabajo o tipo de reclutador.": {
        "es": "Encuentra empresas por sector, modalidad de trabajo o tipo de reclutador.",
        "en": "Find companies by sector, work modality, or recruiter type.",
        "pt": "Encontre empresas por setor, modalidade de trabalho ou tipo de recrutador.",
        "fr": "Trouvez des entreprises par secteur, modalité de travail ou type de recruteur.",
        "de": "Finden Sie Unternehmen nach Branche, Arbeitsmodell oder Recruiter-Typ.",
        "it": "Trova aziende per settore, modalità di lavoro o tipo di recruiter.",
        "ja": "分野、勤務形態、採用担当者のタイプで企業を検索。",
        "ko": "분야, 근무 방식 또는 채용 담당자 유형별로 기업을 찾으세요.",
        "zh_Hans": "按所属行业、工作模式或招聘者类型精准发现目标企业。",
        "ar": "ابحث عن الشركات حسب القطاع أو نمط العمل أو نوع مسؤول التوظيف.",
        "ru": "Находите компании по отрасли, формату работы или типу рекрутера.",
        "hi": "क्षेत्र, कार्य पद्धति या भर्तीकर्ता प्रकार के आधार पर कंपनियां खोजें।"
    },
    "Escribe para buscar tag (ej: Docker, AWS)...": {
        "es": "Escribe para buscar tag (ej: Docker, AWS)...", "en": "Type to search tag (e.g. Docker, AWS)...",
        "pt": "Digite para buscar tag (ex: Docker, AWS)...", "fr": "Tapez pour rechercher un tag (ex : Docker, AWS)...",
        "de": "Tippen, um Tag zu suchen (z.B. Docker, AWS)...", "it": "Scrivi per cercare tag (es: Docker, AWS)...",
        "ja": "入力してタグを検索 (例: Docker, AWS)...", "ko": "태그 검색을 위해 입력 (예: Docker, AWS)...",
        "zh_Hans": "输入以搜索标签 (例: Docker, AWS)...", "ar": "اكتب للبحث عن وسم (مثل: Docker, AWS)...",
        "ru": "Введите для поиска тега (напр. Docker, AWS)...", "hi": "टैग खोजने के लिए टाइप करें (उदा: Docker, AWS)..."
    },
    "Escribe para buscar tag (ej: Python, React)...": {
        "es": "Escribe para buscar tag (ej: Python, React)...", "en": "Type to search tag (e.g. Python, React)...",
        "pt": "Digite para buscar tag (ex: Python, React)...", "fr": "Tapez pour rechercher un tag (ex : Python, React)...",
        "de": "Tippen, um Tag zu suchen (z.B. Python, React)...", "it": "Scrivi per cercare tag (es: Python, React)...",
        "ja": "入力してタグを検索 (例: Python, React)...", "ko": "태그 검색을 위해 입력 (예: Python, React)...",
        "zh_Hans": "输入以搜索标签 (例: Python, React)...", "ar": "اكتب للبحث عن وسم (مثل: Python, React)...",
        "ru": "Введите для поиска тега (напр. Python, React)...", "hi": "टैग खोजने के लिए टाइप करें (उदा: Python, React)..."
    },
    "Explora perfiles verificados con taxonomía de precisión, habilidades reales y contacto directo.": {
        "es": "Explora perfiles verificados con taxonomía de precisión, habilidades reales y contacto directo.",
        "en": "Explore verified profiles with precision taxonomy, real skills, and direct contact.",
        "pt": "Explore perfis verificados com taxonomia de precisão, habilidades reais e contato direto.",
        "fr": "Explorez des profils vérifiés avec une taxonomie de précision, des compétences réelles et un contact direct.",
        "de": "Erkunden Sie verifizierte Profile mit Präzisions-Taxonomie, echten Fähigkeiten und direktem Kontakt.",
        "it": "Esplora profili verificati con tassonomia di precisione, competenze reali e contatto diretto.",
        "ja": "高精度分類、実証されたスキル、直接コンタクトを備えた確認済みプロフィールを検索。",
        "ko": "정밀한 분류 체계, 검증된 역량, 직접 연락이 가능한 프로필을 탐색하세요.",
        "zh_Hans": "探索具备高精度结构化分类、实战技能与直接联络通道的真实人才主页。",
        "ar": "استكشف ملفات تم التحقق منها بتصنيف دقيق ومهارات حقيقية وتواصل مباشر.",
        "ru": "Исследуйте проверенные профили с точной таксономией, реальными навыками и прямым контактом.",
        "hi": "सटीक वर्गीकरण, वास्तविक कौशल और सीधे संपर्क के साथ सत्यापित प्रोफाइल का अन्वेषण करें।"
    },
    "Filtra en cascada por Sector, Rol, Especialidad y competencias específicas.": {
        "es": "Filtra en cascada por Sector, Rol, Especialidad y competencias específicas.",
        "en": "Filter down by Sector, Role, Specialty, and specific skills.",
        "pt": "Filtre em cascata por Setor, Cargo, Especialidade e competências específicas.",
        "fr": "Filtrez en cascade par Secteur, Rôle, Spécialité et compétences spécifiques.",
        "de": "Stufenweise filtern nach Branche, Rolle, Spezialisierung und spezifischen Kompetenzen.",
        "it": "Filtra a cascata per Settore, Ruolo, Specializzazione e competenze specifiche.",
        "ja": "分野、役割、専門領域、特定スキルで段階的に絞り込み。",
        "ko": "섹터, 역할, 전문 분야 및 세부 역량별로 단계별 필터링하세요.",
        "zh_Hans": "按行业、角色、专长及特定技能层层级联筛选。",
        "ar": "قم بالتصفية المتتالية حسب القطاع والدور والتخصص والمهارات المحددة.",
        "ru": "Фильтруйте по цепочке: сектор, роль, специальность и конкретные навыки.",
        "hi": "सेक्टर, भूमिका, विशेषता और विशिष्ट दक्षताओं द्वारा फ़िल्टर करें।"
    },
    "Filtros Adicionales (Seniority y Modalidad)": {
        "es": "Filtros Adicionales (Seniority y Modalidad)", "en": "Additional Filters (Seniority and Modality)",
        "pt": "Filtros Adicionais (Senioridade e Modalidade)", "fr": "Filtres Supplémentaires (Séniorité et Modalité)",
        "de": "Zusätzliche Filter (Seniorität und Arbeitsmodell)", "it": "Filtri Aggiuntivi (Seniority e Modalità)",
        "ja": "追加フィルター (経験レベル & 勤務形態)", "ko": "추가 필터 (경력 수준 및 근무 방식)",
        "zh_Hans": "附加筛选条件 (年资级别与工作模式)", "ar": "فلاتر إضافية (الأقدمية ونمط العمل)",
        "ru": "Дополнительные фильтры (Опыт и формат)", "hi": "अतिरिक्त फ़िल्टर (वरिष्ठता और कार्य पद्धति)"
    },
    "Filtros de Búsqueda Taxonómica": {
        "es": "Filtros de Búsqueda Taxonómica", "en": "Taxonomic Search Filters", "pt": "Filtros de Busca Taxonômica",
        "fr": "Filtres de Recherche Taxonomique", "de": "Taxonomische Suchfilter", "it": "Filtri di Ricerca Tassonomica",
        "ja": "分類検索フィルター", "ko": "분류 체계 검색 필터", "zh_Hans": "分类搜索筛选器",
        "ar": "فلاتر البحث التصنيفي", "ru": "Фильтры таксономического поиска", "hi": "वर्गीकरण खोज फ़िल्टर"
    },
    "Filtros de Empresas y Vacantes": {
        "es": "Filtros de Empresas y Vacantes", "en": "Company and Vacancy Filters", "pt": "Filtros de Empresas e Vagas",
        "fr": "Filtres d'Entreprises et de Postes", "de": "Filter für Unternehmen und Stellen", "it": "Filtri Aziende e Posizioni",
        "ja": "企業・求人フィルター", "ko": "기업 및 채용 공고 필터", "zh_Hans": "企业与职位筛选器",
        "ar": "فلاتر الشركات والوظائف", "ru": "Фильтры компаний и вакансий", "hi": "कंपनी और रिक्ति फ़िल्टर"
    },
    "Match": {
        "es": "Match", "en": "Match", "pt": "Match", "fr": "Match",
        "de": "Match", "it": "Match", "ja": "マッチ", "ko": "매치",
        "zh_Hans": "契合度", "ar": "تطابق", "ru": "Мэтч", "hi": "मिलान"
    },
    "Modalidad de Trabajo": {
        "es": "Modalidad de Trabajo", "en": "Work Modality", "pt": "Modalidade de Trabalho",
        "fr": "Modalité de Travail", "de": "Arbeitsmodell", "it": "Modalità di Lavoro",
        "ja": "勤務形態", "ko": "근무 방식", "zh_Hans": "工作模式",
        "ar": "نمط العمل", "ru": "Формат работы", "hi": "कार्य पद्धति"
    },
    "Nivel de Seniority": {
        "es": "Nivel de Seniority", "en": "Seniority Level", "pt": "Nível de Senioridade",
        "fr": "Niveau de Séniorité", "de": "Senioritätsstufe", "it": "Livello di Seniority",
        "ja": "経験・役職レベル", "ko": "경력 수준", "zh_Hans": "年资级别",
        "ar": "مستوى الخبرة", "ru": "Уровень опыта", "hi": "वरिष्ठता स्तर"
    },
    "No se encontraron empresas con estos filtros": {
        "es": "No se encontraron empresas con estos filtros", "en": "No companies found with these filters",
        "pt": "Nenhuma empresa encontrada com estes filtros", "fr": "Aucune entreprise trouvée avec ces filtres",
        "de": "Keine Unternehmen mit diesen Filtern gefunden", "it": "Nessuna azienda trovata con questi filtri",
        "ja": "該当する企業が見つかりませんでした", "ko": "이 필터와 일치하는 기업이 없습니다", "zh_Hans": "未找到符合条件的企业",
        "ar": "لم يتم العثور على شركات بهذه الفلاتر", "ru": "Компании с такими фильтрами не найдены", "hi": "इन फ़िल्टर के साथ कोई कंपनी नहीं मिली"
    },
    "No se encontraron perfiles con estos filtros": {
        "es": "No se encontraron perfiles con estos filtros", "en": "No profiles found with these filters",
        "pt": "Nenhum perfil encontrado com estes filtros", "fr": "Aucun profil trouvé avec ces filtres",
        "de": "Keine Profile mit diesen Filtern gefunden", "it": "Nessun profilo trovato con questi filtri",
        "ja": "該当するプロフィールが見つかりませんでした", "ko": "이 필터와 일치하는 프로필이 없습니다", "zh_Hans": "未找到符合条件的个人资料",
        "ar": "لم يتم العثور على ملفات بهذه الفلاتر", "ru": "Профили с такими фильтрами не найдены", "hi": "इन फ़िल्टर के साथ कोई प्रोफ़ाइल नहीं मिली"
    },
    "Obligatorios / Deseables": {
        "es": "Obligatorios / Deseables", "en": "Required / Nice to have", "pt": "Obrigatórios / Desejáveis",
        "fr": "Obligatoires / Souhaitables", "de": "Erforderlich / Wünschenswert", "it": "Obbligatori / Desiderabili",
        "ja": "必須 / 歓迎", "ko": "필수 / 우대", "zh_Hans": "必须 / 加分",
        "ar": "إلزامي / مرغوب", "ru": "Обязательные / Желательные", "hi": "अनिवार्य / वांछनीय"
    },
    "Para reclutadores (Empresas)": {
        "es": "Para reclutadores (Empresas)", "en": "For recruiters (Companies)", "pt": "Para recrutadores (Empresas)",
        "fr": "Pour les recruteurs (Entreprises)", "de": "Für Recruiter (Unternehmen)", "it": "Per i recruiter (Aziende)",
        "ja": "採用担当者向け (企業)", "ko": "채용 담당자용 (기업)", "zh_Hans": "企业与招聘方大厅",
        "ar": "لمسؤولي التوظيف (الشركات)", "ru": "Для рекрутеров (Компании)", "hi": "भर्तीकर्ताओं के लिए (कंपनियां)"
    },
    "Para trabajadores (Candidatos)": {
        "es": "Para trabajadores (Candidatos)", "en": "For talent (Candidates)", "pt": "Para talentos (Candidatos)",
        "fr": "Pour les talents (Candidats)", "de": "Für Fachkräfte (Kandidaten)", "it": "Per i lavoratori (Candidati)",
        "ja": "求職者向け (タレント)", "ko": "구직자용 (인재)", "zh_Hans": "专业人才求职大厅",
        "ar": "للمرشحين (المواهب)", "ru": "Для кандидатов (Таланты)", "hi": "प्रतिभाओं के लिए (उम्मीदवार)"
    },
    "Prueba relajando algunos criterios de búsqueda o limpiando los filtros para ver más resultados.": {
        "es": "Prueba relajando algunos criterios de búsqueda o limpiando los filtros para ver más resultados.",
        "en": "Try relaxing some search criteria or resetting filters to see more results.",
        "pt": "Tente relaxar alguns critérios de busca ou limpar os filtros para ver mais resultados.",
        "fr": "Essayez d'élargir certains critères de recherche ou d'effacer les filtres pour voir plus de résultats.",
        "de": "Versuchen Sie, einige Kriterien zu lockern oder Filter zurückzusetzen, um mehr Ergebnisse zu sehen.",
        "it": "Prova a rimuovere alcuni criteri di ricerca o a cancellare i filtri per vedere più risultati.",
        "ja": "検索条件を緩和するか、フィルターをリセットして再検索してみてください。",
        "ko": "검색 조건을 완화하거나 필터를 재설정하여 더 많은 결과를 확인해보세요.",
        "zh_Hans": "尝试放宽部分筛选要求或重置筛选条件以浏览更多结果。",
        "ar": "جرب تخفيف بعض معايير البحث أو إعادة ضبط الفلاتر للاطلاع على مزيد من النتائج.",
        "ru": "Попробуйте смягчить критерии поиска или очистить фильтры, чтобы увидеть больше результатов.",
        "hi": "अधिक परिणाम देखने के लिए कुछ खोज मानदंड कम करें या फ़िल्टर रीसेट करें।"
    },
    "Restablecer todos los filtros": {
        "es": "Restablecer todos los filtros", "en": "Reset all filters", "pt": "Redefinir todos os filtros",
        "fr": "Réinitialiser tous les filtres", "de": "Alle Filter zurücksetzen", "it": "Reimposta tutti i filtri",
        "ja": "すべてのフィルターをリセット", "ko": "모든 필터 초기화", "zh_Hans": "重置全部筛选条件",
        "ar": "إعادة ضبط جميع الفلاتر", "ru": "Сбросить все фильтры", "hi": "सभी फ़िल्टर रीसेट करें"
    },
    "Sectores de Contratación": {
        "es": "Sectores de Contratación", "en": "Hiring Sectors", "pt": "Setores de Contratação",
        "fr": "Secteurs de Recrutement", "de": "Einstellungsbranchen", "it": "Settori di Assunzione",
        "ja": "採用分野", "ko": "채용 분야", "zh_Hans": "招聘行业领域",
        "ar": "قطاعات التوظيف", "ru": "Отрасли найма", "hi": "भर्ती क्षेत्र"
    },
    "Sin descripción": {
        "es": "Sin descripción", "en": "No description", "pt": "Sem descrição", "fr": "Aucune description",
        "de": "Keine Beschreibung", "it": "Nessuna descrizione", "ja": "説明なし", "ko": "설명 없음",
        "zh_Hans": "暂无描述", "ar": "بدون وصف", "ru": "Без описания", "hi": "कोई विवरण नहीं"
    },
    "Tags y Tecnologías Clave": {
        "es": "Tags y Tecnologías Clave", "en": "Tags and Key Technologies", "pt": "Tags e Tecnologias-Chave",
        "fr": "Tags et Technologies Clés", "de": "Tags und Schlüsseltechnologien", "it": "Tag e Tecnologie Chiave",
        "ja": "タグと主要テクノロジー", "ko": "태그 및 핵심 기술", "zh_Hans": "标签与核心技术栈",
        "ar": "الوسوم والتقنيات الرئيسية", "ru": "Теги и ключевые технологии", "hi": "टैग और प्रमुख प्रौद्योगिकियां"
    },
    "Todas las especialidades": {
        "es": "Todas las especialidades", "en": "All specialties", "pt": "Todas as especialidades",
        "fr": "Toutes les spécialités", "de": "Alle Spezialisierungen", "it": "Tutte le specializzazioni",
        "ja": "すべての専門領域", "ko": "모든 전문 분야", "zh_Hans": "所有专业方向",
        "ar": "جميع التخصصات", "ru": "Все специальности", "hi": "सभी विशेषताएं"
    },
    "Todas las modalidades": {
        "es": "Todas las modalidades", "en": "All modalities", "pt": "Todas as modalidades",
        "fr": "Toutes les modalités", "de": "Alle Arbeitsmodelle", "it": "Tutte le modalità",
        "ja": "すべての勤務形態", "ko": "모든 근무 형태", "zh_Hans": "所有工作模式",
        "ar": "جميع الأنماط", "ru": "Все форматы", "hi": "सभी पद्धतियां"
    },
    "Todos los niveles": {
        "es": "Todos los niveles", "en": "All levels", "pt": "Todos os níveis",
        "fr": "Tous les niveaux", "de": "Alle Stufen", "it": "Tutti i livelli",
        "ja": "すべてのレベル", "ko": "모든 레벨", "zh_Hans": "所有经验级别",
        "ar": "جميع المستويات", "ru": "Все уровни", "hi": "सभी स्तर"
    },
    "Todos los roles": {
        "es": "Todos los roles", "en": "All roles", "pt": "Todos os cargos",
        "fr": "Tous les rôles", "de": "Alle Rollen", "it": "Tutti i ruoli",
        "ja": "すべての役割", "ko": "모든 역할", "zh_Hans": "所有职位角色",
        "ar": "جميع الأدوار", "ru": "Все роли", "hi": "सभी भूमिकाएं"
    },
    "Todos los sectores": {
        "es": "Todos los sectores", "en": "All sectors", "pt": "Todos os setores",
        "fr": "Tous les secteurs", "de": "Alle Branchen", "it": "Tutti i settori",
        "ja": "すべての分野", "ko": "모든 섹터", "zh_Hans": "所有行业",
        "ar": "جميع القطاعات", "ru": "Все секторы", "hi": "सभी क्षेत्र"
    },
    "Todos los tipos": {
        "es": "Todos los tipos", "en": "All types", "pt": "Todos os tipos",
        "fr": "Tous les types", "de": "Alle Typen", "it": "Tutti i tipi",
        "ja": "すべてのタイプ", "ko": "모든 유형", "zh_Hans": "所有类型",
        "ar": "جميع الأنواع", "ru": "Все типы", "hi": "सभी प्रकार"
    },
    "Ver empresa y vacantes": {
        "es": "Ver empresa y vacantes", "en": "View company and openings", "pt": "Ver empresa e vagas",
        "fr": "Voir l'entreprise et les postes", "de": "Unternehmen und Stellen ansehen", "it": "Vedi azienda e posizioni aperte",
        "ja": "企業と求人情報を見る", "ko": "기업 및 채용 공고 보기", "zh_Hans": "查看企业主页与热招职位",
        "ar": "عرض الشركة والشواغر", "ru": "Смотреть компанию и вакансии", "hi": "कंपनी और रिक्तियां देखें"
    },
    "Ver perfil interactivo": {
        "es": "Ver perfil interactivo", "en": "View interactive profile", "pt": "Ver perfil interativo",
        "fr": "Voir le profil interactif", "de": "Interaktives Profil ansehen", "it": "Visualizza profilo interattivo",
        "ja": "インタラクティブなプロフィールを見る", "ko": "인터랙티브 프로필 보기", "zh_Hans": "查看互动人才主页",
        "ar": "عرض الملف التفاعلي", "ru": "Смотреть интерактивный профиль", "hi": "इंटरैक्टिव प्रोफ़ाइल देखें"
    },
    "empresa encontrada": {
        "es": "empresa encontrada", "en": "company found", "pt": "empresa encontrada",
        "fr": "entreprise trouvée", "de": "Unternehmen gefunden", "it": "azienda trovata",
        "ja": "件の企業が見つかりました", "ko": "개 기업 발견", "zh_Hans": "家企业",
        "ar": "شركة تم العثور عليها", "ru": "компания найдена", "hi": "कंपनी मिली"
    },
    "empresas encontradas": {
        "es": "empresas encontradas", "en": "companies found", "pt": "empresas encontradas",
        "fr": "entreprises trouvées", "de": "Unternehmen gefunden", "it": "aziende trovate",
        "ja": "件の企業が見つかりました", "ko": "개 기업 발견", "zh_Hans": "家企业",
        "ar": "شركات تم العثور عليها", "ru": "компаний найдено", "hi": "कंपनियां मिलीं"
    },
    "más": {
        "es": "más", "en": "more", "pt": "mais", "fr": "de plus",
        "de": "mehr", "it": "altri", "ja": "件", "ko": "개 더보기",
        "zh_Hans": "项", "ar": "المزيد", "ru": "еще", "hi": "और"
    },
    "profesional encontrado": {
        "es": "profesional encontrado", "en": "professional found", "pt": "profissional encontrado",
        "fr": "professionnel trouvé", "de": "Fachkraft gefunden", "it": "professionista trovato",
        "ja": "名のプロフェッショナルが見つかりました", "ko": "명의 전문가 발견", "zh_Hans": "位专业人才",
        "ar": "مهني تم العثور عليه", "ru": "специалист найден", "hi": "पेशेवर मिला"
    },
    "profesionales encontrados": {
        "es": "profesionales encontrados", "en": "professionals found", "pt": "profissionais encontrados",
        "fr": "professionnels trouvés", "de": "Fachkräfte gefunden", "it": "professionisti trovati",
        "ja": "名のプロフェッショナルが見つかりました", "ko": "명의 전문가 발견", "zh_Hans": "位专业人才",
        "ar": "مهنيين تم العثور عليهم", "ru": "специалистов найдено", "hi": "पेशेवर मिले"
    }
}

def apply_wall_translations():
    for lang in LANGUAGES:
        po_path = f"locale/{lang}/LC_MESSAGES/django.po"
        mo_path = f"locale/{lang}/LC_MESSAGES/django.mo"
        if not os.path.exists(po_path):
            continue

        po = polib.pofile(po_path)
        existing = {e.msgid: e for e in po}
        added = 0
        updated = 0

        for msgid, trans in WALL_TRANSLATIONS.items():
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
        print(f"[{lang}] Wall Translations: {added} added, {updated} updated -> saved to {mo_path}")

if __name__ == '__main__':
    apply_wall_translations()
