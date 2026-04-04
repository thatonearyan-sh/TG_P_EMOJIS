# ==============================================================================
# 💎 KRONOS ECOSYSTEM — ULTIMATE MASTER TELEGRAM CUSTOM EMOJI SYSTEM (1.1K+ ASSETS)
# 👑 LEAD ARCHITECT & DEVELOPER: Aryan (@thatonearyan)
# 🌐 TELEGRAM: https://t.me/thatonearyan
# ⚔️ SYSTEM IDENTITY: ˹ 𝗔 𝗥 𝗬 𝗔 𝗡 ˼
# ⚠️ COPYRIGHT (C) 2026 ARYAN. ALL RIGHTS RESERVED.
# ==============================================================================
from __future__ import annotations
import functools
import re
from typing import Optional
from aiogram.types import InlineKeyboardButton, WebAppInfo

EMOJI_ICONS: dict[str, str] = {
    "AI": "5296447931627352804",
    "BACK": "5409284148491726576",
    "BLACKJACK": "5445353829304387411",
    "BOLT": "5258203794772085854",
    "CARD": "5445353829304387411",
    "CART": "6296218646284863141",
    "CASINO": "5816539591812845173",
    "CELEBRATE": "5409029744693897259",
    "CHART": "6057406808086023473",
    "CHECK": "6339289076545358952",
    "CHERRY_BOMB": "5265219396216861036",
    "COIN": "5039789890133296083",
    "COMMUNITY": "5296533616224906961",
    "CRASH": "5389057356493511934",
    "CROSS": "6053019808230805244",
    "CROWN": "5816539591812845173",
    "DEPOSIT": "5445353829304387411",
    "DESIGN": "5427168083074628963",
    "DEV": "5816539591812845173",
    "DIAMOND": "5408854995359524419",
    "DICE": "5199918773578016345",
    "EDUCATION": "5211146604068757567",
    "FACEBOOK": "5296533616224906961",
    "FIRE": "6129792056589031358",
    "GIFT": "5409029744693897259",
    "GLOBE": "5224450179368767019",
    "GOLD_MAGNET": "5265084173466512423",
    "GOLD_NUGGET": "5265077198439623133",
    "HEART": "5409029744693897259",
    "HOME": "5474534700401833481",
    "HOT_PEPPER": "5262672660998958523",
    "INFO": "5211146604068757567",
    "INSTAGRAM": "6129792056589031358",
    "JACKPOT": "5408854995359524419",
    "LEADERBOARD": "5204046146955153467",
    "MAIL": "4929524417354007168",
    "MINES": "5040034664614462519",
    "MONEY": "5039789890133296083",
    "NETFLIX": "5445353829304387411",
    "OTHER": "5224450179368767019",
    "PHONE": "5346136537123801643",
    "POTATO_MINE": "5264996281255767745",
    "REFRESH": "5030872266716480568",
    "ROCKET": "5389057356493511934",
    "ROULETTE": "5310278924616356636",
    "SEARCH": "5258011929993026890",
    "SETTINGS": "5863945989127148135",
    "SHIELD": "5980930633298350051",
    "SHOP": "5409230963911701228",
    "SLOTS": "5408854995359524419",
    "STAR": "5438496463044752972",
    "STARFRUIT": "5265078456865041208",
    "SUPPORT": "5866185084427572234",
    "TELEGRAM": "6296218646284863141",
    "TIKTOK": "5438496463044752972",
    "TRADING": "6057406808086023473",
    "TWITTER": "5258203794772085854",
    "USERS": "5296533616224906961",
    "VIDEO": "5258500400918587241",
    "VIP": "5816539591812845173",
    "WHATSAPP": "5346136537123801643",
    "WITHDRAW": "5039789890133296083",
    "YOUTUBE": "5258500400918587241",
}

MESSAGE_EMOJI_IDS: dict[str, str] = {}

_EMOJI_REGEX = None
_EMOJI_PREFIX_REGEX = re.compile(r'^[\w\s]+')

def premiumize_text(text: str) -> str:
    return text

def get_custom_emoji_id(identifier: str) -> Optional[str]:
    """
    Returns the Telegram custom emoji ID for either a Unicode emoji (e.g. '💎')
    or a named icon key (e.g. 'CHERRY_BOMB', 'PIXEL_DIAMOND', 'TBOI_DICE_D6').
    """
    if identifier in MESSAGE_EMOJI_IDS:
        return MESSAGE_EMOJI_IDS[identifier]
    upper_id = identifier.upper()
    if upper_id in EMOJI_ICONS:
        return EMOJI_ICONS[upper_id]
    return None

def custom_tag(symbol_or_name: str, fallback: str = "🔥") -> str:
    """
    Generates a single <tg-emoji emoji-id="..."> HTML tag for use in messages.
    """
    eid = get_custom_emoji_id(symbol_or_name)
    if not eid:
        # Check if identifier is already numeric emoji-id
        if symbol_or_name.isdigit():
            eid = symbol_or_name
        else:
            return fallback or symbol_or_name
    return f'<tg-emoji emoji-id="{eid}">{fallback}</tg-emoji>'

def styled_btn(text: str, **kwargs) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, **kwargs)
