import os, sys
# 建议在 streamlit 页面中调整设置
## ======================== 基本设置 ======================== ##
# API 设置 建议使用唯一真神 https://api.wlai.vip, sonnet 价格仅 10r/1M, 也可以（不建议）参考格式修改成你的API
API_KEY = 'sk-xxx'
BASE_URL = 'https://api2.wlai.vip'
MODEL = ['claude-3-5-sonnet-20240620']

# gpt多线程数量
MAX_WORKERS = 8

# 每一步的 LLM 模型选择，其中 3_2 和 5 只建议 sonnet，换模型会不稳定报错
step3_2_split_model = MODEL[0]
step4_1_summarize_model = MODEL[0]
step4_2_translate_direct_model = MODEL[0]
step4_2_translate_free_model = MODEL[0]
step5_align_model = MODEL[0]
step9_trim_model = MODEL[0]

# 语言设置，用自然语言描述
TARGET_LANGUAGE = '简体中文'

# 字幕设置
## 每行英文字幕的最大长度字母数量
MAX_ENGLISH_LENGTH = 80
## 每行翻译字幕的最大长度 根据目标语言调整（如中文为30个字）
MAX_TARGET_LANGUAGE_LENGTH = 30  

# SoVITS角色配置
DUBBNING_CHARACTER = 'Huanyu'

# 视频分辨率
RESOLUTIOM = '854x480'

# whisper 指定语言，auto 为自动识别但目前不用英文后续会有小问题
AUDIO_LANGUAGE = 'en'

## ======================== 进阶设置设置 ======================== ##
# 支持返回 JSON 格式的 LLM，不重要
llm_support_json = ['deepseek-coder', 'gpt-4o']

## 设置趋动云 model dir
cloud = 1 if sys.platform.startswith('linux') else 0
if cloud: # 趋动云
    gemini_pretrain = os.getenv('GEMINI_PRETRAIN')
    cloud_model_dir = os.path.join(gemini_pretrain, "_model_cache") 

# Whisper 和 NLP 配置
MODEL_DIR = "./_model_cache" if not cloud else cloud_model_dir
WHISPER_MODEL = "medium"    # medium :12 GB < GPU > 12GB : large-v2
SPACY_NLP_MODEL = "en_core_web_md"   # _md 足够

# 音频配置
MIN_SUBTITLE_DURATION = 5

# 第一次粗切单词数，18以下会切太碎影响翻译，22 以上太长会导致后续为字幕切分难以对齐
MAX_SPLIT_LENGTH = 18