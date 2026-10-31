# -*- coding: utf-8 -*-
import os, json

LOCALES_DIR = r"d:\Nitin\removesynth\apps\removesynth\src\content\locales"

def save(code, var_name, data):
    with open(os.path.join(LOCALES_DIR, f"{code}.ts"), "w", encoding="utf-8") as f:
        f.write(f"import type {{ HomeContent }} from '../types';\n\nexport const {var_name}: HomeContent = {json.dumps(data, ensure_ascii=False, indent=2)};\n")
    print(f"Saved {code}.ts")

# 9. ZH (Simplified Chinese)
save("zh", "zh", {
  "lang": "zh",
  "title": "SynthID 水印去除工具免费在线版：支持AI图像与视频",
  "description": "免费在线去除AI图像与视频中的谷歌SynthID隐形水印及C2PA元数据。纯浏览器端无损处理，支持PNG、JPG、WebP、MP4和MOV，不上传服务器保护隐私。",
  "hero": {
    "eyebrow": "免注册 · 完全免费 · 图像、视频与音频",
    "h1Before": "免费 ",
    "h1Accent": "SynthID 去除工具",
    "h1After": " 在线版",
    "lead": "去除AI生成图像与视频中的谷歌SynthID隐形数字水印。一键上传处理，以原画质和格式导出干净的媒体文件。",
    "checks": ["支持图像、视频与音频", "处理视频全量帧", "处理完毕即刻永久销毁"],
    "worksWith": "广泛兼容以下工具生成的内容："
  },
  "features": [
    { "title": "图像与视频全支持", "text": "支持PNG、JPG、WebP静态图及MP4、WebM、MOV视频的一站式清洗。" },
    { "title": "全视频帧深度处理", "text": "对于视频文件，逐帧执行无损滤波，绝不跳过任何过渡帧。" },
    { "title": "保留原始画质", "text": "分辨率、格式编码与视频帧率100%保持不变，零画质损失。" },
    { "title": "免登录即用", "text": "无需注册账号或绑定手机，拖入文件即可秒级处理。" },
    { "title": "隐私绝对安全", "text": "处理完成后即刻从临时存储中销毁，不存储任何用户资产。" },
    { "title": "全平台设备通用", "text": "电脑、平板、手机等各类主流浏览器均可流畅极速运行。" }
  ],
  "inside": {
    "kicker": "深入了解AI媒体标记机制",
    "h2": "主流AI内容的两大隐形标记方式",
    "p": "当今主流AI生成工具普遍会自动嵌入人眼不可见的溯源标识。",
    "cards": [
      {
        "kicker": "谷歌 · SynthID",
        "title": "植入像素底层的隐形频域信号",
        "html": "SynthID直接交织在图像频域数据与视频每一帧中，具有极强的鲁棒性，抗裁切、抗滤镜、抗压缩。<a href=\"/what-is-synthid/\">了解SynthID原理</a>"
      },
      {
        "kicker": "C2PA · 内容凭证 (Content Credentials)",
        "title": "文件元数据中的加密来源签名",
        "html": "诸多生成模型还会附带C2PA加密元数据，详细记录该文件是由AI模型所创建的完整日志。"
      }
    ]
  },
  "how": {
    "kicker": "操作指南",
    "h2": "简单四步彻底清除SynthID水印",
    "steps": [
      { "title": "选择并上传文件", "text": "选取由Gemini、Imagen或Veo等生成的AI图片或视频文件。" },
      { "title": "确认处理权限", "text": "勾选声明框，确认您拥有该文件的处置权限与使用权。" },
      { "title": "云端/本地算法处理", "text": "系统自动对文件进行逐帧特征检测与水印中和净化。" },
      { "title": "对比并下载", "text": "实时对比处理前后效果，一键下载原格式干净文件。" }
    ]
  },
  "plans": {
    "kicker": "服务计划",
    "h2": "公测期间全部功能无限制免费开放",
    "p": "早期访问阶段内所有核心功能均无门槛免费使用。",
    "free": {
      "name": "免费公测版",
      "note": "无需绑定任何支付方式",
      "items": ["图像与视频全面支持", "单文件上限高达50MB", "保持100%原生画质", "无需注册账号"],
      "cta": "立即处理文件"
    },
    "pro": {
      "badge": "即将推出",
      "price": "点数制",
      "note": "月度或年度灵活订阅",
      "items": ["支持更大体积与超长视频", "批量并发多文件清洗", "极速独享算力通道", "开放REST API接口"]
    }
  },
  "hood": {
    "kicker": "底层架构与安全规范",
    "h2": "专为极致画质与隐私守护而打造",
    "cards": [
      { "title": "全帧无缝扫描", "text": "完整遍历视频从首帧到末帧的所有画面序列。", "tag": "第1帧 → 240帧 · 处理完成" },
      { "title": "绝对零数据残留", "text": "文件仅在临时隔离沙箱中流转，下载即焚。", "tag": "保留文件数 0" },
      { "title": "原生色彩与分辨率", "text": "精确维持色域、分辨率及帧率规格。", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "适用人群",
    "h2": "赋能每一位AI数字内容创作者",
    "cards": [
      { "title": "内容创作者", "text": "自制AI创意作品，需要导出没有额外隐形水印的纯净底稿。" },
      { "title": "科研与评测人员", "text": "从事数字水印鲁棒性测试、取证与AI标识对抗技术研究。" },
      { "title": "软件开发者", "text": "构建自动化数字媒体流水线，需要批量去除AI隐形标记。" }
    ],
    "note": "请仅处理您拥有合法权利的文件，并遵循数字内容透明与诚信规范。"
  },
  "seo": [
    {
      "h2": "如何在线去除SynthID隐形水印？",
      "html": "只需将文件拖放至上方输入框，勾选权限确认并点击<strong>开始处理文件</strong>，完成后即可下载去除SynthID的水印文件。"
    },
    { "h2": "哪些AI工具会自带SynthID标记？", "html": "谷歌旗下各类生成式AI产品均已集成SynthID，包括Gemini网页端/App、Imagen 3以及Veo视频生成模型。" },
    {
      "h2": "为什么简单的裁剪和截屏无法去除SynthID？",
      "html": "SynthID并非外挂角标，而是通过算法嵌入在像素色彩分布的统计规律中。普通裁剪或截图仍会保留足够多的统计特征，唯有专业算法方可彻底中和。"
    }
  ],
  "faqHeading": "常见问题解答",
  "faqs": [
    { "q": "什么是SynthID去除工具？", "a": "这是一款专门用于中和并消除谷歌嵌入在AI图像和视频中的SynthID不可见水印的专业工具。" },
    { "q": "该工具是否完全免费？", "a": "是的，在当前的早期体验期间，RemoveSynth对所有用户完全免费开放。" },
    { "q": "支持哪些文件格式？", "a": "支持PNG、JPG、WebP格式图片，以及MP4、WebM、MOV格式视频。" },
    { "q": "平台会保存我的文件吗？", "a": "绝对不会。所有上传文件仅用于即时处理，下载完毕后系统会自动永久物理删除。" },
    { "q": "截屏能去掉SynthID吗？", "a": "不能。谷歌在设计SynthID时就专门强化了抗截屏、抗缩放和抗重新编码的能力。" },
    { "q": "RemoveSynth与谷歌官方有关联吗？", "a": "没有。RemoveSynth是由独立团队开发的第三方工具，SynthID是谷歌公司的注册商标。" }
  ],
  "cta": { "h2": "立即体验SynthID去除工具", "p": "无需注册，完全免费，极速处理图像与视频。", "button": "立即开始去除水印" }
})

# 10. ZH-TW (Traditional Chinese)
save("zh-tw", "zhTw", {
  "lang": "zh-tw",
  "title": "SynthID 水印去除工具免費線上版：支援AI圖像與影片",
  "description": "免費線上消除AI圖像與影片中的Google SynthID隱形浮水印與C2PA元資料。純瀏覽器端無失真處理，支援PNG、JPG、WebP、MP4與MOV，保障隱私。",
  "hero": {
    "eyebrow": "免註冊 · 完全免費 · 圖像、影片與音訊",
    "h1Before": "免費 ",
    "h1Accent": "SynthID 去除工具",
    "h1After": " 線上版",
    "lead": "快速消除AI生成圖像與影片中的Google SynthID不可見浮水印。一鍵上傳處理，保留原始畫質與解析度下載乾淨檔案。",
    "checks": ["支援圖像、影片與音訊", "處理影片全部影格", "下載完成即刻安全銷毀"],
    "worksWith": "支援以下主流AI模型檔案："
  },
  "features": [
    { "title": "圖像與影片全支援", "text": "支援PNG、JPG、WebP相片以及MP4、WebM、MOV影片一網打盡。" },
    { "title": "全影格深度無失真處理", "text": "針對影片檔案逐影格處理，絕不遺漏任何中間影格。" },
    { "title": "保留原生高畫質", "text": "解析度、格式與FPS影格率完全無損保留。" },
    { "title": "無需註冊會員", "text": "拖放檔案即可立即處理，無需填寫個資或綁定信箱。" },
    { "title": "嚴格保障隱私", "text": "檔案在處理結束後立即從伺服器永久刪除，絕不留存。" },
    { "title": "跨裝置流暢運行", "text": "電腦、平板、手機皆可透過現代瀏覽器隨時隨地使用。" }
  ],
  "inside": {
    "kicker": "解析AI檔案隱形標籤",
    "h2": "AI內容的兩大隱藏標記機制",
    "p": "現今主流AI工具在生成內容時，皆會埋入肉眼無法看見的溯源信號。",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "植入像素底層的不可見頻率信號",
        "html": "SynthID直接編碼至影像像素資料與影片每秒影格中，可抵抗裁切、縮放與濾鏡。"
      },
      {
        "kicker": "C2PA · 內容憑證 (Content Credentials)",
        "title": "元資料中的數位簽章紀錄",
        "html": "許多模型還會附加C2PA加密證明，紀錄此檔案由生成式AI演算法產生的歷程。"
      }
    ]
  },
  "how": {
    "kicker": "操作教學",
    "h2": "四步驟輕鬆消除SynthID浮水印",
    "steps": [
      { "title": "拖曳上傳檔案", "text": "選擇由Gemini、Imagen或Veo等AI工具輸出的相片或影片。" },
      { "title": "確認檔案處分權", "text": "勾選確認方塊，聲明您具備該檔案的完整使用權利。" },
      { "title": "自動去除運算", "text": "系統自動針對像素進行訊號解構與浮水印過濾。" },
      { "title": "下載純淨檔案", "text": "即時預覽前後差異，立即下載原始格式無浮水印版本。" }
    ]
  },
  "plans": {
    "kicker": "方案與定價",
    "h2": "先行測試期間全站功能完全免費",
    "p": "公測體驗期間所有功能皆無限量免費開放。",
    "free": {
      "name": "免費公測版",
      "note": "無需提供信用卡",
      "items": ["支援圖像與影片處理", "單檔上限50MB", "100%維持原始畫質", "免註冊免登入"],
      "cta": "立即上傳處理"
    },
    "pro": {
      "badge": "即將登場",
      "price": "點數制",
      "note": "按月或按年靈活訂閱",
      "items": ["支援更大檔案與超長影片", "多檔批次同時處理", "優先專屬算力隊列", "提供API串接"]
    }
  },
  "hood": {
    "kicker": "技術標準與隱私承諾",
    "h2": "以高規格品質與資訊安全為核心",
    "cards": [
      { "title": "全影格連續清理", "text": "從第一格到最後一格完整掃描，不跳過任何影格。", "tag": "影格 1 → 240 · 處理完畢" },
      { "title": "零資料留存", "text": "暫存目錄在使用者下載後自動徹底銷毀。", "tag": "0 檔案儲存" },
      { "title": "原生色彩與畫素", "text": "保持原始解析度與色彩表現。", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "適用對象",
    "h2": "為專業AI創作者量身打造",
    "cards": [
      { "title": "內容創作者", "text": "自行構思創作AI影音，期望保有乾淨原始的作品檔。" },
      { "title": "數位鑑識與學術研究", "text": "評估數位水印演算法抗干擾強度與AI辨識技術。" },
      { "title": "系統開發者", "text": "需要將媒體清理流程整合至自動化生產管線中。" }
    ],
    "note": "請務必僅處理您合法擁有的檔案，並遵循內容誠信原則。"
  },
  "seo": [
    {
      "h2": "如何線上移除SynthID隱形浮水印？",
      "html": "將相片或影片拖放到上方區域，勾選權利宣告並點選<strong>處理檔案</strong>，即可下載消除浮水印的成品。"
    },
    { "h2": "哪些生成工具會加入SynthID？", "html": "Google旗下如Gemini、Imagen 3及Veo等AI產品皆內建SynthID。" },
    {
      "h2": "為何截圖或轉檔無法清除SynthID？",
      "html": "因為SynthID是融入像素的深層訊號，截圖與一般轉檔依舊會攜帶該訊號，需依賴專門的對消工具才能清除。"
    }
  ],
  "faqHeading": "常見問題",
  "faqs": [
    { "q": "什麼是SynthID浮水印消除工具？", "a": "這是專門用來中和並清除Google在AI圖像與影片中嵌入的不可見SynthID水印的工具。" },
    { "q": "使用這項工具需要付費嗎？", "a": "目前處於公測體驗階段，所有人皆可完全免費使用。" },
    { "q": "支援哪些副檔名？", "a": "支援PNG、JPG、WebP靜態圖片，以及MP4、WebM、MOV動態影片。" },
    { "q": "網站會儲存我的檔案嗎？", "a": "不會。所有檔案在處理並提供下載後，便會即時自動銷毀。" },
    { "q": "裁切圖片能消除SynthID嗎？", "a": "無法完全消除，SynthID的設計具有高強度抗裁切特性。" },
    { "q": "RemoveSynth是Google的產品嗎？", "a": "不是，RemoveSynth為獨立開發的第三方分析工具。" }
  ],
  "cta": { "h2": "立即清除SynthID浮水印", "p": "免註冊、無費用、支援多種格式圖像與影片。", "button": "馬上開始去除" }
})

# 11. KO (Korean)
save("ko", "ko", {
  "lang": "ko",
  "title": "SynthID 제거 온라인 무료: AI 이미지 및 비디오 워터마크 제거",
  "description": "AI 생성 이미지 및 동영상에서 Google SynthID 비가시성 워터마크와 C2PA 메타데이터를 무손실로 제거합니다. 서버 업로드 없는 100% 브라우저 기반 무료 도구.",
  "hero": {
    "eyebrow": "가입 불필요 · 완전 무료 · 이미지, 비디오 및 오디오 지원",
    "h1Before": "무료 온라인 ",
    "h1Accent": "SynthID 제거",
    "h1After": " 도구",
    "lead": "AI가 생성한 이미지와 영상에 포함된 Google SynthID 보이지 않는 워터마크를 제거하세요. 파일 업로드 후 원본 해상도와 화질 그대로 다운로드할 수 있습니다.",
    "checks": ["이미지, 영상, 오디오 완벽 지원", "모든 비디오 프레임 처리", "처리 후 즉시 파일 영구 삭제"],
    "worksWith": "다음 AI 도구의 생성물과 완벽 호환:"
  },
  "features": [
    { "title": "이미지 및 동영상 지원", "text": "PNG, JPG, WebP 이미지와 MP4, WebM, MOV 동영상을 한 번에 처리합니다." },
    { "title": "전체 프레임 완전 제거", "text": "동영상의 일부 구간만이 아닌 모든 프레임을 처음부터 끝까지 정밀 처리합니다." },
    { "title": "원본 화질 100% 유지", "text": "해상도, 색상 프로필, 프레임 레이트 저하 없이 무손실로 보존됩니다." },
    { "title": "회원가입 없음", "text": "계정 생성이나 로그인 없이 파일을 드래그하여 바로 시작할 수 있습니다." },
    { "title": "철저한 개인정보 보호", "text": "작업 완료 즉시 임시 서버에서 안전하게 영구 파기됩니다." },
    { "title": "모든 디바이스 호환", "text": "PC, 태블릿, 모바일의 모든 최신 웹 브라우저에서 구동됩니다." }
  ],
  "inside": {
    "kicker": "AI 파일 구조 분석",
    "h2": "AI 생성 콘텐츠가 마킹되는 두 가지 방식",
    "p": "대부분의 최신 생성형 AI 도구는 육안으로 보이지 않는 추적 신호를 삽입합니다.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "픽셀 내부에 심어진 보이지 않는 신호",
        "html": "SynthID는 이미지 픽셀 데이터와 비디오 프레임에 정밀하게 각인되어 자르기, 필터 적용, 재압축에도 견디도록 제작되었습니다."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "메타데이터에 암호화된 생성 이력",
        "html": "많은 도구가 AI가 제작했다는 디지털 출처 인증서를 메타데이터 영역에 보관합니다."
      }
    ]
  },
  "how": {
    "kicker": "이용 방법",
    "h2": "단 4단계로 SynthID 워터마크 말끔히 제거",
    "steps": [
      { "title": "파일 드래그 업로드", "text": "Gemini, Imagen, Veo 등에서 생성된 이미지나 비디오를 선택합니다." },
      { "title": "이용 권리 확인", "text": "파일을 처리할 정당한 권리가 있음을 체크박스에 확인합니다." },
      { "title": "자동 워터마크 제거", "text": "알고리즘이 SynthID 신호를 감지하고 프레임별로 깨끗이 중화합니다." },
      { "title": "결과물 다운로드", "text": "전후 상태를 확인하고 원본 확장자 그대로 깨끗한 파일을 다운로드합니다." }
    ]
  },
  "plans": {
    "kicker": "이용 요금",
    "h2": "얼리 액세스 기간 동안 전 기능 완전 무료",
    "p": "현재 모든 핵심 기능을 제한 없이 무료로 제공하고 있습니다.",
    "free": {
      "name": "무료 플랜",
      "note": "신용카드 등록 필요 없음",
      "items": ["이미지 및 비디오 처리", "파일당 최대 50MB 지원", "원본 해상도 유지", "회원가입 불필요"],
      "cta": "파일 처리 시작하기"
    },
    "pro": {
      "badge": "출시 예정",
      "price": "크레딧 방식",
      "note": "월간 또는 연간 플랜",
      "items": ["대용량 파일 & 장편 비디오", "다중 파일 일괄 처리", "초고속 우선 처리", "API 연동 지원"]
    }
  },
  "hood": {
    "kicker": "기술 사양 & 프라이버시",
    "h2": "최고의 화질 유지와 완벽한 프라이버시 보장",
    "cards": [
      { "title": "프레임 누락 제로", "text": "첫 프레임부터 마지막 프레임까지 하나도 빠짐없이 처리합니다.", "tag": "프레임 1 → 240 완료" },
      { "title": "파일 저장 없음", "text": "다운로드 준비 완료와 동시에 임시 저장 파일이 즉각 파기됩니다.", "tag": "저장된 파일 0개" },
      { "title": "원본 품질 보존", "text": "해상도와 프레임 레이트가 그대로 유지됩니다.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "추천 대상",
    "h2": "직접 만든 AI 미디어를 관리하는 크리에이터를 위해",
    "cards": [
      { "title": "콘텐츠 크리에이터", "text": "스스로 프롬프트를 입력해 만든 창작물을 불필요한 마커 없이 깔끔하게 보관하려는 분." },
      { "title": "연구원 및 저널리스트", "text": "디지털 워터마크의 견고성과 AI 식별 기술을 연구하는 전문가." },
      { "title": "개발자", "text": "미디어 처리 자동화 파이프라인 구축을 계획 중인 엔지니어." }
    ],
    "note": "본인이 권리를 소유하고 있거나 허가받은 파일에만 사용하시기 바랍니다."
  },
  "seo": [
    {
      "h2": "SynthID 워터마크를 제거하는 방법은?",
      "html": "상단 업로드 영역에 파일을 끌어다 놓은 뒤 권리 확인에 동의하고 <strong>파일 처리</strong> 버튼을 누르면 워터마크가 제거된 파일을 받을 수 있습니다."
    },
    { "h2": "SynthID를 사용하는 AI 플랫폼은?", "html": "Google의 Gemini 앱, Imagen 3, Veo 동영상 생성 모델 등이 대표적입니다." },
    {
      "h2": "단순한 이미지 자르기로는 왜 제거되지 않나요?",
      "html": "SynthID는 특정 모서리에 위치한 로고가 아니라 픽셀 전반에 미세하게 분포된 수학적 신호이므로 전용 알고리즘으로만 완전히 제거할 수 있습니다."
    }
  ],
  "faqHeading": "자주 묻는 질문",
  "faqs": [
    { "q": "SynthID 제거 도구란 무엇인가요?", "a": "Google이 생성형 AI 결과물에 삽입하는 비가시성 SynthID 워터마크를 무손실로 제거해주는 전문 도구입니다." },
    { "q": "비용이 드나요?", "a": "아닙니다. 현재 얼리 액세스 기간에는 누구나 100% 무료로 사용할 수 있습니다." },
    { "q": "지원하는 파일 형식은 무엇인가요?", "a": "PNG, JPG, WebP 이미지 및 MP4, WebM, MOV 동영상을 지원합니다." },
    { "q": "업로드한 파일이 보관되나요?", "a": "아닙니다. 처리가 끝나고 다운로드가 완료되는 즉시 시스템에서 영구히 삭제됩니다." },
    { "q": "화면을 캡처하면 워터마크가 지워지나요?", "a": "아닙니다. SynthID는 스크린샷이나 리사이징 후에도 유지되도록 설계되어 있습니다." },
    { "q": "RemoveSynth는 Google 공식 서비스인가요?", "a": "아닙니다. RemoveSynth는 독립적으로 개발된 서드파티 웹 도구입니다." }
  ],
  "cta": { "h2": "지금 바로 SynthID를 제거해보세요", "p": "가입 불필요, 100% 무료, 고화질 이미지와 동영상 완벽 지원.", "button": "워터마크 지금 제거하기" }
})

# 12. TH (Thai)
save("th", "th", {
  "lang": "th",
  "title": "ลบ SynthID ออนไลน์ ฟรี: สำหรับรูปภาพและวิดีโอ AI",
  "description": "เครื่องมือลบลายน้ำ SynthID ฟรีสำหรับรูปภาพและวิดีโอที่สร้างด้วย AI กำจัดลายน้ำที่มองไม่เห็นของ Google และ C2PA ในเบราว์เซอร์โดยไม่ลดทอนคุณภาพ.",
  "hero": {
    "eyebrow": "ไม่ต้องลงทะเบียน · ฟรี · รูปภาพ วิดีโอ และเสียง",
    "h1Before": "ฟรี ",
    "h1Accent": "ลบลายน้ำ SynthID",
    "h1After": " ออนไลน์",
    "lead": "ลบลายน้ำ SynthID ที่มองไม่เห็นจากรูปภาพและวิดีโอที่สร้างด้วย AI อัปโหลดไฟล์ ประมวลผลในคลิกเดียว และดาวน์โหลดในคุณภาพเดิม.",
    "checks": ["รองรับรูปภาพ วิดีโอ และเสียง", "ประมวลผลทุกเฟรมของวิดีโอ", "ลบไฟล์ทันทีหลังประมวลผลเสร็จ"],
    "worksWith": "ทำงานร่วมกับไฟล์จาก"
  },
  "features": [
    { "title": "รูปภาพและวิดีโอ", "text": "เครื่องมือเดียวสำหรับ PNG, JPG, WebP และวิดีโอ MP4, WebM, MOV" },
    { "title": "ประมวลผลทุกเฟรม", "text": "สำหรับวิดีโอ คลิปทั้งหมดจะได้รับการประมวลผลทีละเฟรมอย่างสมบูรณ์" },
    { "title": "คุณภาพระดับต้นฉบับ", "text": "ความละเอียด รูปแบบ และอัตราเฟรมคงเดิมไม่เปลี่ยนแปลง" },
    { "title": "ไม่ต้องสมัครสมาชิก", "text": "ลากไฟล์วางแล้วเริ่มได้ทันที ไม่ต้องมีบัญชีผู้ใช้" },
    { "title": "ความปลอดภัยสูงสุด", "text": "ไฟล์จะถูกลบออกจากเซิร์ฟเวอร์ทันทีหลังจากดาวน์โหลดเสร็จ" },
    { "title": "ใช้งานได้ทุกที่", "text": "รองรับบนเบราว์เซอร์ทุกอุปกรณ์ ทั้งคอมพิวเตอร์ แท็บเล็ต และมือถือ" }
  ],
  "inside": {
    "kicker": "สิ่งที่อยู่ในไฟล์ AI",
    "h2": "สองวิธีที่เนื้อหา AI ถูกทำเครื่องหมาย",
    "p": "เครื่องมือ AI ส่วนใหญ่จะทำเครื่องหมายสิ่งที่พวกเขาสร้างขึ้นโดยมองไม่เห็นด้วยตาเปล่า",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "สัญญาณที่มองไม่เห็นในพิกเซล",
        "html": "SynthID ถูกถักทอลงในข้อมูลพิกเซลและทุกเฟรมวิดีโอ ทนทานต่อการครอบตัด ฟิลเตอร์ และการบีบอัด"
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "บันทึกข้อมูลเมตาที่เข้ารหัส",
        "html": "ใบรับรองดิจิทัลที่ฝังอยู่ในข้อมูลเมตาเพื่อระบุว่าสร้างโดย AI"
      }
    ]
  },
  "how": {
    "kicker": "ขั้นตอนการใช้งาน",
    "h2": "ลบ SynthID ใน 4 ขั้นตอนง่ายๆ",
    "steps": [
      { "title": "วางไฟล์ของคุณ", "text": "เลือกรูปภาพหรือวิดีโอจาก Gemini, Imagen หรือ Veo" },
      { "title": "ยืนยันสิทธิ์ของคุณ", "text": "ทำเครื่องหมายในช่องเพื่อยืนยันว่าคุณมีสิทธิ์ในการประมวลผลไฟล์นี้" },
      { "title": "ระบบประมวลผล", "text": "ไฟล์ของคุณจะได้รับการตรวจสอบและลบลายน้ำออกทีละเฟรม" },
      { "title": "ดาวน์โหลด", "text": "ตรวจสอบผลลัพธ์และดาวน์โหลดไฟล์สะอาดในรูปแบบเดิม" }
    ]
  },
  "plans": {
    "kicker": "แพ็กเกจ",
    "h2": "ฟรีในช่วงการเข้าถึงล่วงหน้า (Early Access)",
    "p": "ฟังก์ชันทั้งหมดเปิดให้ใช้งานฟรีโดยไม่มีค่าใช้จ่าย",
    "free": {
      "name": "ฟรี",
      "note": "ไม่ต้องใช้บัตรเครดิต",
      "items": ["รูปภาพและวิดีโอ", "ขนาดไฟล์สูงสุด 50 MB", "คุณภาพระดับต้นฉบับ", "ไม่ต้องสมัครบัญชี"],
      "cta": "เริ่มประมวลผลไฟล์"
    },
    "pro": {
      "badge": "เร็วๆ นี้",
      "price": "เครดิต",
      "note": "รายเดือนหรือรายปี",
      "items": ["ไฟล์ขนาดใหญ่และวิดีโอยาวขึ้น", "ประมวลผลพร้อมกันหลายไฟล์", "คิวประมวลผลด่วน", "การเข้าถึง API"]
    }
  },
  "hood": {
    "kicker": "เบื้องหลังเทคโนโลยี",
    "h2": "สร้างขึ้นเพื่อคุณภาพและความเป็นส่วนตัว",
    "cards": [
      { "title": "ประมวลผลครบทุกเฟรม", "text": "วิดีโอได้รับการจัดการตลอดทั้งคลิปโดยไม่ข้ามเฟรมใดๆ", "tag": "เฟรม 1 → 240 · เสร็จสมบูรณ์" },
      { "title": "ไม่เก็บข้อมูลใดๆ", "text": "ไฟล์จะอยู่ในโฟลเดอร์ชั่วคราวและจะถูกลบทันที", "tag": "เก็บไฟล์ 0 ไฟล์" },
      { "title": "คุณภาพคงเดิม", "text": "ความละเอียดและอัตราเฟรมคงเดิม 100%", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "เหมาะสำหรับใคร",
    "h2": "สร้างขึ้นสำหรับผู้ที่สร้างสื่อ AI ของตนเอง",
    "cards": [
      { "title": "ครีเอเตอร์", "text": "คุณสร้างรูปภาพหรือวิดีโอเองและต้องการไฟล์ที่สะอาดหมดจด" },
      { "title": "นักวิจัย", "text": "คุณกำลังทดสอบความทนทานของลายน้ำดิจิทัล" },
      { "title": "นักพัฒนา", "text": "ต้องการรวมการประมวลผลเข้ากับระบบอัตโนมัติผ่าน API" }
    ],
    "note": "โปรดประมวลผลเฉพาะไฟล์ที่คุณเป็นเจ้าของหรือมีสิทธิ์ตามกฎหมายเท่านั้น"
  },
  "seo": [
    {
      "h2": "วิธีลบลายน้ำ SynthID ออนไลน์",
      "html": "วางไฟล์ลงในช่องด้านบน ยืนยันสิทธิ์ แล้วคลิก <strong>ประมวลผลไฟล์</strong> เพื่อรับผลลัพธ์ที่ปราศจากลายน้ำ"
    },
    { "h2": "เครื่องมือ AI ใดที่ใช้ SynthID?", "html": "Google ใช้ SynthID ในผลิตภัณฑ์ Gemini, Imagen และ Veo" },
    {
      "h2": "ทำไมการครอบตัดรูปภาพจึงไม่สามารถลบ SynthID ได้",
      "html": "SynthID ฝังอยู่ในทุกพิกเซลของภาพ การตัดขอบหรือบันทึกหน้าจอจึงไม่สามารถลบออกได้ ต้องใช้เครื่องมือเฉพาะทางเท่านั้น"
    }
  ],
  "faqHeading": "คำถามที่พบบ่อย",
  "faqs": [
    { "q": "เครื่องมือลบ SynthID คืออะไร?", "a": "เป็นเครื่องมือที่ช่วยลบลายน้ำ SynthID ที่มองไม่เห็นของ Google ออกจากรูปภาพและวิดีโอ AI" },
    { "q": "ใช้งานฟรีหรือไม่?", "a": "ใช่ ฟรีทั้งหมดในช่วงการเข้าถึงล่วงหน้านี้" },
    { "q": "รองรับไฟล์ประเภทใดบ้าง?", "a": "รูปภาพ PNG, JPG, WebP และวิดีโอ MP4, WebM, MOV" },
    { "q": "คุณเก็บไฟล์ของฉันไว้หรือไม่?", "a": "ไม่ ไฟล์จะถูกลบทันทีหลังจากที่คุณดาวน์โหลดเสร็จ" },
    { "q": "การแคปหน้าจอช่วยลบลายน้ำได้หรือไม่?", "a": "ไม่ได้ ลายน้ำ SynthID ออกแบบมาให้ทนทานต่อการแคปหน้าจอ" },
    { "q": "RemoveSynth เกี่ยวข้องกับ Google หรือไม่?", "a": "ไม่ RemoveSynth เป็นเครื่องมืออิสระที่พัฒนาขึ้นเอง" }
  ],
  "cta": { "h2": "ลองใช้เครื่องมือลบ SynthID เลย", "p": "ฟรี ไม่ต้องลงทะเบียน รองรับทั้งรูปภาพและวิดีโอ", "button": "ลบ SynthID ทันที" }
})

# 13. VI (Vietnamese)
save("vi", "vi", {
  "lang": "vi",
  "title": "Xóa SynthID Trực Tuyến Miễn Phí: Hình Ảnh và Video AI",
  "description": "Công cụ xóa hình mờ vô hình SynthID và metadata C2PA từ ảnh và video AI miễn phí. Xử lý 100% trong trình duyệt không nén giảm chất lượng.",
  "hero": {
    "eyebrow": "Không cần đăng ký · Miễn phí · Hình ảnh, video và âm thanh",
    "h1Before": "Miễn phí ",
    "h1Accent": "xóa SynthID",
    "h1After": " trực tuyến",
    "lead": "Xóa hình mờ vô hình SynthID khỏi hình ảnh và video do AI tạo ra. Tải tệp lên, xử lý chỉ trong một cú nhấp chuột và tải xuống với chất lượng gốc nguyên bản.",
    "checks": ["Hỗ trợ ảnh, video & âm thanh", "Xử lý từng khung hình video", "Tệp bị xóa ngay sau khi xử lý"],
    "worksWith": "Tương thích với các tệp từ"
  },
  "features": [
    { "title": "Hình ảnh và video", "text": "Một công cụ duy nhất cho PNG, JPG, WebP và video MP4, WebM, MOV." },
    { "title": "Từng khung hình", "text": "Đối với video, toàn bộ clip được làm sạch từng khung hình đầy đủ." },
    { "title": "Chất lượng gốc", "text": "Độ phân giải, định dạng và tốc độ khung hình được giữ nguyên vẹn." },
    { "title": "Không cần đăng ký", "text": "Chỉ cần kéo thả tệp và bắt đầu ngay mà không cần tài khoản." },
    { "title": "Bảo mật tuyệt đối", "text": "Tệp được xóa vĩnh viễn khỏi máy chủ ngay sau khi hoàn tất tải về." },
    { "title": "Dùng ở mọi nơi", "text": "Chạy mượt mà trên mọi trình duyệt web máy tính và điện thoại." }
  ],
  "inside": {
    "kicker": "Bên trong tệp AI có gì",
    "h2": "Hai cách nội dung AI được đánh dấu bản quyền",
    "p": "Hầu hết các công cụ AI hiện nay đều gắn các dấu vết vô hình vào tệp xuất ra.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Tín hiệu vô hình ẩn sâu trong pixel",
        "html": "SynthID được đan xen vào dữ liệu điểm ảnh và từng khung hình video, chống cắt xén và nén ảnh."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Bản ghi chứng thực trong metadata",
        "html": "Chữ ký số mật mã trong metadata ghi lại quy trình tạo ra tệp bằng trí tuệ nhân tạo."
      }
    ]
  },
  "how": {
    "kicker": "Cách thức hoạt động",
    "h2": "Xóa SynthID chỉ trong 4 bước đơn giản",
    "steps": [
      { "title": "Thả tệp vào đây", "text": "Chọn ảnh hoặc video từ Gemini, Imagen hoặc Veo của Google." },
      { "title": "Xác nhận quyền sở hữu", "text": "Tích vào ô để xác nhận bạn có quyền xử lý tệp này." },
      { "title": "Hệ thống làm sạch", "text": "Tệp của bạn được thuật toán phân tích và trung hòa dấu mờ." },
      { "title": "Tải về máy", "text": "So sánh trước và sau, sau đó tải về tệp sạch ở định dạng gốc." }
    ]
  },
  "plans": {
    "kicker": "Gói dịch vụ",
    "h2": "Miễn phí hoàn toàn trong giai đoạn trải nghiệm sớm",
    "p": "Mọi tính năng hiện đều được mở miễn phí không giới hạn.",
    "free": {
      "name": "Miễn phí",
      "note": "Không cần thẻ tín dụng",
      "items": ["Hình ảnh và video", "Tối đa 50 MB mỗi tệp", "Chất lượng gốc nguyên bản", "Không cần tài khoản"],
      "cta": "Xử lý tệp ngay"
    },
    "pro": {
      "badge": "Sắp ra mắt",
      "price": "Gói tín dụng",
      "note": "Thanh toán theo tháng hoặc năm",
      "items": ["Tệp dung lượng lớn & video dài", "Xử lý hàng loạt", "Hàng đợi ưu tiên", "Truy cập qua API"]
    }
  },
  "hood": {
    "kicker": "Công nghệ & Quyền riêng tư",
    "h2": "Được xây dựng vì chất lượng và sự bảo mật",
    "cards": [
      { "title": "Xử lý không sót khung hình", "text": "Toàn bộ video được làm sạch liên tục từ đầu đến cuối.", "tag": "Khung hình 1 → 240 · Hoàn tất" },
      { "title": "Không lưu trữ tệp", "text": "Thư mục tạm thời bị xóa vĩnh viễn ngay sau khi hoàn thành.", "tag": "0 tệp được lưu" },
      { "title": "Bảo toàn chất lượng", "text": "Độ phân giải và số khung hình/giây giữ nguyên tuyệt đối.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Đối tượng sử dụng",
    "h2": "Dành cho những người tự sáng tạo nội dung AI của mình",
    "cards": [
      { "title": "Nhà sáng tạo nội dung", "text": "Bạn tự tạo hình ảnh/video và muốn có tệp gốc sạch không kèm nhãn ẩn." },
      { "title": "Nhà nghiên cứu", "text": "Thử nghiệm độ bền của các watermark kỹ thuật số." },
      { "title": "Lập trình viên", "text": "Xây dựng hệ thống tự động hóa xử lý tệp đa phương tiện qua API." }
    ],
    "note": "Chỉ xử lý các tệp bạn sở hữu hoặc có quyền hợp pháp."
  },
  "seo": [
    {
      "h2": "Làm thế nào để xóa watermark SynthID trực tuyến?",
      "html": "Thả tệp vào ô bên trên, tích xác nhận và nhấn <strong>Xử lý tệp</strong> để nhận bản tải về sạch hoàn toàn."
    },
    { "h2": "Những công cụ AI nào gắn SynthID?", "html": "Google tích hợp SynthID vào Gemini, Imagen và Veo." },
    {
      "h2": "Tại sao cắt ảnh không xóa được SynthID?",
      "html": "SynthID phân bổ đều khắp các pixel hình ảnh, nên việc crop hay chụp màn hình thông thường không thể loại bỏ được."
    }
  ],
  "faqHeading": "Câu hỏi thường gặp",
  "faqs": [
    { "q": "Công cụ xóa SynthID là gì?", "a": "Đây là công cụ giúp loại bỏ hình mờ kỹ thuật số vô hình SynthID của Google khỏi ảnh và video AI." },
    { "q": "Dịch vụ có miễn phí không?", "a": "Có, hoàn toàn miễn phí trong giai đoạn Early Access." },
    { "q": "Hỗ trợ những định dạng nào?", "a": "Ảnh PNG, JPG, WebP và video MP4, WebM, MOV." },
    { "q": "Tệp của tôi có bị lưu lại không?", "a": "Không, tất cả tệp sẽ được xóa ngay khi tải về xong." },
    { "q": "Chụp màn hình có làm mất SynthID không?", "a": "Không, SynthID được thiết kế để sống sót qua ảnh chụp màn hình." },
    { "q": "RemoveSynth có thuộc Google không?", "a": "Không, RemoveSynth là công cụ độc lập của bên thứ ba." }
  ],
  "cta": { "h2": "Dùng thử công cụ xóa SynthID", "p": "Miễn phí, không cần đăng ký, hỗ trợ cả hình ảnh và video.", "button": "Xóa SynthID ngay" }
})

# 14. ID (Indonesian)
save("id", "id", {
  "lang": "id",
  "title": "Hapus SynthID Online Gratis: Gambar dan Video AI",
  "description": "Alat online gratis penghapus watermark tak terlihat SynthID dan metadata C2PA untuk gambar dan video buatan AI. Diproses langsung di browser tanpa kompresi kualitas.",
  "hero": {
    "eyebrow": "Tanpa daftar · Gratis · Gambar, video & audio",
    "h1Before": "Gratis ",
    "h1Accent": "penghapus SynthID",
    "h1After": " online",
    "lead": "Hapus watermark tak terlihat SynthID dari gambar dan video hasil AI. Unggah file Anda, proses dalam satu klik, dan unduh dengan kualitas aslinya.",
    "checks": ["Gambar, video & audio", "Setiap frame video", "File langsung dihapus setelah diproses"],
    "worksWith": "Mendukung file dari"
  },
  "features": [
    { "title": "Gambar dan video", "text": "Satu alat untuk foto PNG, JPG, WebP dan video MP4, WebM, MOV." },
    { "title": "Setiap frame", "text": "Pada video, seluruh klip diproses frame demi frame tanpa ada yang terlewat." },
    { "title": "Kualitas asli", "text": "Resolusi, format, dan frame rate file Anda tetap terjaga 100% utuh." },
    { "title": "Tanpa registrasi", "text": "Cukup tarik file dan mulai tanpa perlu membuat akun sama sekali." },
    { "title": "Privasi terjamin", "text": "File unggahan langsung dihapus permanen begitu unduhan Anda siap." },
    { "title": "Bisa di mana saja", "text": "Dapat digunakan di browser apa pun di komputer, tablet, atau ponsel." }
  ],
  "inside": {
    "kicker": "Isi di dalam file AI",
    "h2": "Dua cara konten AI diberi tanda pengenal",
    "p": "Sebagian besar alat AI menyisipkan penanda tak kasatmata pada karya yang dibuatnya.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Sinyal tak kasatmata di dalam piksel",
        "html": "SynthID dirajut langsung ke data piksel gambar dan setiap frame video sehingga tahan crop dan kompresi."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Catatan digital di dalam metadata",
        "html": "Sertifikat kriptografis pada metadata yang mencatat bahwa file dibuat oleh AI."
      }
    ]
  },
  "how": {
    "kicker": "Cara kerja",
    "h2": "Hapus SynthID dalam empat langkah mudah",
    "steps": [
      { "title": "Tarik dan letakkan file", "text": "Pilih gambar atau video dari Gemini, Imagen, atau Veo." },
      { "title": "Konfirmasi hak Anda", "text": "Centang kotak untuk mengonfirmasi bahwa Anda berhak memproses file tersebut." },
      { "title": "Proses pembersihan", "text": "File Anda diperiksa dan dibersihkan dari watermark secara otomatis." },
      { "title": "Unduh hasil", "text": "Bandingkan sebelum dan sesudah, lalu unduh file bersih dengan format asli." }
    ]
  },
  "plans": {
    "kicker": "Pilihan Paket",
    "h2": "Gratis selama masa akses awal",
    "p": "Semua fitur dapat digunakan secara gratis tanpa biaya selama periode ini.",
    "free": {
      "name": "Gratis",
      "note": "Tanpa kartu kredit",
      "items": ["Gambar dan video", "Hingga 50 MB per file", "Kualitas asli", "Tanpa perlu akun"],
      "cta": "Proses file sekarang"
    },
    "pro": {
      "badge": "Segera hadir",
      "price": "Kredit",
      "note": "Bulanan atau tahunan",
      "items": ["Ukuran file lebih besar & video panjang", "Pemrosesan massal", "Antrean prioritas", "Akses API"]
    }
  },
  "hood": {
    "kicker": "Teknologi & Privasi",
    "h2": "Dibuat untuk kualitas maksimal dan perlindungan privasi",
    "cards": [
      { "title": "Setiap frame diproses", "text": "Video diproses menyeluruh tanpa ada bagian yang terlewatkan.", "tag": "Frame 1 → 240 · Selesai" },
      { "title": "Tidak ada penyimpanan", "text": "File sementara langsung dimusnahkan setelah pengunduhan selesai.", "tag": "0 file tersimpan" },
      { "title": "Kualitas tanpa kompresi", "text": "Resolusi dan frame rate persis sama dengan file asli.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Target Pengguna",
    "h2": "Dibuat untuk para kreator yang mengelola konten AI mereka sendiri",
    "cards": [
      { "title": "Kreator Konten", "text": "Anda membuat gambar atau video sendiri dan ingin memiliki file bersih tanpa watermark." },
      { "title": "Peneliti & Jurnalis", "text": "Menguji ketahanan watermark digital dan keamanan konten AI." },
      { "title": "Pengembang", "text": "Membangun alur pemrosesan media otomatis menggunakan API." }
    ],
    "note": "Harap hanya memproses file yang Anda miliki atau memiliki izin resmi."
  },
  "seo": [
    {
      "h2": "Bagaimana cara menghapus watermark SynthID?",
      "html": "Unggah file Anda ke kolom di atas, setujui konfirmasi hak cipta, lalu klik <strong>Proses file</strong> untuk mengunduh versi bersih."
    },
    { "h2": "Alat AI apa saja yang menggunakan SynthID?", "html": "Google menyematkan SynthID pada Gemini, Imagen, dan Veo." },
    {
      "h2": "Mengapa cropping tidak bisa menghilangkan SynthID?",
      "html": "SynthID tersebar di seluruh spektrum piksel gambar sehingga crop biasa maupun screenshot tidak akan menghilangkannya."
    }
  ],
  "faqHeading": "Pertanyaan yang Sering Diajukan",
  "faqs": [
    { "q": "Apa itu alat penghapus SynthID?", "a": "Alat khusus untuk menetralkan watermark tak kasatmata SynthID milik Google pada gambar dan video AI." },
    { "q": "Apakah layanan ini gratis?", "a": "Ya, 100% gratis selama masa akses awal berlangsung." },
    { "q": "Format file apa saja yang didukung?", "a": "Gambar PNG, JPG, WebP serta video MP4, WebM, MOV." },
    { "q": "Apakah file saya disimpan?", "a": "Tidak, file langsung dihapus permanen begitu proses selesai." },
    { "q": "Apakah screenshot bisa menghilangkan SynthID?", "a": "Tidak, SynthID dirancang untuk tetap bertahan pada tangkapan layar." },
    { "q": "Apakah RemoveSynth terafiliasi dengan Google?", "a": "Bukan, RemoveSynth adalah alat independen pihak ketiga." }
  ],
  "cta": { "h2": "Coba penghapus SynthID sekarang", "p": "Gratis, tanpa daftar, mendukung gambar dan video.", "button": "Hapus SynthID Sekarang" }
})

print("Batch 2 (East Asia: zh, zh-tw, ko, th, vi, id) completed.")
