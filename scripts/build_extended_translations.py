# -*- coding: utf-8 -*-
import os
import polib

LANGUAGES = ['es', 'en', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'zh_Hans', 'ar', 'ru', 'hi']

EXTENDED_DATA = {
    "Agregar tag": {
        "es": "Agregar tag", "en": "Add tag", "pt": "Adicionar tag", "fr": "Ajouter un tag",
        "de": "Tag hinzufügen", "it": "Aggiungi tag", "ja": "タグを追加", "ko": "태그 추가",
        "zh_Hans": "添加标签", "ar": "إضافة وسم", "ru": "Добавить тег", "hi": "टैग जोड़ें"
    },
    "Añadir": {
        "es": "Añadir", "en": "Add", "pt": "Adicionar", "fr": "Ajouter",
        "de": "Hinzufügen", "it": "Aggiungi", "ja": "追加", "ko": "추가",
        "zh_Hans": "添加", "ar": "إضافة", "ru": "Добавить", "hi": "जोड़ें"
    },
    "Buscar o agregar tag (ej: Python, React, Git)...": {
        "es": "Buscar o agregar tag (ej: Python, React, Git)...",
        "en": "Search or add tag (e.g. Python, React, Git)...",
        "pt": "Buscar ou adicionar tag (ex: Python, React, Git)...",
        "fr": "Rechercher ou ajouter un tag (ex : Python, React, Git)...",
        "de": "Tag suchen oder hinzufügen (z.B. Python, React, Git)...",
        "it": "Cerca o aggiungi tag (es: Python, React, Git)...",
        "ja": "タグを検索または追加 (例: Python, React, Git)...",
        "ko": "태그 검색 또는 추가 (예: Python, React, Git)...",
        "zh_Hans": "搜索或添加标签 (例: Python, React, Git)...",
        "ar": "ابحث أو أضف وسمًا (مثل: Python, React, Git)...",
        "ru": "Найти или добавить тег (напр. Python, React, Git)...",
        "hi": "टैग खोजें या जोड़ें (उदा: Python, React, Git)..."
    },
    "Escribe y presiona Enter o haz clic en + para añadir.": {
        "es": "Escribe y presiona Enter o haz clic en + para añadir.",
        "en": "Type and press Enter or click + to add.",
        "pt": "Digite e pressione Enter ou clique em + para adicionar.",
        "fr": "Tapez et appuyez sur Entrée ou cliquez sur + pour ajouter.",
        "de": "Tippen und Enter drücken oder auf + klicken zum Hinzufügen.",
        "it": "Scrivi e premi Invio o clicca su + per aggiungere.",
        "ja": "入力してEnterを押すか、+ をクリックして追加します。",
        "ko": "입력 후 Enter를 누르거나 + 를 클릭하여 추가하세요.",
        "zh_Hans": "输入后按 Enter 或点击 + 添加。",
        "ar": "اكتب واضغط Enter أو انقر على + للإضافة.",
        "ru": "Введите и нажмите Enter или значок + для добавления.",
        "hi": "टाइप करें और Enter दबाएं या जोड़ने के लिए + पर क्लिक करें।"
    },
    "No hay idiomas seleccionados": {
        "es": "No hay idiomas seleccionados", "en": "No languages selected", "pt": "Nenhum idioma selecionado", "fr": "Aucune langue sélectionnée",
        "de": "Keine Sprachen ausgewählt", "it": "Nessuna lingua selezionata", "ja": "選択された言語はありません", "ko": "선택된 언어가 없습니다",
        "zh_Hans": "未选择语言", "ar": "لم يتم تحديد لغات", "ru": "Языки не выбраны", "hi": "कोई भाषा चयनित नहीं"
    },
    "No hay tags seleccionados": {
        "es": "No hay tags seleccionados", "en": "No tags selected", "pt": "Nenhuma tag selecionada", "fr": "Aucun tag sélectionné",
        "de": "Keine Tags ausgewählt", "it": "Nessun tag selezionato", "ja": "選択されたタグはありません", "ko": "선택된 태그가 없습니다",
        "zh_Hans": "未选择标签", "ar": "لم يتم تحديد وسوم", "ru": "Теги не выбраны", "hi": "कोई टैग चयनित नहीं"
    },
    "Nuevo tag": {
        "es": "Nuevo tag", "en": "New tag", "pt": "Nova tag", "fr": "Nouveau tag",
        "de": "Neuer Tag", "it": "Nuovo tag", "ja": "新しいタグ", "ko": "새 태그",
        "zh_Hans": "新标签", "ar": "وسم جديد", "ru": "Новый тег", "hi": "नया टैग"
    },
    "Anterior": {
        "es": "Anterior", "en": "Previous", "pt": "Anterior", "fr": "Précédent",
        "de": "Vorherige", "it": "Precedente", "ja": "前へ", "ko": "이전",
        "zh_Hans": "上一页", "ar": "السابق", "ru": "Предыдущий", "hi": "पिछला"
    },
    "Descripción (opcional)": {
        "es": "Descripción (opcional)", "en": "Description (optional)", "pt": "Descrição (opcional)", "fr": "Description (facultatif)",
        "de": "Beschreibung (optional)", "it": "Descrizione (opzionale)", "ja": "説明 (任意)", "ko": "설명 (선택)",
        "zh_Hans": "描述 (可选)", "ar": "الوصف (اختياري)", "ru": "Описание (необязательно)", "hi": "विवरण (वैकल्पिक)"
    },
    "Deseables (OR)": {
        "es": "Deseables (OR)", "en": "Desirable (OR)", "pt": "Desejáveis (OR)", "fr": "Souhaitables (OU)",
        "de": "Wünschenswert (ODER)", "it": "Desiderabili (OR)", "ja": "望ましい (OR)", "ko": "우대사항 (OR)",
        "zh_Hans": "加分项 (OR)", "ar": "مرغوب (OR)", "ru": "Желательно (ИЛИ)", "hi": "वांछनीय (OR)"
    },
    "Ej: $30,000 - $50,000 MXN mensuales": {
        "es": "Ej: $30,000 - $50,000 MXN mensuales", "en": "Ex: $30,000 - $50,000 MXN monthly", "pt": "Ex: $30.000 - $50.000 MXN mensais",
        "fr": "Ex : 30 000 $ - 50 000 $ MXN par mois", "de": "Bsp.: 30.000 - 50.000 MXN monatlich", "it": "Es: $30.000 - $50.000 MXN al mese",
        "ja": "例: 月額 $30,000 - $50,000 MXN", "ko": "예: 월 30,000 - 50,000 MXN", "zh_Hans": "例: 每月 $30,000 - $50,000 MXN",
        "ar": "مثال: 30,000$ - 50,000$ بيزو مكسيكي شهريًا", "ru": "Пример: 30 000 - 50 000 MXN в месяц", "hi": "उदा: $30,000 - $50,000 MXN मासिक"
    },
    "Ej: Ciudad de México, México": {
        "es": "Ej: Ciudad de México, México", "en": "Ex: Mexico City, Mexico", "pt": "Ex: Cidade do México, México",
        "fr": "Ex : Mexico, Mexique", "de": "Bsp.: Mexiko-Stadt, Mexiko", "it": "Es: Città del Messico, Messico",
        "ja": "例: メキシコシティ、メキシコ", "ko": "예: 멕시코시티, 멕시코", "zh_Hans": "例: 墨西哥城，墨西哥",
        "ar": "مثال: مكسيكو سيتي، المكسيك", "ru": "Пример: Мехико, Мексика", "hi": "उदा: मेक्सिको सिटी, मेक्सिको"
    },
    "Empresa Directa": {
        "es": "Empresa Directa", "en": "Direct Company", "pt": "Empresa Direta", "fr": "Entreprise Directe",
        "de": "Direktes Unternehmen", "it": "Azienda Diretta", "ja": "直接企業", "ko": "직접 채용 기업",
        "zh_Hans": "直聘企业", "ar": "شركة مباشرة", "ru": "Прямой работодатель", "hi": "प्रत्यक्ष कंपनी"
    },
    "Enviar Mensaje": {
        "es": "Enviar Mensaje", "en": "Send Message", "pt": "Enviar Mensagem", "fr": "Envoyer le Message",
        "de": "Nachricht senden", "it": "Invia Messaggio", "ja": "メッセージを送信", "ko": "메시지 보내기",
        "zh_Hans": "发送消息", "ar": "إرسال رسالة", "ru": "Отправить сообщение", "hi": "संदेश भेजें"
    },
    "Escribe tu propuesta o mensaje para el candidato...": {
        "es": "Escribe tu propuesta o mensaje para el candidato...",
        "en": "Write your proposal or message for the candidate...",
        "pt": "Escreva sua proposta ou mensagem para o candidato...",
        "fr": "Écrivez votre proposition ou message pour le candidat...",
        "de": "Schreibe dein Angebot oder deine Nachricht an den Kandidaten...",
        "it": "Scrivi la tua proposta o messaggio per il candidato...",
        "ja": "候補者への提案やメッセージを入力してください...",
        "ko": "후보자에게 제안이나 메시지를 작성하세요...",
        "zh_Hans": "输入您给候选人的提议或消息...",
        "ar": "اكتب اقتراحك أو رسالتك للمرشح...",
        "ru": "Напишите предложение или сообщение для кандидата...",
        "hi": "उम्मीदवार के लिए अपना प्रस्ताव या संदेश लिखें..."
    },
    "Especialidad y Habilidades": {
        "es": "Especialidad y Habilidades", "en": "Specialty and Skills", "pt": "Especialidade e Habilidades", "fr": "Spécialité et Compétences",
        "de": "Fachgebiet und Fähigkeiten", "it": "Specializzazione e Competenze", "ja": "専門とスキル", "ko": "전문 분야 및 기술",
        "zh_Hans": "专业与技能", "ar": "التخصص والمهارات", "ru": "Специализация и навыки", "hi": "विशेषज्ञता और कौशल"
    },
    "Experiencia Laboral": {
        "es": "Experiencia Laboral", "en": "Work Experience", "pt": "Experiência de Trabalho", "fr": "Expérience Professionnelle",
        "de": "Berufserfahrung", "it": "Esperienza Lavorativa", "ja": "職務経験", "ko": "직무 경력",
        "zh_Hans": "工作经历", "ar": "الخبرة المهنية", "ru": "Опыт работы", "hi": "कार्य अनुभव"
    },
    "Ficha de Datos": {
        "es": "Ficha de Datos", "en": "Data Sheet", "pt": "Ficha de Dados", "fr": "Fiche de Données",
        "de": "Datenblatt", "it": "Scheda Dati", "ja": "データシート", "ko": "데이터 시트",
        "zh_Hans": "数据卡片", "ar": "ورقة البيانات", "ru": "Карточка данных", "hi": "डेटा शीट"
    },
    "Filtra perfiles o empresas por sector, especialidades concretas, modalidad de trabajo y más. Encuentra exactamente la combinación que necesitas.": {
        "es": "Filtra perfiles o empresas por sector, especialidades concretas, modalidad de trabajo y más. Encuentra exactamente la combinación que necesitas.",
        "en": "Filter profiles or companies by sector, specific specialties, work modality, and more. Find exactly the combination you need.",
        "pt": "Filtre perfis ou empresas por setor, especialidades concretas, modalidade de trabalho e mais. Encontre exatamente a combinação que você precisa.",
        "fr": "Filtrez les profils ou entreprises par secteur, spécialités, modalité de travail et plus. Trouvez exactement la combinaison dont vous avez besoin.",
        "de": "Filtere Profile oder Unternehmen nach Branche, Spezialisierung, Arbeitsmodus und mehr. Finde genau die passende Kombination.",
        "it": "Filtra profili o aziende per settore, specializzazioni concrete, modalità di lavoro e altro. Trova esattamente la combinazione necessaria.",
        "ja": "業界、専門分野、勤務形態などでプロフィールや企業を絞り込みます。必要な組み合わせを正確に見つけることができます。",
        "ko": "분야, 특정 전문 기술, 근무 형태 등으로 프로필이나 기업을 필터링하세요. 필요한 완벽한 조합을 찾을 수 있습니다.",
        "zh_Hans": "按行业、具体专业领域、工作模式等筛选个人资料或企业。精准找到符合需求的匹配项。",
        "ar": "قم بتصفية الملفات الشخصية أو الشركات حسب القطاع والتخصصات ونمط العمل والمزيد. اعثر بدقة على التوافق المناسب لك.",
        "ru": "Фильтруйте профили или компании по секторам, специализациям, формату работы и др. Найдите именно то сочетание, которое вам нужно.",
        "hi": "क्षेत्र, विशिष्ट विशेषज्ञता, कार्य शैली आदि के आधार पर प्रोफ़ाइल या कंपनियों को फ़िल्टर करें। बिल्कुल सही संयोजन पाएं।"
    },
    "Filtros Avanzados": {
        "es": "Filtros Avanzados", "en": "Advanced Filters", "pt": "Filtros Avançados", "fr": "Filtres Avancés",
        "de": "Erweiterte Filter", "it": "Filtri Avanzati", "ja": "高度なフィルター", "ko": "고급 필터",
        "zh_Hans": "高级筛选", "ar": "تصفية متقدمة", "ru": "Расширенные фильтры", "hi": "उन्नत फ़िल्टर"
    },
    "Haz visible tu potencial": {
        "es": "Haz visible tu potencial", "en": "Make your potential visible", "pt": "Torne seu potencial visível", "fr": "Rendez votre potentiel visible",
        "de": "Mache dein Potenzial sichtbar", "it": "Rendi visibile il tuo potenziale", "ja": "あなたの可能性を可視化する", "ko": "당신의 잠재력을 드러내세요",
        "zh_Hans": "展现你的潜能", "ar": "اجعل إمكاناتك مرئية", "ru": "Раскройте свой потенциал", "hi": "अपनी क्षमता को दृश्यमान बनाएं"
    },
    "Ingresa un requisito por línea": {
        "es": "Ingresa un requisito por línea", "en": "Enter one requirement per line", "pt": "Insira um requisito por linha", "fr": "Entrez une condition par ligne",
        "de": "Eine Anforderung pro Zeile eingeben", "it": "Inserisci un requisito per riga", "ja": "要件を1行につき1つ入力してください", "ko": "한 줄에 하나의 자격요건을 입력하세요",
        "zh_Hans": "每行输入一条要求", "ar": "أدخل شرطًا واحدًا في كل سطر", "ru": "Введите по одному требованию в строке", "hi": "प्रति पंक्ति एक आवश्यकता दर्ज करें"
    },
    "Logo de empresa": {
        "es": "Logo de empresa", "en": "Company logo", "pt": "Logotipo da empresa", "fr": "Logo de l'entreprise",
        "de": "Unternehmenslogo", "it": "Logo dell'azienda", "ja": "会社ロゴ", "ko": "회사 로고",
        "zh_Hans": "企业标志", "ar": "شعار الشركة", "ru": "Логотип компании", "hi": "कंपनी का लोगो"
    },
    "Logo de la empresa": {
        "es": "Logo de la empresa", "en": "Company logo", "pt": "Logotipo da empresa", "fr": "Logo de l'entreprise",
        "de": "Unternehmenslogo", "it": "Logo dell'azienda", "ja": "会社ロゴ", "ko": "회사 로고",
        "zh_Hans": "企业标志", "ar": "شعار الشركة", "ru": "Логотип компании", "hi": "कंपनी का लोगो"
    },
    "Los profesionales exploran ofertas y empresas públicas; los reclutadores gestionan vacantes y contactan directo con los candidatos.": {
        "es": "Los profesionales exploran ofertas y empresas públicas; los reclutadores gestionan vacantes y contactan directo con los candidatos.",
        "en": "Professionals explore public offers and companies; recruiters manage vacancies and contact candidates directly.",
        "pt": "Profissionais exploram vagas e empresas públicas; recrutadores gerenciam vagas e entram em contato direto com candidatos.",
        "fr": "Les professionnels explorent les offres et entreprises publiques ; les recruteurs gèrent les postes et contactent directement les candidats.",
        "de": "Fachkräfte entdecken Angebote und Unternehmen; Recruiter verwalten Stellen und kontaktieren Kandidaten direkt.",
        "it": "I professionisti esplorano offerte e aziende pubbliche; i recruiter gestiscono posizioni e contattano direttamente i candidati.",
        "ja": "専門職は公開された求人や企業を探索し、採用担当者は求人を管理して候補者と直接コンタクトを取ります。",
        "ko": "구직자는 채용 공고와 공개 기업을 탐색하고, 채용 담당자는 공고를 관리하며 인재에게 직접 연락합니다.",
        "zh_Hans": "专业人才探索公开职位与企业；招聘人员管理职位并直接与候选人联系。",
        "ar": "يستكشف المهنيون العروض والشركات العامة؛ ويدير مسؤولو التوظيف الوظائف ويتواصلون مباشرة مع المرشحين.",
        "ru": "Специалисты изучают открытые вакансии и компании; рекрутеры управляют вакансиями и связываются с кандидатами напрямую.",
        "hi": "पेशेवर खुली नौकरियों और कंपनियों की खोज करते हैं; रिक्रूटर्स रिक्तियों का प्रबंधन करते हैं और उम्मीदवारों से सीधा संपर्क करते हैं।"
    },
    "Mis Ofertas / Vacantes": {
        "es": "Mis Ofertas / Vacantes", "en": "My Offers / Vacancies", "pt": "Minhas Ofertas / Vagas", "fr": "Mes Offres / Postes",
        "de": "Meine Angebote / Stellen", "it": "Le Mie Offerte / Posizioni", "ja": "掲載中の求人 / 募集", "ko": "내 채용 공고 / 포지션",
        "zh_Hans": "我的职位 / 招聘", "ar": "عروضي / الوظائف الشاغرة", "ru": "Мои предложения / Вакансии", "hi": "मेरे ऑफ़र / रिक्तियां"
    },
    "Modalidad": {
        "es": "Modalidad", "en": "Modality", "pt": "Modalidade", "fr": "Modalité",
        "de": "Arbeitsmodus", "it": "Modalità", "ja": "勤務形態", "ko": "근무 형태",
        "zh_Hans": "工作模式", "ar": "نمط العمل", "ru": "Формат работы", "hi": "कार्य शैली"
    },
    "Modalidad:": {
        "es": "Modalidad:", "en": "Modality:", "pt": "Modalidade:", "fr": "Modalité :",
        "de": "Arbeitsmodus:", "it": "Modalità:", "ja": "勤務形態:", "ko": "근무 형태:",
        "zh_Hans": "工作模式:", "ar": "نمط العمل:", "ru": "Формат работы:", "hi": "कार्य शैली:"
    },
    "No hay vacantes activas por el momento.": {
        "es": "No hay vacantes activas por el momento.", "en": "There are no active vacancies at the moment.",
        "pt": "Não há vagas ativas no momento.", "fr": "Il n'y a aucun poste actif pour le moment.",
        "de": "Derzeit gibt es keine aktiven Stellenangebote.", "it": "Al momento non ci sono posizioni attive.",
        "ja": "現在募集中の求人はありません。", "ko": "현재 활성화된 채용 공고가 없습니다.",
        "zh_Hans": "目前暂无活跃职位。", "ar": "لا توجد وظائف شاغرة حاليًا.",
        "ru": "В настоящее время активных вакансий нет.", "hi": "इस समय कोई सक्रिय रिक्ति नहीं है।"
    },
    "No se encontraron empresas con estos filtros.": {
        "es": "No se encontraron empresas con estos filtros.", "en": "No companies found with these filters.",
        "pt": "Nenhuma empresa encontrada com esses filtros.", "fr": "Aucune entreprise trouvée avec ces filtres.",
        "de": "Keine Unternehmen mit diesen Filtern gefunden.", "it": "Nessuna azienda trovata con questi filtri.",
        "ja": "該当する条件の企業は見つかりませんでした。", "ko": "해당 조건의 기업을 찾을 수 없습니다.",
        "zh_Hans": "未找到符合筛选条件的企业。", "ar": "لم يتم العثور على شركات وفقًا لهذه الفلاتر.",
        "ru": "Компании с такими фильтрами не найдены.", "hi": "इन फ़िल्टरों के साथ कोई कंपनी नहीं मिली।"
    },
    "No se encontraron perfiles con estos filtros.": {
        "es": "No se encontraron perfiles con estos filtros.", "en": "No profiles found with these filters.",
        "pt": "Nenhum perfil encontrado com esses filtros.", "fr": "Aucun profil trouvé avec ces filtres.",
        "de": "Keine Profile mit diesen Filtern gefunden.", "it": "Nessun profilo trovato con questi filtri.",
        "ja": "該当する条件のプロフィールは見つかりませんでした。", "ko": "해당 조건의 프로필을 찾을 수 없습니다.",
        "zh_Hans": "未找到符合筛选条件的人才资料。", "ar": "لم يتم العثور على ملفات شخصية بهذه الفلاتر.",
        "ru": "Профили с такими фильтрами не найдены.", "hi": "इन फ़िल्टरों के साथ कोई प्रोफ़ाइल नहीं मिली।"
    },
    "No tienes vacantes publicadas": {
        "es": "No tienes vacantes publicadas", "en": "You have no published vacancies",
        "pt": "Você não tem vagas publicadas", "fr": "Vous n'avez aucun poste publié",
        "de": "Du hast keine Stellenangebote veröffentlicht", "it": "Non hai posizioni pubblicate",
        "ja": "公開中の求人はありません", "ko": "게시된 채용 공고가 없습니다",
        "zh_Hans": "您尚未发布职位", "ar": "ليس لديك وظائف منشورة",
        "ru": "У вас нет опубликованных вакансий", "hi": "आपकी कोई प्रकाशित रिक्ति नहीं है"
    },
    "Nota: La funcionalidad de guardado estará disponible próximamente.": {
        "es": "Nota: La funcionalidad de guardado estará disponible próximamente.",
        "en": "Note: Save functionality will be available soon.",
        "pt": "Nota: A funcionalidade de salvar estará disponível em breve.",
        "fr": "Remarque : La fonction de sauvegarde sera bientôt disponible.",
        "de": "Hinweis: Die Speicherfunktion wird in Kürze verfügbar sein.",
        "it": "Nota: La funzionalità di salvataggio sarà disponibile a breve.",
        "ja": "注: 保存機能は近日中に利用可能になります。",
        "ko": "참고: 저장 기능은 곧 제공될 예정입니다.",
        "zh_Hans": "提示: 保存功能即将上线。",
        "ar": "ملاحظة: ستتوفر ميزة الحفظ قريبًا.",
        "ru": "Примечание: Функция сохранения скоро станет доступна.",
        "hi": "नोट: सहेजने की सुविधा जल्द ही उपलब्ध होगी।"
    },
    "Obligatorios (AND)": {
        "es": "Obligatorios (AND)", "en": "Mandatory (AND)", "pt": "Obrigatórios (AND)", "fr": "Obligatoires (ET)",
        "de": "Erforderlich (UND)", "it": "Obbligatori (AND)", "ja": "必須 (AND)", "ko": "필수사항 (AND)",
        "zh_Hans": "必填项 (AND)", "ar": "إلزامي (AND)", "ru": "Обязательно (И)", "hi": "अनिवार्य (AND)"
    },
    "Particular": {
        "es": "Particular", "en": "Individual", "pt": "Particular", "fr": "Particulier",
        "de": "Privat / Einzelperson", "it": "Privato", "ja": "個人", "ko": "개인",
        "zh_Hans": "个人", "ar": "فردي", "ru": "Частное лицо", "hi": "व्यक्तिगत"
    },
    "Paso 1 de 4 – ¿Qué buscas?": {
        "es": "Paso 1 de 4 – ¿Qué buscas?", "en": "Step 1 of 4 – What are you looking for?",
        "pt": "Passo 1 de 4 – O que você procura?", "fr": "Étape 1 sur 4 – Que cherchez-vous ?",
        "de": "Schritt 1 von 4 – Was suchst du?", "it": "Passo 1 di 4 – Cosa cerchi?",
        "ja": "ステップ 1 / 4 – 何をお探しですか？", "ko": "1단계 / 4단계 – 무엇을 찾고 계신가요?",
        "zh_Hans": "第 1 步 / 共 4 步 – 您在寻找什么？", "ar": "الخطوة 1 من 4 – ما الذي تبحث عنه؟",
        "ru": "Шаг 1 из 4 – Что вы ищете?", "hi": "चरण 1 का 4 – आप क्या ढूंढ रहे हैं?"
    },
    "Paso 1 de 4 — ¿Qué buscas?": {
        "es": "Paso 1 de 4 — ¿Qué buscas?", "en": "Step 1 of 4 — What are you looking for?",
        "pt": "Passo 1 de 4 — O que você procura?", "fr": "Étape 1 sur 4 — Que cherchez-vous ?",
        "de": "Schritt 1 von 4 — Was suchst du?", "it": "Passo 1 di 4 — Cosa cerchi?",
        "ja": "ステップ 1 / 4 — 何をお探しですか？", "ko": "1단계 / 4단계 — 무엇을 찾고 계신가요?",
        "zh_Hans": "第 1 步 / 共 4 步 — 您在寻找什么？", "ar": "الخطوة 1 من 4 — ما الذي تبحث عنه؟",
        "ru": "Шаг 1 из 4 — Что вы ищете?", "hi": "चरण 1 का 4 — आप क्या ढूंढ रहे हैं?"
    },
    "Perfiles Interactivos": {
        "es": "Perfiles Interactivos", "en": "Interactive Profiles", "pt": "Perfis Interativos", "fr": "Profils Interactifs",
        "de": "Interaktive Profile", "it": "Profili Interattivi", "ja": "インタラクティブなプロフィール", "ko": "인터랙티브 프로필",
        "zh_Hans": "互动个人档案", "ar": "ملفات شخصية تفاعلية", "ru": "Интерактивные профили", "hi": "इंटरैक्टिव प्रोफाइल"
    },
    "Preferencias de Trabajo": {
        "es": "Preferencias de Trabajo", "en": "Work Preferences", "pt": "Preferências de Trabalho", "fr": "Préférences de Travail",
        "de": "Arbeitspräferenzen", "it": "Preferenze di Lavoro", "ja": "勤務の希望条件", "ko": "근무 선호사항",
        "zh_Hans": "求职意向与偏好", "ar": "تفضيلات العمل", "ru": "Предпочтения по работе", "hi": "कार्य प्राथमिकताएं"
    },
    "Presenta tu experiencia, seniority, disponibilidad y red de habilidades en una página pública optimizada para compartir.": {
        "es": "Presenta tu experiencia, seniority, disponibilidad y red de habilidades en una página pública optimizada para compartir.",
        "en": "Showcase your experience, seniority, availability, and skill network on a public page optimized for sharing.",
        "pt": "Apresente sua experiência, senioridade, disponibilidade e habilidades em uma página pública otimizada para compartilhamento.",
        "fr": "Présentez votre expérience, séniorité, disponibilité et réseau de compétences sur une page publique optimisée pour le partage.",
        "de": "Präsentiere deine Erfahrung, Seniorität, Verfügbarkeit und Fähigkeiten auf einer für das Teilen optimierten öffentlichen Seite.",
        "it": "Presenta la tua esperienza, livello, disponibilità e competenze su una pagina pubblica ottimizzata per la condivisione.",
        "ja": "共有に最適化された公開ページで、経験、シニアレベル、稼働可能性、スキルを提示できます。",
        "ko": "공유에 최적화된 공개 페이지에서 경력, 시니어 레벨, 가능 일정, 보유 기술을 한눈에 보여주세요.",
        "zh_Hans": "在专为分享优化的公开主页上，展示您的经验、资历、可到岗时间和技能网络。",
        "ar": "اعرض خبراتك ومستواك وتوافرك وشبكة مهاراتك في صفحة عامة مُحسّنة للمشاركة.",
        "ru": "Представьте свой опыт, уровень, доступность и навыки на публичной странице, оптимизированной для шеринга.",
        "hi": "साझा करने के लिए अनुकूलित सार्वजनिक पृष्ठ पर अपना अनुभव, स्तर, उपलब्धता और कौशल प्रस्तुत करें।"
    },
    "Proyectos Destacados": {
        "es": "Proyectos Destacados", "en": "Featured Projects", "pt": "Projetos em Destaque", "fr": "Projets Phares",
        "de": "Hervorgehobene Projekte", "it": "Progetti in Evidenza", "ja": "注目のプロジェクト", "ko": "주요 프로젝트",
        "zh_Hans": "重点项目", "ar": "مشاريع مميزة", "ru": "Избранные проекты", "hi": "प्रमुख परियोजनाएं"
    },
    "Rango salarial": {
        "es": "Rango salarial", "en": "Salary range", "pt": "Faixa salarial", "fr": "Fourchette salariale",
        "de": "Gehaltsspanne", "it": "Fascia retributiva", "ja": "給与レンジ", "ko": "급여 범위",
        "zh_Hans": "薪资范围", "ar": "نطاق الراتب", "ru": "Диапазон зарплат", "hi": "वेतन सीमा"
    },
    "Reclutador": {
        "es": "Reclutador", "en": "Recruiter", "pt": "Recrutador", "fr": "Recruteur",
        "de": "Recruiter", "it": "Recruiter", "ja": "採用担当者", "ko": "채용 담당자",
        "zh_Hans": "招聘顾问", "ar": "مسؤول توظيف", "ru": "Рекрутер", "hi": "भर्तीकर्ता"
    },
    "Reclutador Independiente": {
        "es": "Reclutador Independiente", "en": "Independent Recruiter", "pt": "Recrutador Independente", "fr": "Recruteur Indépendant",
        "de": "Unabhängiger Recruiter", "it": "Recruiter Indipendente", "ja": "独立系採用担当者", "ko": "프리랜서 채용 담당자",
        "zh_Hans": "独立猎头/招聘顾问", "ar": "مسؤول توظيف مستقل", "ru": "Независимый рекрутер", "hi": "स्वतंत्र भर्तीकर्ता"
    },
    "Redes Sociales y Portafolio": {
        "es": "Redes Sociales y Portafolio", "en": "Social Links and Portfolio", "pt": "Redes Sociais e Portfólio", "fr": "Réseaux Sociaux et Portfolio",
        "de": "Soziale Netzwerke & Portfolio", "it": "Social Network e Portfolio", "ja": "SNS・ポートフォリオ", "ko": "소셜 미디어 및 포트폴리오",
        "zh_Hans": "社交网络与作品集", "ar": "التواصل الاجتماعي والملف المهني", "ru": "Соцсети и портфолио", "hi": "सोशल मीडिया और पोर्टफोलियो"
    },
    "Redes y Enlaces": {
        "es": "Redes y Enlaces", "en": "Links and Social Media", "pt": "Redes e Links", "fr": "Réseaux et Liens",
        "de": "Netzwerke und Links", "it": "Reti e Collegamenti", "ja": "リンクとSNS", "ko": "소셜 링크",
        "zh_Hans": "网络与链接", "ar": "الشبكات والروابط", "ru": "Ссылки и соцсети", "hi": "नेटवर्क और लिंक"
    },
    "Requisitos": {
        "es": "Requisitos", "en": "Requirements", "pt": "Requisitos", "fr": "Conditions requises",
        "de": "Anforderungen", "it": "Requisiti", "ja": "必要条件", "ko": "자격 요건",
        "zh_Hans": "职位要求", "ar": "المتطلبات", "ru": "Требования", "hi": "आवश्यकताएं"
    },
    "Sin enlaces externos configurados.": {
        "es": "Sin enlaces externos configurados.", "en": "No external links configured.", "pt": "Nenhum link externo configurado.",
        "fr": "Aucun lien externe configuré.", "de": "Keine externen Links eingerichtet.", "it": "Nessun collegamento esterno configurato.",
        "ja": "設定された外部リンクはありません。", "ko": "설정된 외부 링크가 없습니다.", "zh_Hans": "未配置外部链接。",
        "ar": "لا توجد روابط خارجية مهيأة.", "ru": "Внешние ссылки не настроены.", "hi": "कोई बाहरी लिंक कॉन्फ़िगर नहीं है।"
    },
    "Sitio Web (opcional)": {
        "es": "Sitio Web (opcional)", "en": "Website (optional)", "pt": "Website (opcional)", "fr": "Site web (facultatif)",
        "de": "Website (optional)", "it": "Sito Web (opzionale)", "ja": "ウェブサイト (任意)", "ko": "웹사이트 (선택)",
        "zh_Hans": "网站 (可选)", "ar": "الموقع الإلكتروني (اختياري)", "ru": "Веб-сайт (необязательно)", "hi": "वेबसाइट (वैकल्पिक)"
    },
    "Sitio Web:": {
        "es": "Sitio Web:", "en": "Website:", "pt": "Website:", "fr": "Site web :",
        "de": "Website:", "it": "Sito Web:", "ja": "ウェブサイト:", "ko": "웹사이트:",
        "zh_Hans": "网站:", "ar": "الموقع الإلكتروني:", "ru": "Веб-сайт:", "hi": "वेबसाइट:"
    },
    "Sobre Nosotros": {
        "es": "Sobre Nosotros", "en": "About Us", "pt": "Sobre Nós", "fr": "À Propos de Nous",
        "de": "Über uns", "it": "Chi Siamo", "ja": "私たちについて", "ko": "회사 소개",
        "zh_Hans": "关于我们", "ar": "من نحن", "ru": "О нас", "hi": "हमारे बारे में"
    },
    "Tablón de Empresas": {
        "es": "Tablón de Empresas", "en": "Companies Board", "pt": "Quadro de Empresas", "fr": "Tableau des Entreprises",
        "de": "Unternehmens-Board", "it": "Bacheca Aziende", "ja": "企業ボード", "ko": "기업 게시판",
        "zh_Hans": "企业展板", "ar": "لوحة الشركات", "ru": "Доска компаний", "hi": "कंपनी बोर्ड"
    },
    "Tags (Opcionales)": {
        "es": "Tags (Opcionales)", "en": "Tags (Optional)", "pt": "Tags (Opcionais)", "fr": "Tags (Facultatif)",
        "de": "Tags (Optional)", "it": "Tag (Opzionali)", "ja": "タグ (任意)", "ko": "태그 (선택)",
        "zh_Hans": "标签 (可选)", "ar": "الوسوم (اختياري)", "ru": "Теги (необязательно)", "hi": "टैग (वैकल्पिक)"
    },
    "Tecnologías": {
        "es": "Tecnologías", "en": "Technologies", "pt": "Tecnologias", "fr": "Technologies",
        "de": "Technologien", "it": "Tecnologie", "ja": "使用技術", "ko": "기술 스택",
        "zh_Hans": "技能技术", "ar": "التقنيات", "ru": "Технологии", "hi": "प्रौद्योगिकियां"
    },
    "Tipo de Empresa": {
        "es": "Tipo de Empresa", "en": "Company Type", "pt": "Tipo de Empresa", "fr": "Type d'Entreprise",
        "de": "Unternehmenstyp", "it": "Tipo di Azienda", "ja": "企業タイプ", "ko": "기업 형태",
        "zh_Hans": "企业性质", "ar": "نوع الشركة", "ru": "Тип компании", "hi": "कंपनी का प्रकार"
    },
    "Tipo de Reclutador": {
        "es": "Tipo de Reclutador", "en": "Recruiter Type", "pt": "Tipo de Recrutador", "fr": "Type de Recruteur",
        "de": "Recruiter-Typ", "it": "Tipo di Recruiter", "ja": "採用担当タイプ", "ko": "채용 담당자 유형",
        "zh_Hans": "招聘人类型", "ar": "نوع مسؤول التوظيف", "ru": "Тип рекрутера", "hi": "भर्तीकर्ता प्रकार"
    },
    "Tipo:": {
        "es": "Tipo:", "en": "Type:", "pt": "Tipo:", "fr": "Type :",
        "de": "Typ:", "it": "Tipo:", "ja": "タイプ:", "ko": "유형:",
        "zh_Hans": "类型:", "ar": "النوع:", "ru": "Тип:", "hi": "प्रकार:"
    },
    "Todas": {
        "es": "Todas", "en": "All", "pt": "Todas", "fr": "Toutes",
        "de": "Alle", "it": "Tutte", "ja": "すべて", "ko": "전체",
        "zh_Hans": "全部", "ar": "الكل", "ru": "Все", "hi": "सभी"
    },
    "Trayectoria laboral y proyectos destacados": {
        "es": "Trayectoria laboral y proyectos destacados", "en": "Work history and featured projects",
        "pt": "Trajetória profissional e projetos em destaque", "fr": "Parcours professionnel et projets phares",
        "de": "Beruflicher Werdegang und ausgewählte Projekte", "it": "Percorso professionale e progetti in evidenza",
        "ja": "職歴と注目のプロジェクト", "ko": "업무 이력 및 주요 프로젝트",
        "zh_Hans": "工作轨迹与精选项目", "ar": "المسيرة المهنية والمشاريع المميزة",
        "ru": "Трудовой путь и ключевые проекты", "hi": "कार्य इतिहास और प्रमुख परियोजनाएं"
    },
    "Ubicación:": {
        "es": "Ubicación:", "en": "Location:", "pt": "Localização:", "fr": "Emplacement :",
        "de": "Standort:", "it": "Posizione:", "ja": "所在地:", "ko": "위치:",
        "zh_Hans": "地点:", "ar": "الموقع:", "ru": "Местоположение:", "hi": "स्थान:"
    },
    "Un espacio doble": {
        "es": "Un espacio doble", "en": "A double space", "pt": "Um espaço duplo", "fr": "Un double espace",
        "de": "Ein doppelter Raum", "it": "Un doppio spazio", "ja": "2つのスペース", "ko": "두 개의 공간",
        "zh_Hans": "双重空间", "ar": "مساحة مزدوجة", "ru": "Двойное пространство", "hi": "एक दोहरा स्थान"
    },
    "Un requisito por línea...": {
        "es": "Un requisito por línea...", "en": "One requirement per line...", "pt": "Um requisito por linha...", "fr": "Une condition par ligne...",
        "de": "Eine Anforderung pro Zeile...", "it": "Un requisito per riga...", "ja": "1行につき1つの要件...", "ko": "한 줄에 하나의 자격 요건...",
        "zh_Hans": "每行一个要求...", "ar": "شرط واحد لكل سطر...", "ru": "Одно требование на строку...", "hi": "प्रति पंक्ति एक आवश्यकता..."
    },
    "Vacantes Activas": {
        "es": "Vacantes Activas", "en": "Active Vacancies", "pt": "Vagas Ativas", "fr": "Postes Actifs",
        "de": "Aktive Stellen", "it": "Posizioni Attive", "ja": "募集中の求人", "ko": "진행 중인 채용 공고",
        "zh_Hans": "活跃职位", "ar": "الوظائف النشطة", "ru": "Активные вакансии", "hi": "सक्रिय रिक्तियां"
    },
    "Ver proyecto": {
        "es": "Ver proyecto", "en": "View project", "pt": "Ver projeto", "fr": "Voir le projet",
        "de": "Projekt ansehen", "it": "Vedi progetto", "ja": "プロジェクトを見る", "ko": "프로젝트 보기",
        "zh_Hans": "查看项目", "ar": "عرض المشروع", "ru": "Смотреть проект", "hi": "परियोजना देखें"
    },
    "Vista previa: así es como los reclutadores y empresas ven tu perfil público.": {
        "es": "Vista previa: así es como los reclutadores y empresas ven tu perfil público.",
        "en": "Preview: this is how recruiters and companies see your public profile.",
        "pt": "Pré-visualização: é assim que recrutadores e empresas veem seu perfil público.",
        "fr": "Aperçu : voici comment les recruteurs et entreprises voient votre profil public.",
        "de": "Vorschau: So sehen Recruiter und Unternehmen dein öffentliches Profil.",
        "it": "Anteprima: ecco come i recruiter e le aziende vedono il tuo profilo pubblico.",
        "ja": "プレビュー: 採用担当者や企業にはこのように公開プロフィールが表示されます。",
        "ko": "미리보기: 채용 담당자와 기업에게 공개 프로필이 이렇게 표시됩니다.",
        "zh_Hans": "预览：这是招聘人员和企业查看您公开主页的样式。",
        "ar": "معاينة: هكذا يرى مسؤولو التوظيف والشركات ملفك الشخصي العام.",
        "ru": "Предпросмотр: так рекрутеры и компании видят ваш публичный профиль.",
        "hi": "पूर्वावलोकन: रिक्रूटर्स और कंपनियाँ आपकी सार्वजनिक प्रोफ़ाइल को इस प्रकार देखते हैं।"
    },
    "candidatos": {
        "es": "candidatos", "en": "candidates", "pt": "candidatos", "fr": "candidats",
        "de": "Kandidaten", "it": "candidati", "ja": "候補者", "ko": "후보자",
        "zh_Hans": "候选人", "ar": "مرشحين", "ru": "кандидатов", "hi": "उम्मीदवार"
    },
    "tu@empresa.com": {
        "es": "tu@empresa.com", "en": "you@company.com", "pt": "voce@empresa.com", "fr": "vous@entreprise.com",
        "de": "du@unternehmen.de", "it": "tu@azienda.it", "ja": "you@company.com", "ko": "you@company.com",
        "zh_Hans": "you@company.com", "ar": "you@company.com", "ru": "you@company.com", "hi": "you@company.com"
    },
    "Sin biografía disponible": {
        "es": "Sin biografía disponible", "en": "No bio available", "pt": "Sem biografia disponível", "fr": "Aucune biographie disponible",
        "de": "Keine Biografie verfügbar", "it": "Nessuna biografia disponibile", "ja": "自己紹介はありません", "ko": "등록된 소개가 없습니다",
        "zh_Hans": "暂无简介", "ar": "لا توجد سيرة ذاتية متاحة", "ru": "Биография отсутствует", "hi": "कोई बायो उपलब्ध नहीं"
    },
    "Contactar con Candidato": {
        "es": "Contactar con Candidato", "en": "Contact Candidate", "pt": "Contatar Candidato", "fr": "Contacter le Candidat",
        "de": "Kandidat kontaktieren", "it": "Contatta Candidato", "ja": "候補者に連絡する", "ko": "후보자에게 연락하기",
        "zh_Hans": "联系候选人", "ar": "التواصل مع المرشح", "ru": "Связаться с кандидатом", "hi": "उम्मीदवार से संपर्क करें"
    },
    "Contactar a": {
        "es": "Contactar a", "en": "Contact", "pt": "Contatar", "fr": "Contacter",
        "de": "Kontaktieren:", "it": "Contatta", "ja": "連絡先:", "ko": "연락 대상:",
        "zh_Hans": "联系", "ar": "التواصل مع", "ru": "Связаться с", "hi": "संपर्क करें"
    },
    "Tu nombre": {
        "es": "Tu nombre", "en": "Your name", "pt": "Seu nome", "fr": "Votre nom",
        "de": "Dein Name", "it": "Il tuo nome", "ja": "氏名", "ko": "이름",
        "zh_Hans": "您的姓名", "ar": "اسمك", "ru": "Ваше имя", "hi": "आपका नाम"
    },
    "Nombre y apellidos": {
        "es": "Nombre y apellidos", "en": "Full name", "pt": "Nome completo", "fr": "Nom et prénom",
        "de": "Vor- und Nachname", "it": "Nome e cognome", "ja": "氏名（フルネーム）", "ko": "성명",
        "zh_Hans": "姓名", "ar": "الاسم الكامل", "ru": "Имя и фамилия", "hi": "पूरा नाम"
    },
    "Tu email": {
        "es": "Tu email", "en": "Your email", "pt": "Seu e-mail", "fr": "Votre e-mail",
        "de": "Deine E-Mail", "it": "La tua email", "ja": "メールアドレス", "ko": "이메일",
        "zh_Hans": "您的电子邮箱", "ar": "بريدك الإلكتروني", "ru": "Ваш email", "hi": "आपका ईमेल"
    },
    "Mensaje": {
        "es": "Mensaje", "en": "Message", "pt": "Mensagem", "fr": "Message",
        "de": "Nachricht", "it": "Messaggio", "ja": "メッセージ", "ko": "메시지",
        "zh_Hans": "留言内容", "ar": "الرسالة", "ru": "Сообщение", "hi": "संदेश"
    },
    "Tipo de empleo:": {
        "es": "Tipo de empleo:", "en": "Employment type:", "pt": "Tipo de emprego:", "fr": "Type d'emploi :",
        "de": "Beschäftigungsart:", "it": "Tipo di impiego:", "ja": "雇用形態:", "ko": "고용 형태:",
        "zh_Hans": "工作类型:", "ar": "نوع التوظيف:", "ru": "Тип занятости:", "hi": "रोजगार प्रकार:"
    },
    "Disponible para mudarse:": {
        "es": "Disponible para mudarse:", "en": "Willing to relocate:", "pt": "Disponível para mudança:", "fr": "Prêt à déménager :",
        "de": "Umzugsbereit:", "it": "Disponibile al trasferimento:", "ja": "転勤・移住可能:", "ko": "이직/거주 이전 가능 여부:",
        "zh_Hans": "愿意外派迁移:", "ar": "مستعد للانتقال:", "ru": "Готовность к переезду:", "hi": "स्थानांतरण के लिए तैयार:"
    },
    "Disponible para viajar:": {
        "es": "Disponible para viajar:", "en": "Travel availability:", "pt": "Disponível para viajar:", "fr": "Prêt à voyager :",
        "de": "Reisebereitschaft:", "it": "Disponibile a viaggiare:", "ja": "出張可能:", "ko": "출장 가능 여부:",
        "zh_Hans": "出差意愿:", "ar": "مستعد للسفر:", "ru": "Готовность к командировкам:", "hi": "यात्रा के लिए उपलब्ध:"
    },
    "Ir al Dashboard": {
        "es": "Ir al Dashboard", "en": "Go to Dashboard", "pt": "Ir para o Dashboard", "fr": "Aller au Tableau de Bord",
        "de": "Zum Dashboard gehen", "it": "Vai alla Dashboard", "ja": "ダッシュボードへ戻る", "ko": "대시보드로 이동",
        "zh_Hans": "返回仪表盘", "ar": "الذهاب إلى لوحة التحكم", "ru": "В панель управления", "hi": "डैशबोर्ड पर जाएं"
    },
    "Perfil Profesional": {
        "es": "Perfil Profesional", "en": "Professional Profile", "pt": "Perfil Profissional", "fr": "Profil Professionnel",
        "de": "Berufliches Profil", "it": "Profilo Professionale", "ja": "プロフェッショナル プロフィール", "ko": "전문가 프로필",
        "zh_Hans": "专业人才主页", "ar": "الملف المهني", "ru": "Профессиональный профиль", "hi": "व्यावसायिक प्रोफ़ाइल"
    },
}

try:
    from scripts.build_landing_translations import LANDING_TRANSLATIONS
    EXTENDED_DATA.update(LANDING_TRANSLATIONS)
except ImportError:
    try:
        from build_landing_translations import LANDING_TRANSLATIONS
        EXTENDED_DATA.update(LANDING_TRANSLATIONS)
    except ImportError:
        pass

try:
    from scripts.build_wall_translations import WALL_TRANSLATIONS
    EXTENDED_DATA.update(WALL_TRANSLATIONS)
except ImportError:
    try:
        from build_wall_translations import WALL_TRANSLATIONS
        EXTENDED_DATA.update(WALL_TRANSLATIONS)
    except ImportError:
        pass

def apply_extended():
    for lang in LANGUAGES:
        po_path = f"locale/{lang}/LC_MESSAGES/django.po"
        mo_path = f"locale/{lang}/LC_MESSAGES/django.mo"
        if not os.path.exists(po_path):
            continue

        po = polib.pofile(po_path)
        existing = {e.msgid: e for e in po}
        added = 0
        updated = 0

        for msgid, trans in EXTENDED_DATA.items():
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
        print(f"[{lang}] Extended: {added} added, {updated} updated -> saved to {mo_path}")

if __name__ == '__main__':
    apply_extended()
