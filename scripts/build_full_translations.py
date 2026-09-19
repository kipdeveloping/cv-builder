# -*- coding: utf-8 -*-
import os
import polib

LANGUAGES = ['es', 'en', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'zh_Hans', 'ar', 'ru', 'hi']

# Dictionary of translations for all critical missing/fuzzy strings across all 12 languages
DATA = {
    "Mis Habilidades": {
        "es": "Mis Habilidades", "en": "My Skills", "pt": "Minhas Habilidades", "fr": "Mes Compétences",
        "de": "Meine Fähigkeiten", "it": "Le Mie Competenze", "ja": "マイスキル", "ko": "내 기술",
        "zh_Hans": "我的技能", "ar": "مهاراتي", "ru": "Мои навыки", "hi": "मेरे कौशल"
    },
    "Editar estado": {
        "es": "Editar estado", "en": "Edit status", "pt": "Editar status", "fr": "Modifier le statut",
        "de": "Status bearbeiten", "it": "Modifica stato", "ja": "ステータスを編集", "ko": "상태 수정",
        "zh_Hans": "编辑状态", "ar": "تعديل الحالة", "ru": "Редактировать статус", "hi": "स्थिति संपादित करें"
    },
    "Experiencia y Proyectos": {
        "es": "Experiencia y Proyectos", "en": "Experience and Projects", "pt": "Experiência e Projetos", "fr": "Expérience et Projets",
        "de": "Erfahrung und Projekte", "it": "Esperienza e Progetti", "ja": "職歴とプロジェクト", "ko": "경력 및 프로젝트",
        "zh_Hans": "经历与项目", "ar": "الخبرات والمشاريع", "ru": "Опыт и проекты", "hi": "अनुभव और परियोजनाएं"
    },
    "Perfil público": {
        "es": "Perfil público", "en": "Public profile", "pt": "Perfil público", "fr": "Profil public",
        "de": "Öffentliches Profil", "it": "Profilo pubblico", "ja": "公開プロフィール", "ko": "공개 프로필",
        "zh_Hans": "公开个人资料", "ar": "الملف الشخصي العام", "ru": "Публичный профиль", "hi": "सार्वजनिक प्रोफ़ाइल"
    },
    "Perfil publico": {
        "es": "Perfil público", "en": "Public profile", "pt": "Perfil público", "fr": "Profil public",
        "de": "Öffentliches Profil", "it": "Profilo pubblico", "ja": "公開プロフィール", "ko": "공개 프로필",
        "zh_Hans": "公开个人资料", "ar": "الملف الشخصي العام", "ru": "Публичный профиль", "hi": "सार्वजनिक प्रोफ़ाइल"
    },
    "Activa para que tu perfil sea visible en el tablón": {
        "es": "Activa para que tu perfil sea visible en el tablón",
        "en": "Enable so your profile is visible on the board",
        "pt": "Ative para que seu perfil fique visível no quadro",
        "fr": "Activez pour que votre profil soit visible sur le tableau",
        "de": "Aktivieren, damit dein Profil auf der Pinnwand sichtbar ist",
        "it": "Attiva per rendere visibile il tuo profilo sulla bacheca",
        "ja": "ボードでプロフィールを公開するには有効にしてください",
        "ko": "게시판에 프로필이 표시되도록 활성화하세요",
        "zh_Hans": "开启后个人资料将在展示板上可见",
        "ar": "فعّل ليظهر ملفك الشخصي في اللوحة",
        "ru": "Включите, чтобы профиль отображался на доске",
        "hi": "बोर्ड पर अपनी प्रोफ़ाइल दिखाने के लिए सक्रिय करें"
    },
    "Debes subir una foto de perfil para hacer tu perfil público.": {
        "es": "Debes subir una foto de perfil para hacer tu perfil público.",
        "en": "You must upload a profile photo to make your profile public.",
        "pt": "Você deve enviar uma foto de perfil para tornar seu perfil público.",
        "fr": "Vous devez télécharger une photo de profil pour rendre votre profil public.",
        "de": "Du musst ein Profilbild hochladen, um dein Profil öffentlich zu machen.",
        "it": "Devi caricare una foto del profilo per renderlo pubblico.",
        "ja": "プロフィールを公開するにはプロフィール写真をアップロードする必要があります。",
        "ko": "프로필을 공개하려면 프로필 사진을 업로드해야 합니다.",
        "zh_Hans": "必须上传个人头像才能公开资料。",
        "ar": "يجب تحميل صورة للملف الشخصي لجعله عامًا.",
        "ru": "Загрузите фото профиля, чтобы сделать его публичным.",
        "hi": "प्रोफ़ाइल सार्वजनिक करने के लिए फ़ोटो अपलोड करना आवश्यक है।"
    },
    "Debes subir una foto de perfil para hacer tu perfil publico.": {
        "es": "Debes subir una foto de perfil para hacer tu perfil público.",
        "en": "You must upload a profile photo to make your profile public.",
        "pt": "Você deve enviar uma foto de perfil para tornar seu perfil público.",
        "fr": "Vous devez télécharger une photo de profil pour rendre votre profil public.",
        "de": "Du musst ein Profilbild hochladen, um dein Profil öffentlich zu machen.",
        "it": "Devi caricare una foto del profilo per renderlo pubblico.",
        "ja": "プロフィールを公開するにはプロフィール写真をアップロードする必要があります。",
        "ko": "프로필을 공개하려면 프로필 사진을 업로드해야 합니다.",
        "zh_Hans": "必须上传个人头像才能公开资料。",
        "ar": "يجب تحميل صورة للملف الشخصي لجعله عامًا.",
        "ru": "Загрузите фото профиля, чтобы сделать его публичным.",
        "hi": "प्रोफ़ाइल सार्वजनिक करने के लिए फ़ोटो अपलोड करना आवश्यक है।"
    },
    "Sin titular": {
        "es": "Sin titular", "en": "No headline", "pt": "Sem título", "fr": "Sans titre",
        "de": "Keine Berufsbezeichnung", "it": "Nessun titolo", "ja": "肩書なし", "ko": "한 줄 소개 없음",
        "zh_Hans": "暂无头衔", "ar": "بدون عنوان", "ru": "Без заголовка", "hi": "कोई शीर्षक नहीं"
    },
    "Sin biografia": {
        "es": "Sin biografía", "en": "No bio available", "pt": "Sem biografia", "fr": "Aucune biographie",
        "de": "Keine Biografie", "it": "Nessuna biografia", "ja": "自己紹介なし", "ko": "자기소개 없음",
        "zh_Hans": "暂无简介", "ar": "لا توجد سيرة ذاتية", "ru": "Биография не указана", "hi": "कोई बायो उपलब्ध नहीं"
    },
    "Sin biografía": {
        "es": "Sin biografía", "en": "No bio available", "pt": "Sem biografia", "fr": "Aucune biographie",
        "de": "Keine Biografie", "it": "Nessuna biografia", "ja": "自己紹介なし", "ko": "자기소개 없음",
        "zh_Hans": "暂无简介", "ar": "لا توجد سيرة ذاتية", "ru": "Биография не указана", "hi": "कोई बायो उपलब्ध नहीं"
    },
    "Sector:": {
        "es": "Sector:", "en": "Sector:", "pt": "Setor:", "fr": "Secteur :",
        "de": "Bereich:", "it": "Settore:", "ja": "分野:", "ko": "분야:",
        "zh_Hans": "行业:", "ar": "القطاع:", "ru": "Сектор:", "hi": "क्षेत्र:"
    },
    "Rol:": {
        "es": "Rol:", "en": "Role:", "pt": "Função:", "fr": "Rôle :",
        "de": "Rolle:", "it": "Ruolo:", "ja": "役職:", "ko": "역할:",
        "zh_Hans": "角色:", "ar": "الدور:", "ru": "Роль:", "hi": "भूमिका:"
    },
    "Especialidad:": {
        "es": "Especialidad:", "en": "Specialty:", "pt": "Especialidade:", "fr": "Spécialité :",
        "de": "Fachgebiet:", "it": "Specializzazione:", "ja": "専門分野:", "ko": "전문 분야:",
        "zh_Hans": "专业领域:", "ar": "التخصص:", "ru": "Специализация:", "hi": "विशेषज्ञता:"
    },
    "Seniority:": {
        "es": "Seniority:", "en": "Seniority:", "pt": "Senioridade:", "fr": "Séniorité :",
        "de": "Erfahrungsstufe:", "it": "Livello di esperienza:", "ja": "経験レベル:", "ko": "경력 레벨:",
        "zh_Hans": "资历级别:", "ar": "مستوى الخبرة:", "ru": "Уровень опыта:", "hi": "अनुभव स्तर:"
    },
    "Idiomas:": {
        "es": "Idiomas:", "en": "Languages:", "pt": "Idiomas:", "fr": "Langues :",
        "de": "Sprachen:", "it": "Lingue:", "ja": "言語:", "ko": "언어:",
        "zh_Hans": "语言:", "ar": "اللغات:", "ru": "Языки:", "hi": "भाषाएँ:"
    },
    "Tags:": {
        "es": "Tags:", "en": "Tags:", "pt": "Tags:", "fr": "Tags :",
        "de": "Tags:", "it": "Tag:", "ja": "タグ:", "ko": "태그:",
        "zh_Hans": "标签:", "ar": "الوسوم:", "ru": "Теги:", "hi": "टैग:"
    },
    "Tipo de empleo:": {
        "es": "Tipo de empleo:", "en": "Employment type:", "pt": "Tipo de emprego:", "fr": "Type d'emploi :",
        "de": "Beschäftigungsart:", "it": "Tipo di impiego:", "ja": "雇用形態:", "ko": "고용 형태:",
        "zh_Hans": "雇佣类型:", "ar": "نوع التوظيف:", "ru": "Тип занятости:", "hi": "रोज़गार प्रकार:"
    },
    "Disponible para mudarse:": {
        "es": "Disponible para mudarse:", "en": "Willing to relocate:", "pt": "Disponível para mudança:", "fr": "Prêt à déménager :",
        "de": "Umzugsbereit:", "it": "Disponibile al trasferimento:", "ja": "転居可能:", "ko": "이사 가능:",
        "zh_Hans": "愿意搬迁:", "ar": "مستعد للانتقال:", "ru": "Готов к переезду:", "hi": "स्थानांतरण के लिए तैयार:"
    },
    "Disponible para viajar:": {
        "es": "Disponible para viajar:", "en": "Willing to travel:", "pt": "Disponível para viajar:", "fr": "Prêt à voyager :",
        "de": "Reisebereit:", "it": "Disponibile a viaggiare:", "ja": "出張可能:", "ko": "출장 가능:",
        "zh_Hans": "愿意出差:", "ar": "مستعد للسفر:", "ru": "Готов к командировкам:", "hi": "यात्रा के लिए तैयार:"
    },
    "Sin experiencia ni proyectos agregados": {
        "es": "Sin experiencia ni proyectos agregados", "en": "No experience or projects added yet", "pt": "Nenhuma experiência ou projeto adicionado", "fr": "Aucune expérience ni projet ajouté",
        "de": "Noch keine Erfahrung oder Projekte hinzugefügt", "it": "Nessuna esperienza o progetto aggiunto", "ja": "職歴やプロジェクトはまだ追加されていません", "ko": "추가된 경력이나 프로젝트가 없습니다",
        "zh_Hans": "暂未添加任何经历或项目", "ar": "لم تتم إضافة أي خبرة أو مشروع بعد", "ru": "Опыт и проекты пока не добавлены", "hi": "अभी तक कोई अनुभव या परियोजना नहीं जोड़ी गई"
    },
    "Sin redes sociales configuradas": {
        "es": "Sin redes sociales configuradas", "en": "No social links configured", "pt": "Nenhuma rede social configurada", "fr": "Aucun réseau social configuré",
        "de": "Keine sozialen Netzwerke eingerichtet", "it": "Nessun social network configurato", "ja": "ソーシャルリンクが設定されていません", "ko": "설정된 소셜 링크가 없습니다",
        "zh_Hans": "暂未配置社交链接", "ar": "لم يتم تكوين شبكات التواصل الاجتماعي", "ru": "Социальные сети не настроены", "hi": "कोई सोशल लिंक कॉन्फ़िगर नहीं है"
    },
    "Cargo / Puesto": {
        "es": "Cargo / Puesto", "en": "Position / Role", "pt": "Cargo / Posição", "fr": "Poste / Fonction",
        "de": "Position / Funktion", "it": "Posizione / Ruolo", "ja": "役職 / ポジション", "ko": "직책 / 직무",
        "zh_Hans": "职位 / 岗位", "ar": "المنصب / الوظيفة", "ru": "Должность / Роль", "hi": "पद / भूमिका"
    },
    "Empresa o Cliente": {
        "es": "Empresa o Cliente", "en": "Company or Client", "pt": "Empresa ou Cliente", "fr": "Entreprise ou Client",
        "de": "Unternehmen oder Kunde", "it": "Azienda o Cliente", "ja": "企業またはクライアント", "ko": "회사 또는 고객사",
        "zh_Hans": "公司或客户", "ar": "الشركة أو العميل", "ru": "Компания или клиент", "hi": "कंपनी या ग्राहक"
    },
    "Logotipo de la empresa (Opcional)": {
        "es": "Logotipo de la empresa (Opcional)", "en": "Company logo (Optional)", "pt": "Logotipo da empresa (Opcional)", "fr": "Logo de l'entreprise (Optionnel)",
        "de": "Unternehmenslogo (Optional)", "it": "Logo dell'azienda (Opzionale)", "ja": "企業ロゴ（任意）", "ko": "회사 로고 (선택 사항)",
        "zh_Hans": "公司徽标（可选）", "ar": "شعار الشركة (اختياري)", "ru": "Логотип компании (необязательно)", "hi": "कंपनी का लोगो (वैकल्पिक)"
    },
    "Captura o imagen del proyecto (Opcional)": {
        "es": "Captura o imagen del proyecto (Opcional)", "en": "Project screenshot or image (Optional)", "pt": "Captura de tela ou imagem do projeto (Opcional)", "fr": "Capture d'écran ou image du projet (Optionnel)",
        "de": "Screenshot oder Bild des Projekts (Optional)", "it": "Screenshot o immagine del progetto (Opzionale)", "ja": "プロジェクトのスクリーンショットまたは画像（任意）", "ko": "프로젝트 스크린샷 또는 이미지 (선택 사항)",
        "zh_Hans": "项目截图或图片（可选）", "ar": "لقطة شاشة أو صورة للمشروع (اختياري)", "ru": "Скриншот или изображение проекта (необязательно)", "hi": "परियोजना का स्क्रीनशॉट या छवि (वैकल्पिक)"
    },
    "Haz clic para subir": {
        "es": "Haz clic para subir", "en": "Click to upload", "pt": "Clique para enviar", "fr": "Cliquez pour télécharger",
        "de": "Klicken zum Hochladen", "it": "Clicca per caricare", "ja": "クリックしてアップロード", "ko": "클릭하여 업로드",
        "zh_Hans": "点击上传", "ar": "انقر للتحميل", "ru": "Нажмите для загрузки", "hi": "अपलोड करने के लिए क्लिक करें"
    },
    "el logo o imagen": {
        "es": "el logo o imagen", "en": "the logo or image", "pt": "o logotipo ou imagem", "fr": "le logo ou l'image",
        "de": "Logo oder Bild", "it": "il logo o l'immagine", "ja": "ロゴまたは画像", "ko": "로고 또는 이미지",
        "zh_Hans": "徽标或图片", "ar": "الشعار أو الصورة", "ru": "логотип или изображение", "hi": "लोगो या छवि"
    },
    "la captura del proyecto": {
        "es": "la captura del proyecto", "en": "the project screenshot", "pt": "a captura do projeto", "fr": "la capture du projet",
        "de": "den Projekt-Screenshot", "it": "lo screenshot del progetto", "ja": "プロジェクトのスクリーンショット", "ko": "프로젝트 스크린샷",
        "zh_Hans": "项目截图", "ar": "لقطة شاشة المشروع", "ru": "скриншот проекта", "hi": "परियोजना स्क्रीनशॉट"
    },
    "Logotipo cargado": {
        "es": "Logotipo cargado", "en": "Logo uploaded", "pt": "Logotipo carregado", "fr": "Logo téléchargé",
        "de": "Logo hochgeladen", "it": "Logo caricato", "ja": "ロゴがアップロードされました", "ko": "로고 업로드 완료",
        "zh_Hans": "徽标已上传", "ar": "تم تحميل الشعار", "ru": "Логотип загружен", "hi": "लोगो अपलोड हो गया"
    },
    "Imagen cargada": {
        "es": "Imagen cargada", "en": "Image uploaded", "pt": "Imagem carregada", "fr": "Image téléchargée",
        "de": "Bild hochgeladen", "it": "Immagine caricata", "ja": "画像がアップロードされました", "ko": "이미지 업로드 완료",
        "zh_Hans": "图片已上传", "ar": "تم تحميل الصورة", "ru": "Изображение загружено", "hi": "छवि अपलोड हो गई"
    },
    "Listo para guardar": {
        "es": "Listo para guardar", "en": "Ready to save", "pt": "Pronto para salvar", "fr": "Prêt à enregistrer",
        "de": "Bereit zum Speichern", "it": "Pronto per il salvataggio", "ja": "保存の準備完了", "ko": "저장 준비 완료",
        "zh_Hans": "准备保存", "ar": "جاهز للحفظ", "ru": "Готово к сохранению", "hi": "सहेजने के लिए तैयार"
    },
    "Eliminar": {
        "es": "Eliminar", "en": "Delete", "pt": "Excluir", "fr": "Supprimer",
        "de": "Löschen", "it": "Elimina", "ja": "削除", "ko": "삭제",
        "zh_Hans": "删除", "ar": "حذف", "ru": "Удалить", "hi": "हटाएं"
    },
    "Ver": {
        "es": "Ver", "en": "View", "pt": "Ver", "fr": "Voir",
        "de": "Ansehen", "it": "Visualizza", "ja": "見る", "ko": "보기",
        "zh_Hans": "查看", "ar": "عرض", "ru": "Посмотреть", "hi": "देखें"
    },
    "Editar Habilidades": {
        "es": "Editar Habilidades", "en": "Edit Skills", "pt": "Editar Habilidades", "fr": "Modifier les Compétences",
        "de": "Fähigkeiten bearbeiten", "it": "Modifica Competenze", "ja": "スキルを編集", "ko": "기술 수정",
        "zh_Hans": "编辑技能", "ar": "تعديل المهارات", "ru": "Редактировать навыки", "hi": "कौशल संपादित करें"
    },
    "Actualizar titular": {
        "es": "Actualizar titular", "en": "Update headline", "pt": "Atualizar título", "fr": "Mettre à jour le titre",
        "de": "Berufsbezeichnung aktualisieren", "it": "Aggiorna titolo", "ja": "肩書を更新", "ko": "한 줄 소개 업데이트",
        "zh_Hans": "更新头衔", "ar": "تحديث العنوان", "ru": "Обновить заголовок", "hi": "शीर्षक अपडेट करें"
    },
    "Actualizar bio": {
        "es": "Actualizar bio", "en": "Update bio", "pt": "Atualizar biografia", "fr": "Mettre à jour la biographie",
        "de": "Biografie aktualisieren", "it": "Aggiorna biografia", "ja": "自己紹介を更新", "ko": "자기소개 업데이트",
        "zh_Hans": "更新个人简介", "ar": "تحديث السيرة الذاتية", "ru": "Обновить биографию", "hi": "बायो अपडेट करें"
    },
    "Actualizar estado": {
        "es": "Actualizar estado", "en": "Update status", "pt": "Atualizar status", "fr": "Mettre à jour le statut",
        "de": "Status aktualisieren", "it": "Aggiorna stato", "ja": "ステータスを更新", "ko": "상태 업데이트",
        "zh_Hans": "更新状态", "ar": "تحديث الحالة", "ru": "Обновить статус", "hi": "स्थिति अपडेट करें"
    },
    "Actualizar foto": {
        "es": "Actualizar foto", "en": "Update photo", "pt": "Atualizar foto", "fr": "Mettre à jour la photo",
        "de": "Foto aktualisieren", "it": "Aggiorna foto", "ja": "写真を更新", "ko": "사진 업데이트",
        "zh_Hans": "更新照片", "ar": "تحديث الصورة", "ru": "Обновить фото", "hi": "फ़ोटो अपडेट करें"
    },
    "Agregar proyecto": {
        "es": "Agregar proyecto", "en": "Add project", "pt": "Adicionar projeto", "fr": "Ajouter un projet",
        "de": "Projekt hinzufügen", "it": "Aggiungi progetto", "ja": "プロジェクトを追加", "ko": "프로젝트 추가",
        "zh_Hans": "添加项目", "ar": "إضافة مشروع", "ru": "Добавить проект", "hi": "परियोजना जोड़ें"
    },
    "Agregar experiencia": {
        "es": "Agregar experiencia", "en": "Add experience", "pt": "Adicionar experiência", "fr": "Ajouter une expérience",
        "de": "Erfahrung hinzufügen", "it": "Aggiungi esperienza", "ja": "職歴を追加", "ko": "경력 추가",
        "zh_Hans": "添加经历", "ar": "إضافة خبرة", "ru": "Добавить опыт", "hi": "अनुभव जोड़ें"
    },
    "Editar experiencia": {
        "es": "Editar experiencia", "en": "Edit experience", "pt": "Editar experiência", "fr": "Modifier l'expérience",
        "de": "Erfahrung bearbeiten", "it": "Modifica esperienza", "ja": "職歴を編集", "ko": "경력 수정",
        "zh_Hans": "编辑经历", "ar": "تعديل الخبرة", "ru": "Редактировать опыт", "hi": "अनुभव संपादित करें"
    },
    "Editar proyecto": {
        "es": "Editar proyecto", "en": "Edit project", "pt": "Editar projeto", "fr": "Modifier le projet",
        "de": "Projekt bearbeiten", "it": "Modifica progetto", "ja": "プロジェクトを編集", "ko": "프로젝트 수정",
        "zh_Hans": "编辑项目", "ar": "تعديل المشروع", "ru": "Редактировать проект", "hi": "परियोजना संपादित करें"
    },
    "Guardar": {
        "es": "Guardar", "en": "Save", "pt": "Salvar", "fr": "Enregistrer",
        "de": "Speichern", "it": "Salva", "ja": "保存", "ko": "저장",
        "zh_Hans": "保存", "ar": "حفظ", "ru": "Сохранить", "hi": "सहेजें"
    },
    "Cancelar": {
        "es": "Cancelar", "en": "Cancel", "pt": "Cancelar", "fr": "Annuler",
        "de": "Abbrechen", "it": "Annulla", "ja": "キャンセル", "ko": "취소",
        "zh_Hans": "取消", "ar": "إلغاء", "ru": "Отмена", "hi": "रद्द करें"
    },
    "Estado de búsqueda": {
        "es": "Estado de búsqueda", "en": "Job search status", "pt": "Status de busca de emprego", "fr": "Statut de recherche d'emploi",
        "de": "Jobsuche-Status", "it": "Stato della ricerca", "ja": "求職ステータス", "ko": "구직 상태",
        "zh_Hans": "求职状态", "ar": "حالة البحث عن عمل", "ru": "Статус поиска работы", "hi": "नौकरी खोज की स्थिति"
    },
    "Estado de busqueda": {
        "es": "Estado de búsqueda", "en": "Job search status", "pt": "Status de busca de emprego", "fr": "Statut de recherche d'emploi",
        "de": "Jobsuche-Status", "it": "Stato della ricerca", "ja": "求職ステータス", "ko": "구직 상태",
        "zh_Hans": "求职状态", "ar": "حالة البحث عن عمل", "ru": "Статус поиска работы", "hi": "नौकरी खोज की स्थिति"
    },
    "Preferencia de ubicación": {
        "es": "Preferencia de ubicación", "en": "Workplace preference", "pt": "Preferência de local de trabalho", "fr": "Préférence de lieu de travail",
        "de": "Arbeitsort-Präferenz", "it": "Preferenza di luogo di lavoro", "ja": "勤務地設定", "ko": "근무 위치 선호도",
        "zh_Hans": "工作地点偏好", "ar": "تفضيل موقع العمل", "ru": "Предпочтение места работы", "hi": "कार्यस्थल प्राथमिकता"
    },
    "Preferencia de ubicacion": {
        "es": "Preferencia de ubicación", "en": "Workplace preference", "pt": "Preferência de local de trabalho", "fr": "Préférence de lieu de travail",
        "de": "Arbeitsort-Präferenz", "it": "Preferenza di luogo di lavoro", "ja": "勤務地設定", "ko": "근무 위치 선호도",
        "zh_Hans": "工作地点偏好", "ar": "تفضيل موقع العمل", "ru": "Предпочтение места работы", "hi": "कार्यस्थल प्राथमिकता"
    },
    "Cuéntanos sobre ti...": {
        "es": "Cuéntanos sobre ti...", "en": "Tell us about yourself...", "pt": "Conte-nos sobre você...", "fr": "Parlez-nous de vous...",
        "de": "Erzähl uns von dir...", "it": "Raccontaci di te...", "ja": "自己紹介を記入してください...", "ko": "자신에 대해 알려주세요...",
        "zh_Hans": "介绍一下你自己...", "ar": "أخبرنا عن نفسك...", "ru": "Расскажите о себе...", "hi": "अपने बारे में बताएं..."
    },
    "Cuentanos sobre ti...": {
        "es": "Cuéntanos sobre ti...", "en": "Tell us about yourself...", "pt": "Conte-nos sobre você...", "fr": "Parlez-nous de vous...",
        "de": "Erzähl uns von dir...", "it": "Raccontaci di te...", "ja": "自己紹介を記入してください...", "ko": "자신에 대해 알려주세요...",
        "zh_Hans": "介绍一下你自己...", "ar": "أخبرنا عن نفسك...", "ru": "Расскажите о себе...", "hi": "अपने बारे में बताएं..."
    },
    "Editar redes sociales": {
        "es": "Editar redes sociales", "en": "Edit social links", "pt": "Editar redes sociais", "fr": "Modifier les réseaux sociaux",
        "de": "Soziale Netzwerke bearbeiten", "it": "Modifica social network", "ja": "ソーシャルリンクを編集", "ko": "소셜 링크 수정",
        "zh_Hans": "编辑社交链接", "ar": "تعديل شبكات التواصل الاجتماعي", "ru": "Редактировать социальные сети", "hi": "सोशल लिंक संपादित करें"
    },
    "JPG, PNG o WebP. Máximo 5MB.": {
        "es": "JPG, PNG o WebP. Máximo 5MB.", "en": "JPG, PNG or WebP. Maximum 5MB.", "pt": "JPG, PNG ou WebP. Máximo de 5MB.", "fr": "JPG, PNG ou WebP. Maximum 5 Mo.",
        "de": "JPG, PNG oder WebP. Maximal 5 MB.", "it": "JPG, PNG o WebP. Massimo 5MB.", "ja": "JPG、PNG、またはWebP。最大5MB。", "ko": "JPG, PNG 또는 WebP. 최대 5MB.",
        "zh_Hans": "JPG、PNG 或 WebP。最大 5MB。", "ar": "JPG أو PNG أو WebP. بحد أقصى 5 ميجابايت.", "ru": "JPG, PNG или WebP. Максимум 5 МБ.", "hi": "JPG, PNG या WebP. अधिकतम 5MB."
    },
    "JPG, PNG o WebP. Maximo 5MB.": {
        "es": "JPG, PNG o WebP. Máximo 5MB.", "en": "JPG, PNG or WebP. Maximum 5MB.", "pt": "JPG, PNG ou WebP. Máximo de 5MB.", "fr": "JPG, PNG ou WebP. Maximum 5 Mo.",
        "de": "JPG, PNG oder WebP. Maximal 5 MB.", "it": "JPG, PNG o WebP. Massimo 5MB.", "ja": "JPG、PNG、またはWebP。最大5MB。", "ko": "JPG, PNG 또는 WebP. 최대 5MB.",
        "zh_Hans": "JPG、PNG 或 WebP。最大 5MB。", "ar": "JPG أو PNG أو WebP. بحد أقصى 5 ميجابايت.", "ru": "JPG, PNG или WebP. Максимум 5 МБ.", "hi": "JPG, PNG या WebP. अधिकतम 5MB."
    },
    "URL del proyecto (Opcional)": {
        "es": "URL del proyecto (Opcional)", "en": "Project URL (Optional)", "pt": "URL do projeto (Opcional)", "fr": "URL du projet (Optionnel)",
        "de": "Projekt-URL (Optional)", "it": "URL del progetto (Opzionale)", "ja": "プロジェクトURL（任意）", "ko": "프로젝트 URL (선택 사항)",
        "zh_Hans": "项目网址（可选）", "ar": "رابط المشروع (اختياري)", "ru": "URL проекта (необязательно)", "hi": "परियोजना URL (वैकल्पिक)"
    },
    "Nombre del proyecto": {
        "es": "Nombre del proyecto", "en": "Project name", "pt": "Nome do projeto", "fr": "Nom du projet",
        "de": "Projektname", "it": "Nome del progetto", "ja": "プロジェクト名", "ko": "프로젝트 이름",
        "zh_Hans": "项目名称", "ar": "اسم المشروع", "ru": "Название проекта", "hi": "परियोजना का नाम"
    },
    "Describe el proyecto y las tecnologías usadas...": {
        "es": "Describe el proyecto y las tecnologías usadas...", "en": "Describe the project and technologies used...", "pt": "Descreva o projeto e as tecnologias utilizadas...", "fr": "Décrivez le projet et les technologies utilisées...",
        "de": "Beschreibe das Projekt und die verwendeten Technologien...", "it": "Descrivi il progetto e le tecnologie utilizzate...", "ja": "プロジェクトと使用した技術について説明してください...", "ko": "프로젝트와 사용된 기술을 설명하세요...",
        "zh_Hans": "描述该项目以及所使用的技术...", "ar": "صف المشروع والتقنيات المستخدمة...", "ru": "Опишите проект и использованные технологии...", "hi": "परियोजना और उपयोग की गई तकनीकों का वर्णन करें..."
    },
    "Describe tus responsabilidades y logros...": {
        "es": "Describe tus responsabilidades y logros...", "en": "Describe your responsibilities and achievements...", "pt": "Descreva suas responsabilidades e conquistas...", "fr": "Décrivez vos responsabilités et réalisations...",
        "de": "Beschreibe deine Verantwortlichkeiten und Erfolge...", "it": "Descrivi le tue responsabilità e i tuoi traguardi...", "ja": "担当業務や成果について説明してください...", "ko": "담당 업무 및 성과를 설명하세요...",
        "zh_Hans": "描述你的职责和成就...", "ar": "صف مسؤولياتك وإنجازاتك...", "ru": "Опишите свои обязанности и достижения...", "hi": "अपनी जिम्मेदारियों और उपलब्धियों का वर्णन करें..."
    },
    "Seleccionar...": {
        "es": "Seleccionar...", "en": "Select...", "pt": "Selecionar...", "fr": "Sélectionner...",
        "de": "Auswählen...", "it": "Seleziona...", "ja": "選択...", "ko": "선택...",
        "zh_Hans": "请选择...", "ar": "اختر...", "ru": "Выбрать...", "hi": "चुनें..."
    },
    "Seleccionar idioma...": {
        "es": "Seleccionar idioma...", "en": "Select language...", "pt": "Selecionar idioma...", "fr": "Sélectionner la langue...",
        "de": "Sprache auswählen...", "it": "Seleziona lingua...", "ja": "言語を選択...", "ko": "언어 선택...",
        "zh_Hans": "选择语言...", "ar": "اختر اللغة...", "ru": "Выберите язык...", "hi": "भाषा चुनें..."
    },
    "Buscar tag...": {
        "es": "Buscar tag...", "en": "Search tag...", "pt": "Buscar tag...", "fr": "Rechercher un tag...",
        "de": "Tag suchen...", "it": "Cerca tag...", "ja": "タグを検索...", "ko": "태그 검색...",
        "zh_Hans": "搜索标签...", "ar": "ابحث عن وسم...", "ru": "Поиск тега...", "hi": "टैग खोजें..."
    },
    "Buscando activamente": {
        "es": "Buscando activamente", "en": "Actively looking", "pt": "Buscando ativamente", "fr": "En recherche active",
        "de": "Aktiv auf Jobsuche", "it": "In cerca attiva", "ja": "積極的に転職活動中", "ko": "적극적 구직 중",
        "zh_Hans": "积极寻找机会", "ar": "أبحث بنشاط عن عمل", "ru": "В активном поиске", "hi": "सक्रिय रूप से तलाश में"
    },
    "Abierto a ofertas": {
        "es": "Abierto a ofertas", "en": "Open to offers", "pt": "Aberto a propostas", "fr": "À l'écoute du marché",
        "de": "Offen für Angebote", "it": "Aperto a offerte", "ja": "良い案件があれば検討", "ko": "이직 제안에 열려 있음",
        "zh_Hans": "对机会持开放态度", "ar": "منفتح على العروض", "ru": "Открыт к предложениям", "hi": "अवसरों के लिए तैयार"
    },
    "No buscando": {
        "es": "No buscando", "en": "Not looking", "pt": "Não estou procurando", "fr": "Pas en recherche",
        "de": "Nicht auf Jobsuche", "it": "Non in cerca", "ja": "転職希望なし", "ko": "구직 중이 아님",
        "zh_Hans": "暂不考虑机会", "ar": "لا أبحث عن عمل", "ru": "Не ищу работу", "hi": "तलाश नहीं कर रहे"
    },
    "Inmediata": {
        "es": "Inmediata", "en": "Immediate", "pt": "Imediata", "fr": "Immédiate",
        "de": "Sofort", "it": "Immediata", "ja": "即時", "ko": "즉시 가능",
        "zh_Hans": "立即到岗", "ar": "فوري", "ru": "Немедленно", "hi": "तत्काल"
    },
    "2 semanas": {
        "es": "2 semanas", "en": "2 weeks", "pt": "2 semanas", "fr": "2 semaines",
        "de": "2 Wochen", "it": "2 settimane", "ja": "2週間", "ko": "2주 후",
        "zh_Hans": "2周内", "ar": "أسبوعان", "ru": "2 недели", "hi": "2 सप्ताह"
    },
    "1 mes": {
        "es": "1 mes", "en": "1 month", "pt": "1 mês", "fr": "1 mois",
        "de": "1 Monat", "it": "1 mese", "ja": "1ヶ月", "ko": "1개월 후",
        "zh_Hans": "1个月内", "ar": "شهر واحد", "ru": "1 месяц", "hi": "1 महीना"
    },
    "Negociable": {
        "es": "Negociable", "en": "Negotiable", "pt": "Negociável", "fr": "Négociable",
        "de": "Verhandelbar", "it": "Trattabile", "ja": "相談可能", "ko": "협의 가능",
        "zh_Hans": "可协商", "ar": "قابل للتفاوض", "ru": "Договорная", "hi": "परक्राम्य"
    },
    "Remoto": {
        "es": "Remoto", "en": "Remote", "pt": "Remoto", "fr": "Télétravail",
        "de": "Remote", "it": "Da remoto", "ja": "リモート", "ko": "원격 근무",
        "zh_Hans": "远程办公", "ar": "عن بُعد", "ru": "Удалённо", "hi": "रिमोट"
    },
    "Híbrido": {
        "es": "Híbrido", "en": "Hybrid", "pt": "Híbrido", "fr": "Hybride",
        "de": "Hybrid", "it": "Ibrido", "ja": "ハイブリッド", "ko": "하이브리드",
        "zh_Hans": "混合办公", "ar": "هجين", "ru": "Гибрид", "hi": "हाइब्रिड"
    },
    "Hibrido": {
        "es": "Híbrido", "en": "Hybrid", "pt": "Híbrido", "fr": "Hybride",
        "de": "Hybrid", "it": "Ibrido", "ja": "ハイブリッド", "ko": "하이브리드",
        "zh_Hans": "混合办公", "ar": "هجين", "ru": "Гибрид", "hi": "हाइब्रिड"
    },
    "Presencial": {
        "es": "Presencial", "en": "On-site", "pt": "Presencial", "fr": "Sur site",
        "de": "Vor Ort", "it": "In sede", "ja": "出社", "ko": "현장 근무",
        "zh_Hans": "现场办公", "ar": "حضوري", "ru": "В офисе", "hi": "ऑन-साइट"
    },
    "Según destino": {
        "es": "Según destino", "en": "Depends on location", "pt": "Depende do destino", "fr": "Selon la destination",
        "de": "Abhängig vom Ort", "it": "A seconda della destinazione", "ja": "勤務地による", "ko": "지역에 따라 결정",
        "zh_Hans": "视地点而定", "ar": "حسب الوجهة", "ru": "Зависит от места", "hi": "स्थान पर निर्भर"
    },
    "Segun destino": {
        "es": "Según destino", "en": "Depends on location", "pt": "Depende do destino", "fr": "Selon la destination",
        "de": "Abhängig vom Ort", "it": "A seconda della destinazione", "ja": "勤務地による", "ko": "지역에 따라 결정",
        "zh_Hans": "视地点而定", "ar": "حسب الوجهة", "ru": "Зависит от места", "hi": "स्थान पर निर्भर"
    },
    "Ocasional": {
        "es": "Ocasional", "en": "Occasional", "pt": "Ocasional", "fr": "Occasionnel",
        "de": "Gelegentlich", "it": "Occasionale", "ja": "時々", "ko": "때때로 가능",
        "zh_Hans": "偶尔出差", "ar": "عرضي", "ru": "Иногда", "hi": "कभी-कभार"
    },
    "Frecuente": {
        "es": "Frecuente", "en": "Frequent", "pt": "Frequente", "fr": "Fréquent",
        "de": "Häufig", "it": "Frequente", "ja": "頻繁", "ko": "자주 가능",
        "zh_Hans": "频繁出差", "ar": "متكرر", "ru": "Часто", "hi": "अक्सर"
    },
    "Full-time": {
        "es": "Full-time", "en": "Full-time", "pt": "Tempo integral", "fr": "Temps plein",
        "de": "Vollzeit", "it": "Tempo pieno", "ja": "フルタイム", "ko": "정규직",
        "zh_Hans": "全职", "ar": "دوام كامل", "ru": "Полная занятость", "hi": "पूर्णकालिक"
    },
    "Part-time": {
        "es": "Part-time", "en": "Part-time", "pt": "Meio período", "fr": "Temps partiel",
        "de": "Teilzeit", "it": "Part-time", "ja": "パートタイム", "ko": "파트타임",
        "zh_Hans": "兼职", "ar": "دوام جزئي", "ru": "Частичная занятость", "hi": "अंशकालिक"
    },
    "Contrato": {
        "es": "Contrato", "en": "Contract", "pt": "Contrato", "fr": "Contrat",
        "de": "Vertrag", "it": "Contratto", "ja": "契約", "ko": "계약직",
        "zh_Hans": "合同工", "ar": "عقد", "ru": "Контракт", "hi": "अनुबंध"
    },
    "Freelance": {
        "es": "Freelance", "en": "Freelance", "pt": "Freelance", "fr": "Freelance",
        "de": "Freiberuflich", "it": "Freelance", "ja": "フリーランス", "ko": "프리랜서",
        "zh_Hans": "自由职业", "ar": "عمل حر", "ru": "Фриланс", "hi": "फ्रीलांस"
    },
    "Sí": {
        "es": "Sí", "en": "Yes", "pt": "Sim", "fr": "Oui",
        "de": "Ja", "it": "Sì", "ja": "はい", "ko": "예",
        "zh_Hans": "是", "ar": "نعم", "ru": "Да", "hi": "हाँ"
    },
    "Si": {
        "es": "Sí", "en": "Yes", "pt": "Sim", "fr": "Oui",
        "de": "Ja", "it": "Sì", "ja": "はい", "ko": "예",
        "zh_Hans": "是", "ar": "نعم", "ru": "Да", "hi": "हाँ"
    },
    "No": {
        "es": "No", "en": "No", "pt": "Não", "fr": "Non",
        "de": "Nein", "it": "No", "ja": "いいえ", "ko": "아니오",
        "zh_Hans": "否", "ar": "لا", "ru": "Нет", "hi": "नहीं"
    },
    "No especificado": {
        "es": "No especificado", "en": "Not specified", "pt": "Não especificado", "fr": "Non spécifié",
        "de": "Nicht angegeben", "it": "Non specificato", "ja": "未指定", "ko": "지정되지 않음",
        "zh_Hans": "未指定", "ar": "غير محدد", "ru": "Не указано", "hi": "अनिर्दिष्ट"
    },
    "Junior": {
        "es": "Junior", "en": "Junior", "pt": "Júnior", "fr": "Junior",
        "de": "Junior", "it": "Junior", "ja": "ジュニア", "ko": "주니어",
        "zh_Hans": "初级", "ar": "مبتدئ", "ru": "Джуниор", "hi": "जूनियर"
    },
    "Semi-Senior": {
        "es": "Semi-Senior", "en": "Mid-Level", "pt": "Pleno", "fr": "Intermédiaire",
        "de": "Mid-Level", "it": "Mid-Level", "ja": "ミドル", "ko": "미드 레벨",
        "zh_Hans": "中级", "ar": "متوسط الخبرة", "ru": "Мидл", "hi": "मध्यम स्तर"
    },
    "Senior": {
        "es": "Senior", "en": "Senior", "pt": "Sênior", "fr": "Sénior",
        "de": "Senior", "it": "Senior", "ja": "シニア", "ko": "시니어",
        "zh_Hans": "资深", "ar": "خبير", "ru": "Сеньор", "hi": "वरिष्ठ"
    },
    "Lead": {
        "es": "Lead", "en": "Lead", "pt": "Líder", "fr": "Lead",
        "de": "Lead", "it": "Lead", "ja": "リード", "ko": "리드",
        "zh_Hans": "专家/主管", "ar": "قائد فريق", "ru": "Лид", "hi": "लीड"
    },
    "Español": {
        "es": "Español", "en": "Spanish", "pt": "Espanhol", "fr": "Espagnol",
        "de": "Spanisch", "it": "Spagnolo", "ja": "スペイン語", "ko": "스페인어",
        "zh_Hans": "西班牙语", "ar": "الإسبانية", "ru": "Испанский", "hi": "स्पैनिश"
    },
    "Inglés": {
        "es": "Inglés", "en": "English", "pt": "Inglês", "fr": "Anglais",
        "de": "Englisch", "it": "Inglese", "ja": "英語", "ko": "영어",
        "zh_Hans": "英语", "ar": "الإنجليزية", "ru": "Английский", "hi": "अंग्रेज़ी"
    },
    "Portugués": {
        "es": "Portugués", "en": "Portuguese", "pt": "Português", "fr": "Portugais",
        "de": "Portugiesisch", "it": "Portoghese", "ja": "ポルトガル語", "ko": "포르투갈어",
        "zh_Hans": "葡萄牙语", "ar": "البرتغالية", "ru": "Португальский", "hi": "पुर्तगाली"
    },
    "Francés": {
        "es": "Francés", "en": "French", "pt": "Francês", "fr": "Français",
        "de": "Französisch", "it": "Francese", "ja": "フランス語", "ko": "프랑스어",
        "zh_Hans": "法语", "ar": "الفرنسية", "ru": "Французский", "hi": "फ्रेंच"
    },
    "Alemán": {
        "es": "Alemán", "en": "German", "pt": "Alemão", "fr": "Allemand",
        "de": "Deutsch", "it": "Tedesco", "ja": "ドイツ語", "ko": "독일어",
        "zh_Hans": "德语", "ar": "الألمانية", "ru": "Немецкий", "hi": "जर्मन"
    },
    "Italiano": {
        "es": "Italiano", "en": "Italian", "pt": "Italiano", "fr": "Italien",
        "de": "Italienisch", "it": "Italiano", "ja": "イタリア語", "ko": "이탈리아어",
        "zh_Hans": "意大利语", "ar": "الإيطالية", "ru": "Итальянский", "hi": "इतालवी"
    },
    "Japonés": {
        "es": "Japonés", "en": "Japanese", "pt": "Japonês", "fr": "Japonais",
        "de": "Japanisch", "it": "Giapponese", "ja": "日本語", "ko": "일본어",
        "zh_Hans": "日语", "ar": "اليابانية", "ru": "Японский", "hi": "जापानी"
    },
    "Coreano": {
        "es": "Coreano", "en": "Korean", "pt": "Coreano", "fr": "Coréen",
        "de": "Koreanisch", "it": "Coreano", "ja": "韓国語", "ko": "한국어",
        "zh_Hans": "韩语", "ar": "الكورية", "ru": "Корейский", "hi": "कोरियाई"
    },
    "Chino": {
        "es": "Chino", "en": "Chinese", "pt": "Chinês", "fr": "Chinois",
        "de": "Chinesisch", "it": "Cinese", "ja": "中国語", "ko": "중국어",
        "zh_Hans": "中文", "ar": "الصينية", "ru": "Китайский", "hi": "चीनी"
    },
    "Ruso": {
        "es": "Ruso", "en": "Russian", "pt": "Russo", "fr": "Russe",
        "de": "Russisch", "it": "Russo", "ja": "ロシア語", "ko": "러시아어",
        "zh_Hans": "俄语", "ar": "الروسية", "ru": "Русский", "hi": "रूसी"
    },
    "Árabe": {
        "es": "Árabe", "en": "Arabic", "pt": "Árabe", "fr": "Arabe",
        "de": "Arabisch", "it": "Arabo", "ja": "アラビア語", "ko": "아랍어",
        "zh_Hans": "阿拉伯语", "ar": "العربية", "ru": "Арабский", "hi": "अरबी"
    },
    "Hindi": {
        "es": "Hindi", "en": "Hindi", "pt": "Hindi", "fr": "Hindi",
        "de": "Hindi", "it": "Hindi", "ja": "ヒンディー語", "ko": "힌디어",
        "zh_Hans": "印地语", "ar": "الهندية", "ru": "Хинди", "hi": "हिन्दी"
    },
    "Experiencia": {
        "es": "Experiencia", "en": "Experience", "pt": "Experiência", "fr": "Expérience",
        "de": "Erfahrung", "it": "Esperienza", "ja": "職歴", "ko": "경력",
        "zh_Hans": "经历", "ar": "خبرة", "ru": "Опыт", "hi": "अनुभव"
    },
    "Proyecto": {
        "es": "Proyecto", "en": "Project", "pt": "Projeto", "fr": "Projet",
        "de": "Projekt", "it": "Progetto", "ja": "プロジェクト", "ko": "프로젝트",
        "zh_Hans": "项目", "ar": "مشروع", "ru": "Проект", "hi": "परियोजना"
    },
    "Empresa": {
        "es": "Empresa", "en": "Company", "pt": "Empresa", "fr": "Entreprise",
        "de": "Unternehmen", "it": "Azienda", "ja": "企業", "ko": "회사",
        "zh_Hans": "公司", "ar": "الشركة", "ru": "Компания", "hi": "कंपनी"
    },
    "Periodo": {
        "es": "Periodo", "en": "Period", "pt": "Período", "fr": "Période",
        "de": "Zeitraum", "it": "Periodo", "ja": "期間", "ko": "기간",
        "zh_Hans": "时间段", "ar": "الفترة", "ru": "Период", "hi": "अवधि"
    },
    "Descripción": {
        "es": "Descripción", "en": "Description", "pt": "Descrição", "fr": "Description",
        "de": "Beschreibung", "it": "Descrizione", "ja": "説明", "ko": "설명",
        "zh_Hans": "描述", "ar": "الوصف", "ru": "Описание", "hi": "विवरण"
    },
    "Bio": {
        "es": "Bio", "en": "Bio", "pt": "Bio", "fr": "Bio",
        "de": "Biografie", "it": "Bio", "ja": "自己紹介", "ko": "소개",
        "zh_Hans": "简介", "ar": "السيرة الذاتية", "ru": "О себе", "hi": "बायो"
    },
    "Editar": {
        "es": "Editar", "en": "Edit", "pt": "Editar", "fr": "Modifier",
        "de": "Bearbeiten", "it": "Modifica", "ja": "編集", "ko": "수정",
        "zh_Hans": "编辑", "ar": "تعديل", "ru": "Редактировать", "hi": "संपादित करें"
    },
    "Redes Sociales": {
        "es": "Redes Sociales", "en": "Social Links", "pt": "Redes Sociais", "fr": "Réseaux Sociaux",
        "de": "Soziale Netzwerke", "it": "Social Network", "ja": "ソーシャルリンク", "ko": "소셜 링크",
        "zh_Hans": "社交网络", "ar": "شبكات التواصل", "ru": "Социальные сети", "hi": "सोशल नेटवर्क"
    },
    "Foto de perfil": {
        "es": "Foto de perfil", "en": "Profile photo", "pt": "Foto de perfil", "fr": "Photo de profil",
        "de": "Profilbild", "it": "Foto del profilo", "ja": "プロフィール写真", "ko": "프로필 사진",
        "zh_Hans": "个人头像", "ar": "صورة الملف الشخصي", "ru": "Фото профиля", "hi": "प्रोफ़ाइल फ़ोटो"
    },
    "Sector": {
        "es": "Sector", "en": "Sector", "pt": "Setor", "fr": "Secteur",
        "de": "Bereich", "it": "Settore", "ja": "分野", "ko": "분야",
        "zh_Hans": "行业", "ar": "القطاع", "ru": "Сектор", "hi": "क्षेत्र"
    },
    "Rol": {
        "es": "Rol", "en": "Role", "pt": "Função", "fr": "Rôle",
        "de": "Rolle", "it": "Ruolo", "ja": "役職", "ko": "역할",
        "zh_Hans": "角色", "ar": "الدور", "ru": "Роль", "hi": "भूमिका"
    },
    "Especialidad": {
        "es": "Especialidad", "en": "Specialty", "pt": "Especialidade", "fr": "Spécialité",
        "de": "Fachgebiet", "it": "Specializzazione", "ja": "専門分野", "ko": "전문 분야",
        "zh_Hans": "专业领域", "ar": "التخصص", "ru": "Специализация", "hi": "विशेषज्ञता"
    },
    "Seniority": {
        "es": "Seniority", "en": "Seniority", "pt": "Senioridade", "fr": "Séniorité",
        "de": "Erfahrungsstufe", "it": "Livello di esperienza", "ja": "経験レベル", "ko": "경력 레벨",
        "zh_Hans": "资历级别", "ar": "مستوى الخبرة", "ru": "Уровень опыта", "hi": "अनुभव स्तर"
    },
    "Idiomas": {
        "es": "Idiomas", "en": "Languages", "pt": "Idiomas", "fr": "Langues",
        "de": "Sprachen", "it": "Lingue", "ja": "言語", "ko": "언어",
        "zh_Hans": "语言", "ar": "اللغات", "ru": "Языки", "hi": "भाषाएँ"
    },
    "Tags": {
        "es": "Tags", "en": "Tags", "pt": "Tags", "fr": "Tags",
        "de": "Tags", "it": "Tag", "ja": "タグ", "ko": "태그",
        "zh_Hans": "标签", "ar": "الوسوم", "ru": "Теги", "hi": "टैग"
    },
    "Tipo de empleo": {
        "es": "Tipo de empleo", "en": "Employment type", "pt": "Tipo de emprego", "fr": "Type d'emploi",
        "de": "Beschäftigungsart", "it": "Tipo di impiego", "ja": "雇用形態", "ko": "고용 형태",
        "zh_Hans": "雇佣类型", "ar": "نوع التوظيف", "ru": "Тип занятости", "hi": "रोज़गार प्रकार"
    },
    "Preferencias de trabajo": {
        "es": "Preferencias de trabajo", "en": "Work Preferences", "pt": "Preferências de Trabalho", "fr": "Préférences de Travail",
        "de": "Arbeitspräferenzen", "it": "Preferenze di Lavoro", "ja": "勤務設定", "ko": "근무 선호도",
        "zh_Hans": "工作偏好", "ar": "تفضيلات العمل", "ru": "Предпочтения по работе", "hi": "काम की प्राथमिकताएं"
    },
    "Disponible para mudarse": {
        "es": "Disponible para mudarse", "en": "Willing to relocate", "pt": "Disponível para mudança", "fr": "Prêt à déménager",
        "de": "Umzugsbereit", "it": "Disponibile al trasferimento", "ja": "転居可能", "ko": "이사 가능",
        "zh_Hans": "愿意搬迁", "ar": "مستعد للانتقال", "ru": "Готов к переезду", "hi": "स्थानांतरण के लिए तैयार"
    },
    "Disponible para viajar": {
        "es": "Disponible para viajar", "en": "Willing to travel", "pt": "Disponível para viajar", "fr": "Prêt à voyager",
        "de": "Reisebereit", "it": "Disponibile a viaggiare", "ja": "出張可能", "ko": "출장 가능",
        "zh_Hans": "愿意出差", "ar": "مستعد للسفر", "ru": "Готов к командировкам", "hi": "यात्रा के लिए तैयार"
    },
    "Disponibilidad": {
        "es": "Disponibilidad", "en": "Availability", "pt": "Disponibilidade", "fr": "Disponibilité",
        "de": "Verfügbarkeit", "it": "Disponibilità", "ja": "就業開始可能日", "ko": "입사 가능 시기",
        "zh_Hans": "到岗时间", "ar": "التوافر", "ru": "Доступность", "hi": "उपलब्धता"
    },
    "Perfil Profesional": {
        "es": "Perfil Profesional", "en": "Professional Profile", "pt": "Perfil Profissional", "fr": "Profil Professionnel",
        "de": "Berufliches Profil", "it": "Profilo Professionale", "ja": "職務プロフィール", "ko": "전문가 프로필",
        "zh_Hans": "专业个人资料", "ar": "الملف المهني", "ru": "Профессиональный профиль", "hi": "व्यावसायिक प्रोफ़ाइल"
    },
    "Dashboard": {
        "es": "Dashboard", "en": "Dashboard", "pt": "Painel", "fr": "Tableau de bord",
        "de": "Dashboard", "it": "Pannello", "ja": "ダッシュボード", "ko": "대시보드",
        "zh_Hans": "控制台", "ar": "لوحة التحكم", "ru": "Панель управления", "hi": "डैशबोर्ड"
    },
    "Tablón": {
        "es": "Tablón", "en": "Board", "pt": "Quadro", "fr": "Tableau",
        "de": "Pinnwand", "it": "Bacheca", "ja": "ボード", "ko": "게시판",
        "zh_Hans": "展示板", "ar": "اللوحة", "ru": "Доска", "hi": "बोर्ड"
    },
    "Para trabajadores": {
        "es": "Para trabajadores", "en": "For workers", "pt": "Para trabalhadores", "fr": "Pour les professionnels",
        "de": "Für Fachkräfte", "it": "Per i lavoratori", "ja": "求職者向け", "ko": "구직자용",
        "zh_Hans": "面向求职者", "ar": "للباحثين عن عمل", "ru": "Для соискателей", "hi": "पेशेवरों के लिए"
    },
    "Para reclutadores": {
        "es": "Para reclutadores", "en": "For recruiters", "pt": "Para recrutadores", "fr": "Pour les recruteurs",
        "de": "Für Recruiter", "it": "Per i recruiter", "ja": "採用担当者向け", "ko": "채용 담당자용",
        "zh_Hans": "面向招聘方", "ar": "لمسؤولي التوظيف", "ru": "Для рекрутеров", "hi": "नियोक्ताओं के लिए"
    },
    "Cambiar tema": {
        "es": "Cambiar tema", "en": "Toggle theme", "pt": "Alternar tema", "fr": "Changer de thème",
        "de": "Design wechseln", "it": "Cambia tema", "ja": "テーマを切り替え", "ko": "테마 전환",
        "zh_Hans": "切换主题", "ar": "تغيير المظهر", "ru": "Сменить тему", "hi": "थीम बदलें"
    },
    "Salir": {
        "es": "Salir", "en": "Log out", "pt": "Sair", "fr": "Déconnexion",
        "de": "Abmelden", "it": "Esci", "ja": "ログアウト", "ko": "로그아웃",
        "zh_Hans": "退出登录", "ar": "تسجيل الخروج", "ru": "Выйти", "hi": "लॉग आउट"
    },
    "Entrar": {
        "es": "Entrar", "en": "Log in", "pt": "Entrar", "fr": "Connexion",
        "de": "Anmelden", "it": "Accedi", "ja": "ログイン", "ko": "로그인",
        "zh_Hans": "登录", "ar": "تسجيل الدخول", "ru": "Войти", "hi": "लॉग इन"
    },
    "Registrarse": {
        "es": "Registrarse", "en": "Sign up", "pt": "Cadastre-se", "fr": "Inscription",
        "de": "Registrieren", "it": "Registrati", "ja": "新規登録", "ko": "회원가입",
        "zh_Hans": "注册", "ar": "إنشاء حساب", "ru": "Регистрация", "hi": "साइन अप"
    },
    "¿Deseas eliminar esta experiencia laboral?": {
        "es": "¿Deseas eliminar esta experiencia laboral?", "en": "Do you want to delete this work experience?", "pt": "Deseja excluir esta experiência profissional?", "fr": "Voulez-vous supprimer cette expérience professionnelle ?",
        "de": "Möchtest du diese Berufserfahrung löschen?", "it": "Vuoi eliminare questa esperienza lavorativa?", "ja": "この職歴を削除してもよろしいですか？", "ko": "이 경력을 삭제하시겠습니까?",
        "zh_Hans": "确定要删除此工作经历吗？", "ar": "هل ترغب في حذف هذه الخبرة المهنية؟", "ru": "Удалить этот опыт работы?", "hi": "क्या आप इस कार्य अनुभव को हटाना चाहते हैं?"
    },
    "¿Deseas eliminar este proyecto?": {
        "es": "¿Deseas eliminar este proyecto?", "en": "Do you want to delete this project?", "pt": "Deseja excluir este projeto?", "fr": "Voulez-vous supprimer ce projet ?",
        "de": "Möchtest du dieses Projekt löschen?", "it": "Vuoi eliminare questo progetto?", "ja": "このプロジェクトを削除してもよろしいですか？", "ko": "이 프로젝트를 삭제하시겠습니까?",
        "zh_Hans": "确定要删除此项目吗？", "ar": "هل ترغب في حذف هذا المشروع؟", "ru": "Удалить этот проект?", "hi": "क्या आप इस परियोजना को हटाना चाहते हैं?"
    },
    "Ej: Desarrollador Full Stack": {
        "es": "Ej: Desarrollador Full Stack", "en": "e.g. Full Stack Developer", "pt": "Ex: Desenvolvedor Full Stack", "fr": "Ex : Développeur Full Stack",
        "de": "z.B. Full Stack Entwickler", "it": "Es: Sviluppatore Full Stack", "ja": "例: フルスタックエンジニア", "ko": "예: 풀스택 개발자",
        "zh_Hans": "例如：全栈开发工程师", "ar": "مثال: مطور برمجيات متكامل", "ru": "Например: Full Stack разработчик", "hi": "उदा: फुल स्टैक डेवलपर"
    },
    "Ej: Tech Solutions": {
        "es": "Ej: Tech Solutions", "en": "e.g. Tech Solutions", "pt": "Ex: Tech Solutions", "fr": "Ex : Tech Solutions",
        "de": "z.B. Tech Solutions", "it": "Es: Tech Solutions", "ja": "例: Tech Solutions", "ko": "예: Tech Solutions",
        "zh_Hans": "例如：科技创新有限公司", "ar": "مثال: حلول التقنية", "ru": "Например: Tech Solutions", "hi": "उदा: टेक सॉल्यूशंस"
    },
    "2021 - Presente": {
        "es": "2021 - Presente", "en": "2021 - Present", "pt": "2021 - Presente", "fr": "2021 - Présent",
        "de": "2021 - Heute", "it": "2021 - Presente", "ja": "2021 - 現在", "ko": "2021 - 현재",
        "zh_Hans": "2021 - 至今", "ar": "2021 - الحاضر", "ru": "2021 - настоящее время", "hi": "2021 - वर्तमान"
    },
    "Ej: App de Delivery": {
        "es": "Ej: App de Delivery", "en": "e.g. Delivery App", "pt": "Ex: App de Entregas", "fr": "Ex : App de Livraison",
        "de": "z.B. Liefer-App", "it": "Es: App di Consegne", "ja": "例: フードデリバリーアプリ", "ko": "예: 배달 애플리케이션",
        "zh_Hans": "例如：外卖配送应用", "ar": "مثال: تطبيق توصيل", "ru": "Например: Сервис доставки", "hi": "उदा: डिलीवरी ऐप"
    },
    "Ej: Proyecto Personal": {
        "es": "Ej: Proyecto Personal", "en": "e.g. Personal Project", "pt": "Ex: Projeto Pessoal", "fr": "Ex : Projet Personnel",
        "de": "z.B. Persönliches Projekt", "it": "Es: Progetto Personale", "ja": "例: 個人プロジェクト", "ko": "예: 개인 프로젝트",
        "zh_Hans": "例如：个人项目", "ar": "مثال: مشروع شخصي", "ru": "Например: Личный проект", "hi": "उदा: व्यक्तिगत परियोजना"
    },
    "2023": {
        "es": "2023", "en": "2023", "pt": "2023", "fr": "2023",
        "de": "2023", "it": "2023", "ja": "2023", "ko": "2023",
        "zh_Hans": "2023", "ar": "2023", "ru": "2023", "hi": "2023"
    },
    "Ej: Desarrollador Full Stack Senior": {
        "es": "Ej: Desarrollador Full Stack Senior", "en": "e.g. Senior Full Stack Developer", "pt": "Ex: Desenvolvedor Full Stack Sênior", "fr": "Ex : Développeur Full Stack Sénior",
        "de": "z.B. Senior Full Stack Entwickler", "it": "Es: Sviluppatore Full Stack Senior", "ja": "例: シニアフルスタックエンジニア", "ko": "예: 시니어 풀스택 개발자",
        "zh_Hans": "例如：资深全栈工程师", "ar": "مثال: مطور برمجيات متقدم", "ru": "Например: Senior Full Stack разработчик", "hi": "उदा: वरिष्ठ फुल स्टैक डेवलपर"
    },
    "Acerca de mí": {
        "es": "Acerca de mí", "en": "About me", "pt": "Sobre mim", "fr": "À propos de moi",
        "de": "Über mich", "it": "Su di me", "ja": "自己紹介", "ko": "내 소개",
        "zh_Hans": "关于我", "ar": "عني", "ru": "Обо мне", "hi": "मेरे बारे में"
    },
    "Activa": {
        "es": "Activa", "en": "Active", "pt": "Ativa", "fr": "Active",
        "de": "Aktiv", "it": "Attiva", "ja": "有効", "ko": "활성",
        "zh_Hans": "生效中", "ar": "نشط", "ru": "Активно", "hi": "सक्रिय"
    },
    "Activa para que tu empresa sea visible en el directorio": {
        "es": "Activa para que tu empresa sea visible en el directorio", "en": "Enable so your company is visible in the directory",
        "pt": "Ative para que sua empresa fique visível no diretório", "fr": "Activez pour que votre entreprise soit visible dans l'annuaire",
        "de": "Aktivieren, damit dein Unternehmen im Verzeichnis sichtbar ist", "it": "Attiva per rendere visibile la tua azienda nella directory",
        "ja": "企業をディレクトリに表示するには有効にしてください", "ko": "기업 디렉토리에 표시되도록 활성화하세요",
        "zh_Hans": "开启后企业将在目录中可见", "ar": "فعّل لتظهر شركتك في الدليل", "ru": "Включите, чтобы компания отображалась в каталоге",
        "hi": "निर्देशिका में कंपनी दिखाने के लिए सक्रिय करें"
    },
    "Actualizar descripción": {
        "es": "Actualizar descripción", "en": "Update description", "pt": "Atualizar descrição", "fr": "Mettre à jour la description",
        "de": "Beschreibung aktualisieren", "it": "Aggiorna descrizione", "ja": "説明を更新", "ko": "설명 업데이트",
        "zh_Hans": "更新描述", "ar": "تحديث الوصف", "ru": "Обновить описание", "hi": "विवरण अपडेट करें"
    },
    "Al menos un carácter especial (!@#$%^&*...)": {
        "es": "Al menos un carácter especial (!@#$%^&*...)", "en": "At least one special character (!@#$%^&*...)", "pt": "Pelo menos um caractere especial (!@#$%^&*...)", "fr": "Au moins un caractère spécial (!@#$%^&*...)",
        "de": "Mindestens ein Sonderzeichen (!@#$%^&*...)", "it": "Almeno un carattere speciale (!@#$%^&*...)", "ja": "1文字以上の特殊文字（!@#$%^&*...）", "ko": "특수 문자 1개 이상 (!@#$%^&*...)",
        "zh_Hans": "至少包含一个特殊字符（!@#$%^&*...）", "ar": "رمز خاص واحد على الأقل (!@#$%^&*...)", "ru": "Хотя бы один специальный символ (!@#$%^&*...)", "hi": "कम से कम एक विशेष वर्ण (!@#$%^&*...)"
    },
    "Al menos un número": {
        "es": "Al menos un número", "en": "At least one number", "pt": "Pelo menos um número", "fr": "Au moins un chiffre",
        "de": "Mindestens eine Zahl", "it": "Almeno un numero", "ja": "1文字以上の数字", "ko": "숫자 1개 이상",
        "zh_Hans": "至少包含一个数字", "ar": "رقم واحد على الأقل", "ru": "Хотя бы одна цифра", "hi": "कम से कम एक संख्या"
    },
    "Al menos una letra mayúscula": {
        "es": "Al menos una letra mayúscula", "en": "At least one uppercase letter", "pt": "Pelo menos uma letra maiúscula", "fr": "Au moins une majuscule",
        "de": "Mindestens ein Großbuchstabe", "it": "Almeno una lettera maiuscola", "ja": "1文字以上の大文字", "ko": "대문자 1개 이상",
        "zh_Hans": "至少包含一个大写字母", "ar": "حرف كبير واحد على الأقل", "ru": "Хотя бы одна заглавная буква", "hi": "कम से कम एक बड़ा अक्षर"
    },
    "Buscar sector...": {
        "es": "Buscar sector...", "en": "Search sector...", "pt": "Buscar setor...", "fr": "Rechercher un secteur...",
        "de": "Bereich suchen...", "it": "Cerca settore...", "ja": "分野を検索...", "ko": "분야 검색...",
        "zh_Hans": "搜索行业...", "ar": "ابحث عن قطاع...", "ru": "Поиск сектора...", "hi": "क्षेत्र खोजें..."
    },
    "Busco Talento": {
        "es": "Busco Talento", "en": "I'm hiring", "pt": "Busco Talentos", "fr": "Je recrute",
        "de": "Ich suche Talente", "it": "Cerco Talenti", "ja": "人材を探す", "ko": "인재 찾기",
        "zh_Hans": "招募人才", "ar": "أبحث عن مواهب", "ru": "Ищу сотрудников", "hi": "प्रतिभा तलाश रहे हैं"
    },
    "Busco Trabajo": {
        "es": "Busco Trabajo", "en": "I'm looking for work", "pt": "Busco Trabalho", "fr": "Je cherche un emploi",
        "de": "Ich suche Arbeit", "it": "Cerco Lavoro", "ja": "仕事を探す", "ko": "구직 중",
        "zh_Hans": "寻找工作", "ar": "أبحث عن عمل", "ru": "Ищу работу", "hi": "काम तलाश रहे हैं"
    },
    "Búsqueda Avanzada y Scoring": {
        "es": "Búsqueda Avanzada y Scoring", "en": "Advanced Search & Scoring", "pt": "Busca Avançada e Pontuação", "fr": "Recherche avancée et scoring",
        "de": "Erweiterte Suche & Scoring", "it": "Ricerca avanzata e punteggio", "ja": "高度な検索とスコアリング", "ko": "고급 검색 및 스코어링",
        "zh_Hans": "高级搜索与匹配评分", "ar": "بحث متقدم وتقييم", "ru": "Расширенный поиск и оценка", "hi": "उन्नत खोज और स्कोरिंग"
    },
    "Candidato": {
        "es": "Candidato", "en": "Candidate", "pt": "Candidato", "fr": "Candidat",
        "de": "Kandidat", "it": "Candidato", "ja": "候補者", "ko": "구직자",
        "zh_Hans": "候选人", "ar": "مرشح", "ru": "Кандидат", "hi": "उम्मीदवार"
    },
    "Contactar con Candidato": {
        "es": "Contactar con Candidato", "en": "Contact Candidate", "pt": "Contatar Candidato", "fr": "Contacter le candidat",
        "de": "Kandidat kontaktieren", "it": "Contatta candidato", "ja": "候補者に連絡", "ko": "구직자에게 연락",
        "zh_Hans": "联系候选人", "ar": "الاتصال بالمرشح", "ru": "Связаться с кандидатом", "hi": "उम्मीदवार से संपर्क करें"
    },
    "Crea tu perfil en minutos o explora nuestro directorio de empresas y talentos.": {
        "es": "Crea tu perfil en minutos o explora nuestro directorio de empresas y talentos.",
        "en": "Create your profile in minutes or explore our directory of companies and talent.",
        "pt": "Crie seu perfil em minutos ou explore nosso diretório de empresas e talentos.",
        "fr": "Créez votre profil en quelques minutes ou explorez notre répertoire d'entreprises et de talents.",
        "de": "Erstelle dein Profil in wenigen Minuten oder erkunde unser Verzeichnis von Unternehmen und Talenten.",
        "it": "Crea il tuo profilo in pochi minuti o esplora la nostra directory di aziende e talenti.",
        "ja": "数分でプロフィールを作成するか、企業と人材のディレクトリを探索しましょう。",
        "ko": "몇 분 만에 프로필을 만들거나 기업 및 인재 디렉토리를 탐색하세요.",
        "zh_Hans": "几分钟内创建您的个人资料，或探索我们的企业与人才名录。",
        "ar": "أنشئ ملفك الشخصي في دقائق أو استكشف دليل الشركات والمواهب لدينا.",
        "ru": "Создайте профиль за пару минут или исследуйте каталог компаний и талантов.",
        "hi": "मिनटों में अपनी प्रोफ़ाइल बनाएं या कंपनियों और प्रतिभाओं की निर्देशिका देखें।"
    },
    "Crear Nueva Vacante": {
        "es": "Crear Nueva Vacante", "en": "Create New Vacancy", "pt": "Criar Nova Vaga", "fr": "Créer une nouvelle offre",
        "de": "Neue Stelle erstellen", "it": "Crea nuova offerta", "ja": "求人を新規作成", "ko": "새 채용 공고 작성",
        "zh_Hans": "创建新职位", "ar": "إنشاء شاغر جديد", "ru": "Создать вакансию", "hi": "नई रिक्ति बनाएं"
    },
    "Crear Vacante": {
        "es": "Crear Vacante", "en": "Create Vacancy", "pt": "Criar Vaga", "fr": "Créer une offre",
        "de": "Stelle erstellen", "it": "Crea offerta", "ja": "求人作成", "ko": "채용 공고 작성",
        "zh_Hans": "发布职位", "ar": "إنشاء شاغر", "ru": "Опубликовать вакансию", "hi": "रिक्ति बनाएं"
    },
    "Crear una cuenta gratis": {
        "es": "Crear una cuenta gratis", "en": "Create a free account", "pt": "Criar uma conta grátis", "fr": "Créer un compte gratuit",
        "de": "Kostenloses Konto erstellen", "it": "Crea un account gratuito", "ja": "無料アカウント作成", "ko": "무료 계정 만들기",
        "zh_Hans": "免费注册账号", "ar": "إنشاء حساب مجاني", "ru": "Создать бесплатный аккаунт", "hi": "मुफ़्त खाता बनाएं"
    },
    "Cuéntanos sobre tu empresa...": {
        "es": "Cuéntanos sobre tu empresa...", "en": "Tell us about your company...", "pt": "Conte-nos sobre sua empresa...", "fr": "Parlez-nous de votre entreprise...",
        "de": "Erzähle uns von deinem Unternehmen...", "it": "Raccontaci della tua azienda...", "ja": "貴社について教えてください...", "ko": "회사에 대해 알려주세요...",
        "zh_Hans": "介绍一下您的公司...", "ar": "أخبرنا عن شركتك...", "ru": "Расскажите о вашей компании...", "hi": "अपनी कंपनी के बारे में बताएं..."
    },
    "Debe ser un correo corporativo (no Gmail, Yahoo, Hotmail, etc).": {
        "es": "Debe ser un correo corporativo (no Gmail, Yahoo, Hotmail, etc).", "en": "Must be a corporate email (no Gmail, Yahoo, Hotmail, etc).",
        "pt": "Deve ser um e-mail corporativo (não Gmail, Yahoo, Hotmail, etc).", "fr": "Doit être une adresse e-mail professionnelle (pas Gmail, Yahoo, Hotmail, etc.).",
        "de": "Muss eine Firmen-E-Mail-Adresse sein (kein Gmail, Yahoo, Hotmail etc.).", "it": "Deve essere un'email aziendale (non Gmail, Yahoo, Hotmail, ecc.).",
        "ja": "会社用メールアドレスを入力してください（Gmail、Yahoo、Hotmailなどは不可）。", "ko": "회사 이메일이어야 합니다 (Gmail, Yahoo, Hotmail 등 불가).",
        "zh_Hans": "必须使用企业邮箱（不支持 Gmail、Yahoo、Hotmail 等公共邮箱）。", "ar": "يجب أن يكون بريدًا إلكترونيًا رسميًا للشركة (ليس Gmail أو Yahoo أو Hotmail إلخ).",
        "ru": "Укажите корпоративную почту (не Gmail, Yahoo, Hotmail и т.д.).", "hi": "कॉर्पोरेट ईमेल होना आवश्यक है (Gmail, Yahoo, Hotmail आदि नहीं)।"
    },
    "Describe las responsabilidades y requisitos del puesto...": {
        "es": "Describe las responsabilidades y requisitos del puesto...", "en": "Describe the responsibilities and requirements of the position...",
        "pt": "Descreva as responsabilidades e requisitos da vaga...", "fr": "Décrivez les responsabilités et exigences du poste...",
        "de": "Beschreibe die Aufgaben und Anforderungen der Position...", "it": "Descrivi le responsabilità e i requisiti del ruolo...",
        "ja": "職務内容と応募要件について記述してください...", "ko": "직무의 책임 및 자격 요건을 설명하세요...",
        "zh_Hans": "描述该职位的职责和要求...", "ar": "صف مسؤوليات ومتطلبات الوظيفة...",
        "ru": "Опишите обязанности и требования к вакансии...", "hi": "पद की जिम्मेदारियों और आवश्यकताओं का वर्णन करें..."
    },
    "Descubre empresas y reclutadores en diferentes sectores.": {
        "es": "Descubre empresas y reclutadores en diferentes sectores.", "en": "Discover companies and recruiters across different sectors.",
        "pt": "Descubra empresas e recrutadores em diferentes setores.", "fr": "Découvrez des entreprises et recruteurs dans divers secteurs.",
        "de": "Entdecke Unternehmen und Recruiter in verschiedenen Branchen.", "it": "Scopri aziende e recruiter in diversi settori.",
        "ja": "さまざまな分野の企業や採用担当者を見つけましょう。", "ko": "다양한 분야의 기업과 채용 담당자를 만나보세요.",
        "zh_Hans": "发现不同行业的企业与招聘方。", "ar": "اكتشف الشركات ومسؤولي التوظيف في مختلف القطاعات.",
        "ru": "Находите компании и рекрутеров в различных секторах.", "hi": "विभिन्न क्षेत्रों की कंपनियों और नियोक्ताओं को खोजें।"
    },
    "Explorar tablón de candidatos": {
        "es": "Explorar tablón de candidatos", "en": "Explore candidate board", "pt": "Explorar quadro de candidatos", "fr": "Explorer le tableau des candidats",
        "de": "Kandidaten-Pinnwand erkunden", "it": "Esplora bacheca candidati", "ja": "候補者ボードを見る", "ko": "구직자 게시판 둘러보기",
        "zh_Hans": "浏览人才板", "ar": "استكشف لوحة المرشحين", "ru": "Смотреть доску кандидатов", "hi": "उम्मीदवार बोर्ड देखें"
    },
    "Explorar tablón de reclutadores": {
        "es": "Explorar tablón de reclutadores", "en": "Explore recruiter board", "pt": "Explorar quadro de recrutadores", "fr": "Explorer le tableau des recruteurs",
        "de": "Recruiter-Pinnwand erkunden", "it": "Esplora bacheca recruiter", "ja": "企業ボードを見る", "ko": "채용 공고 게시판 둘러보기",
        "zh_Hans": "浏览企业职位板", "ar": "استكشف لوحة مسؤولي التوظيف", "ru": "Смотреть доску вакансий", "hi": "नियोक्ता बोर्ड देखें"
    },
    "Explorar tablón público sin registro": {
        "es": "Explorar tablón público sin registro", "en": "Explore public board without registering", "pt": "Explorar quadro público sem registro", "fr": "Explorer le tableau public sans inscription",
        "de": "Öffentliche Pinnwand ohne Registrierung ansehen", "it": "Esplora la bacheca pubblica senza registrazione", "ja": "登録なしで公開ボードを見る", "ko": "가입 없이 공개 게시판 둘러보기",
        "zh_Hans": "无需注册直接浏览公开展示板", "ar": "استكشف اللوحة العامة دون تسجيل", "ru": "Смотреть публичную доску без регистрации", "hi": "बिना पंजीकरण के सार्वजनिक बोर्ड देखें"
    },
    "Inicia sesión aquí": {
        "es": "Inicia sesión aquí", "en": "Log in here", "pt": "Faça login aqui", "fr": "Connectez-vous ici",
        "de": "Hier anmelden", "it": "Accedi qui", "ja": "こちらからログイン", "ko": "여기서 로그인",
        "zh_Hans": "在此登录", "ar": "سجّل الدخول هنا", "ru": "Войти здесь", "hi": "यहाँ लॉग इन करें"
    },
    "Ir a tablón de reclutadores": {
        "es": "Ir a tablón de reclutadores", "en": "Go to recruiter board", "pt": "Ir para o quadro de recrutadores", "fr": "Aller au tableau des recruteurs",
        "de": "Zur Recruiter-Pinnwand", "it": "Vai alla bacheca recruiter", "ja": "採用企業ボードへ", "ko": "채용 공고 게시판으로 이동",
        "zh_Hans": "前往招聘展示板", "ar": "الانتقال إلى لوحة التوظيف", "ru": "Перейти к доске вакансий", "hi": "नियोक्ता बोर्ड पर जाएं"
    },
    "Ir a tablón de trabajadores": {
        "es": "Ir a tablón de trabajadores", "en": "Go to talent board", "pt": "Ir para o quadro de talentos", "fr": "Aller au tableau des talents",
        "de": "Zur Kandidaten-Pinnwand", "it": "Vai alla bacheca talenti", "ja": "求職者ボードへ", "ko": "인재 게시판으로 이동",
        "zh_Hans": "前往求职人才板", "ar": "الانتقال إلى لوحة المواهب", "ru": "Перейти к доске талантов", "hi": "प्रतिभा बोर्ड पर जाएं"
    },
    "La plataforma que redefine el CV tradicional en un perfil profesional interactivo.": {
        "es": "La plataforma que redefine el CV tradicional en un perfil profesional interactivo.",
        "en": "The platform that redefines traditional CVs into interactive professional profiles.",
        "pt": "A plataforma que redefine o currículo tradicional em um perfil profissional interativo.",
        "fr": "La plateforme qui transforme le CV traditionnel en profil professionnel interactif.",
        "de": "Die Plattform, die den klassischen Lebenslauf in ein interaktives Profil verwandelt.",
        "it": "La piattaforma che ridefinisce il CV tradizionale in un profilo professionale interattivo.",
        "ja": "従来の履歴書をインタラクティブな職務プロフィールへと刷新するプラットフォーム。",
        "ko": "전통적인 이력서를 인터랙티브 전문가 프로필로 재정의하는 플랫폼.",
        "zh_Hans": "将传统简历升级为互动式职业名片的全新平台。",
        "ar": "المنصة التي تعيد صياغة السيرة الذاتية التقليدية إلى ملف مهني تفاعلي.",
        "ru": "Платформа, превращающая традиционное резюме в интерактивный профиль.",
        "hi": "पारंपरिक सीवी को एक इंटरैक्टिव पेशेवर प्रोफ़ाइल में बदलने वाला मंच।"
    },
    "Limpiar filtros": {
        "es": "Limpiar filtros", "en": "Clear filters", "pt": "Limpar filtros", "fr": "Effacer les filtres",
        "de": "Filter zurücksetzen", "it": "Cancella filtri", "ja": "フィルターをクリア", "ko": "필터 초기화",
        "zh_Hans": "清除筛选", "ar": "مسح الفلاتر", "ru": "Сбросить фильтры", "hi": "फ़िल्टर साफ़ करें"
    },
    "Mínimo 8 caracteres": {
        "es": "Mínimo 8 caracteres", "en": "At least 8 characters", "pt": "Mínimo de 8 caracteres", "fr": "Au moins 8 caractères",
        "de": "Mindestens 8 Zeichen", "it": "Almeno 8 caratteri", "ja": "8文字以上", "ko": "최소 8자 이상",
        "zh_Hans": "至少8个字符", "ar": "8 أحرف على الأقل", "ru": "Не менее 8 символов", "hi": "कम से कम 8 वर्ण"
    },
    "Nombre de Empresa": {
        "es": "Nombre de Empresa", "en": "Company Name", "pt": "Nome da Empresa", "fr": "Nom de l'entreprise",
        "de": "Unternehmensname", "it": "Nome dell'azienda", "ja": "会社名", "ko": "회사명",
        "zh_Hans": "公司名称", "ar": "اسم الشركة", "ru": "Название компании", "hi": "कंपनी का नाम"
    },
    "Nombre de tu empresa": {
        "es": "Nombre de tu empresa", "en": "Your company name", "pt": "Nome da sua empresa", "fr": "Nom de votre entreprise",
        "de": "Name deines Unternehmens", "it": "Nome della tua azienda", "ja": "貴社の社名", "ko": "회사 이름",
        "zh_Hans": "贵公司名称", "ar": "اسم شركتك", "ru": "Название вашей компании", "hi": "आपकी कंपनी का नाम"
    },
    "Nombre y apellidos": {
        "es": "Nombre y apellidos", "en": "Full name", "pt": "Nome completo", "fr": "Nom et prénom",
        "de": "Vor- und Nachname", "it": "Nome e cognome", "ja": "氏名", "ko": "성명",
        "zh_Hans": "姓名", "ar": "الاسم الكامل", "ru": "Имя и фамилия", "hi": "पूरा नाम"
    },
    "Registrarme como Candidato": {
        "es": "Registrarme como Candidato", "en": "Register as Candidate", "pt": "Cadastrar como Candidato", "fr": "S'inscrire comme Candidat",
        "de": "Als Kandidat registrieren", "it": "Registrati come Candidato", "ja": "求職者として登録", "ko": "구직자로 등록",
        "zh_Hans": "注册为求职人才", "ar": "التسجيل كمرشح", "ru": "Зарегистрироваться как соискатель", "hi": "उम्मीदवार के रूप में पंजीकरण करें"
    },
    "Registrarme como Reclutador": {
        "es": "Registrarme como Reclutador", "en": "Register as Recruiter", "pt": "Cadastrar como Recrutador", "fr": "S'inscrire comme Recruteur",
        "de": "Als Recruiter registrieren", "it": "Registrati come Recruiter", "ja": "採用担当者として登録", "ko": "채용 담당자로 등록",
        "zh_Hans": "注册为招聘方", "ar": "التسجيل كمسؤول توظيف", "ru": "Зарегистрироваться как рекрутер", "hi": "नियोक्ता के रूप में पंजीकरण करें"
    },
    "Requisitos de la contraseña:": {
        "es": "Requisitos de la contraseña:", "en": "Password requirements:", "pt": "Requisitos da senha:", "fr": "Exigences du mot de passe :",
        "de": "Passwortanforderungen:", "it": "Requisiti della password:", "ja": "パスワード要件:", "ko": "비밀번호 요구사항:",
        "zh_Hans": "密码要求：", "ar": "متطلبات كلمة المرور:", "ru": "Требования к паролю:", "hi": "पासवर्ड की आवश्यकताएं:"
    },
    "Sitio Web": {
        "es": "Sitio Web", "en": "Website", "pt": "Site", "fr": "Site Web",
        "de": "Webseite", "it": "Sito Web", "ja": "ウェブサイト", "ko": "웹사이트",
        "zh_Hans": "官方网站", "ar": "الموقع الإلكتروني", "ru": "Веб-сайт", "hi": "वेबसाइट"
    },
    "Sobre la empresa": {
        "es": "Sobre la empresa", "en": "About the company", "pt": "Sobre a empresa", "fr": "À propos de l'entreprise",
        "de": "Über das Unternehmen", "it": "Informazioni sull'azienda", "ja": "企業について", "ko": "회사 소개",
        "zh_Hans": "关于公司", "ar": "عن الشركة", "ru": "О компании", "hi": "कंपनी के बारे में"
    },
    "Ubicación": {
        "es": "Ubicación", "en": "Location", "pt": "Localização", "fr": "Lieu",
        "de": "Standort", "it": "Posizione", "ja": "所在地", "ko": "위치",
        "zh_Hans": "所在地", "ar": "الموقع", "ru": "Местоположение", "hi": "स्थान"
    },
    "¿Listo para impulsar tu carrera o escalar tu equipo?": {
        "es": "¿Listo para impulsar tu carrera o escalar tu equipo?", "en": "Ready to boost your career or scale your team?",
        "pt": "Pronto para impulsionar sua carreira ou expandir sua equipe?", "fr": "Prêt à booster votre carrière ou agrandir votre équipe ?",
        "de": "Bereit, deine Karriere voranzutreiben oder dein Team zu vergrößern?", "it": "Pronto a dare slancio alla tua carriera o far crescere il tuo team?",
        "ja": "キャリアを加速させ、またはチームを拡大する準備はできましたか？", "ko": "커리어를 도약시키거나 팀을 확장할 준비가 되셨나요?",
        "zh_Hans": "准备好提升您的职业生涯或组建强大团队了吗？", "ar": "هل أنت مستعد لتعزيز مسيرتك المهنية أو توسيع فريقك؟",
        "ru": "Готовы ускорить карьеру или масштабировать команду?", "hi": "क्या आप अपने करियर को बढ़ावा देने या टीम बढ़ाने के लिए तैयार हैं?"
    },
    "¿Por qué TalentStack?": {
        "es": "¿Por qué TalentStack?", "en": "Why TalentStack?", "pt": "Por que TalentStack?", "fr": "Pourquoi TalentStack ?",
        "de": "Warum TalentStack?", "it": "Perché TalentStack?", "ja": "TalentStackが選ばれる理由", "ko": "왜 TalentStack인가요?",
        "zh_Hans": "为什么选择 TalentStack？", "ar": "لماذا TalentStack؟", "ru": "Почему TalentStack?", "hi": "TalentStack क्यों?"
    },
    "¿Qué estás buscando en la plataforma?": {
        "es": "¿Qué estás buscando en la plataforma?", "en": "What are you looking for on the platform?",
        "pt": "O que você está procurando na plataforma?", "fr": "Que recherchez-vous sur la plateforme ?",
        "de": "Was suchst du auf der Plattform?", "it": "Cosa cerchi sulla piattaforma?",
        "ja": "このプラットフォームで何をお探しですか？", "ko": "플랫폼에서 무엇을 찾고 계신가요?",
        "zh_Hans": "您在寻找什么？", "ar": "عما تبحث في المنصة؟", "ru": "Что вы ищете на платформе?",
        "hi": "आप इस मंच पर क्या खोज रहे हैं?"
    },
    "¿Ya tienes una cuenta con Google, GitHub o LinkedIn?": {
        "es": "¿Ya tienes una cuenta con Google, GitHub o LinkedIn?", "en": "Already have an account with Google, GitHub, or LinkedIn?",
        "pt": "Já tem uma conta com Google, GitHub ou LinkedIn?", "fr": "Avez-vous déjà un compte avec Google, GitHub ou LinkedIn ?",
        "de": "Hast du bereits ein Konto bei Google, GitHub oder LinkedIn?", "it": "Hai già un account con Google, GitHub o LinkedIn?",
        "ja": "Google、GitHub、LinkedInのアカウントをお持ちですか？", "ko": "Google, GitHub 또는 LinkedIn 계정이 이미 있으신가요?",
        "zh_Hans": "已有 Google、GitHub 或 LinkedIn 账号？", "ar": "هل لديك حساب بالفعل مع Google أو GitHub أو LinkedIn؟",
        "ru": "Уже есть аккаунт Google, GitHub или LinkedIn?", "hi": "क्या आपके पास पहले से Google, GitHub या LinkedIn खाता है?"
    }

}

def update_po_files():
    for lang in LANGUAGES:
        po_path = f"locale/{lang}/LC_MESSAGES/django.po"
        mo_path = f"locale/{lang}/LC_MESSAGES/django.mo"
        if not os.path.exists(po_path):
            print(f"Skipping missing: {po_path}")
            continue

        po = polib.pofile(po_path)
        existing_entries = {entry.msgid: entry for entry in po}
        
        updated_count = 0
        added_count = 0
        unfuzzied_count = 0

        for msgid, translations in DATA.items():
            trans_text = translations.get(lang, translations.get('en', msgid))
            
            if msgid in existing_entries:
                entry = existing_entries[msgid]
                was_fuzzy = 'fuzzy' in entry.flags
                if was_fuzzy:
                    entry.flags.remove('fuzzy')
                    unfuzzied_count += 1
                
                # If msgstr is empty or was fuzzy or incorrect
                if not entry.msgstr.strip() or was_fuzzy or lang != 'es':
                    entry.msgstr = trans_text
                    updated_count += 1
            else:
                new_entry = polib.POEntry(
                    msgid=msgid,
                    msgstr=trans_text,
                )
                po.append(new_entry)
                existing_entries[msgid] = new_entry
                added_count += 1

        # Also check all remaining fuzzy entries in the PO file and remove fuzzy flag if translation exists
        for entry in po:
            if 'fuzzy' in entry.flags:
                entry.flags.remove('fuzzy')
                unfuzzied_count += 1

        po.save(po_path)
        po.save_as_mofile(mo_path)
        print(f"[{lang}] Successfully updated: {added_count} added, {updated_count} updated, {unfuzzied_count} unfuzzied. Saved to {mo_path}")

if __name__ == '__main__':
    update_po_files()
