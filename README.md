# 💎 KRONOS UNIVERSAL CUSTOM EMOJI SYSTEM (1.3K+ ASSETS)
> **Lead Architect & Developer:** Aryan ([@thatonearyan](https://t.me/thatonearyan))  
> **System Identity:** ˹ 𝗔 𝗥 𝗬 𝗔 𝗡 ˼  
> **Active Inventory:** 1,316 High-Definition Telegram Animated Custom Emojis | 1,471 Named Semantic Tokens  
> **Universal Module Location:** `/Users/aryan/Desktop/CUSTOM EMOJIS/`

---

## 📖 Table of Contents
1. [Introduction & Purpose](#1-introduction--purpose)
2. [Folder Architecture](#2-folder-architecture)
3. [How Custom Emojis Work in Telegram Messages](#3-how-custom-emojis-work-in-telegram-messages)
   - [The HTML Tag Syntax](#the-html-tag-syntax)
   - [⚠️ The Critical Golden Rule of Fallback Characters](#️-the-critical-golden-rule-of-fallback-characters)
   - [Automatic Text Upgrades (`premiumize_text`)](#automatic-text-upgrades-premiumize_text)
   - [Manual Tag Insertion (`custom_tag`)](#manual-tag-insertion-custom_tag)
4. [How to Insert Premium Emojis into Inline Buttons](#4-how-to-insert-premium-emojis-into-inline-buttons)
   - [`icon_custom_emoji_id` in Aiogram 3.x](#icon_custom_emoji_id-in-aiogram-3x)
   - [The High-Level `styled_btn()` Factory](#the-high-level-styled_btn-factory)
5. [How to Set COLOR to Any Button (Exhaustive Masterclass)](#5-how-to-set-color-to-any-button-exhaustive-masterclass)
   - [Technique 1: Native Bot API 7.0+ Button Styles](#technique-1-native-bot-api-70-button-styles)
   - [Technique 2: Chromatic Animated Icon Anchors](#technique-2-chromatic-animated-icon-anchors)
   - [Technique 3: Telegram Mini App (Web App) Full RGB/Hex Control](#technique-3-telegram-mini-app-web-app-full-rgbhex-control)
   - [Technique 4: Unicode Badges & Text Contrast](#technique-4-unicode-badges--text-contrast)
6. [How to Discover & Add New Custom Emojis](#6-how-to-discover--add-new-custom-emojis)
7. [Full Pack Directory & Cheat Sheet](#7-full-pack-directory--cheat-sheet)

---

## 1. Introduction & Purpose

This directory (`CUSTOM EMOJIS`) is the **single source of truth** for all Telegram custom animated emoji assets across the entire Aryan ecosystem (Kronos Casino, Kronos SMM Panel, Kronos Prime, Telegram Bots, and Web Apps).

Whenever you start a new bot or modify an existing project, simply import from or copy this folder. It provides instant access to 1,316 verified, production-tested Telegram custom stickers that render natively on iOS, Android, macOS, and Windows.

---

## 2. Folder Architecture

```text
CUSTOM EMOJIS/
├── custom_emojis.py          # Master Python module
├── __init__.py               # Python package export (allows 'import custom_emojis')
├── named_emoji_registry.json # Machine-readable JSON dictionary of all 1,316 items
├── ALL_NAMED_EMOJIS.txt      # Human-readable full inventory with IDs, icons & 1-line gaps
├── demo.py                   # Runnable test script & interactive showcase
└── README.md                 # This comprehensive production manual
```

### Quick Import in Any Project:
```python
import sys
sys.path.insert(0, "/Users/aryan/Desktop/CUSTOM EMOJIS")

from custom_emojis import (
    custom_tag,          # Generates <tg-emoji> tags by semantic name or ID
    styled_btn,          # Creates InlineKeyboardButton with custom icon & color style
    premiumize_text,     # Automatically converts standard emojis in text to custom emojis
    calendar_day_tag,    # Dynamic flip calendar day stickers (1-31)
    calendar_weekday_tag,# Dynamic weekday stickers (MON-SUN)
    calendar_month_tag,  # Dynamic month stickers (JAN-DEC)
    school_number_tag,   # Playful 3D school number font
    EMOJI_ICONS          # Dict of 1,471 pre-mapped semantic icon tokens
)
```

---

## 3. How Custom Emojis Work in Telegram Messages

Telegram renders custom animated emojis in chat messages through Telegram Bot API entity tags.

### The HTML Tag Syntax

```html
<tg-emoji emoji-id="5215221866607716402">🏫</tg-emoji>
```

- **`emoji-id`**: The permanent 64-bit integer ID of the custom sticker.
- **`Fallback character`** (`🏫`): The unicode emoji placed between the tags. This is shown to users on outdated Telegram clients or when notifications pop up.
- **`parse_mode`**: You **MUST** specify `parse_mode=ParseMode.HTML` (or `"HTML"`) when calling `bot.send_message()`.

---

### ⚠️ The Critical Golden Rule of Fallback Characters

> [!CAUTION]
> **NEVER USE COMPOUND EMOJIS INSIDE `<tg-emoji>` TAGS!**  
> Telegram strictly enforces that the fallback content inside `<tg-emoji>` must represent **exactly ONE Unicode code point**.
>
> If you put any of the following inside `<tg-emoji>`:
> - Compound emojis with Zero-Width Joiners (ZWJ), e.g., `👨‍💻` (`U+1F468 U+200D U+1F4BB`)
> - Multi-byte emojis with gender/skin tones, e.g., `🤷‍♂️`, `❤️‍🔥`
> - Two characters together, e.g., `10`
>
> Telegram Bot API will instantly crash your request with:  
> `TelegramBadRequest: Bad Request: can't parse entities: ENTITY_TEXT_INVALID`

#### Safe vs Unsafe Fallbacks:
| ❌ Dangerous (Causes Bot Crash) | ✅ 100% Safe Fallback |
|:---|:---|
| `<tg-emoji emoji-id="...">👨‍💻</tg-emoji>` | `<tg-emoji emoji-id="...">💻</tg-emoji>` |
| `<tg-emoji emoji-id="...">❤️‍🔥</tg-emoji>` | `<tg-emoji emoji-id="...">🔥</tg-emoji>` |
| `<tg-emoji emoji-id="...">🤷‍♂️</tg-emoji>` | `<tg-emoji emoji-id="...">🤷</tg-emoji>` |
| `<tg-emoji emoji-id="...">10</tg-emoji>` | `<tg-emoji emoji-id="...">🔟</tg-emoji>` |

Our `custom_tag()` function automatically enforces this rule and guarantees safe fallbacks.

---

### Automatic Text Upgrades (`premiumize_text`)

Instead of manually wrapping every emoji in `<tg-emoji>`, simply write natural text and run it through `premiumize_text()`:

```python
from custom_emojis import premiumize_text

# Raw input message
raw = "Welcome to Kronos Casino! 🎰 Roll the dice 🎲 and win 💎 diamonds! 🚀"

# Converts to Telegram custom emojis automatically
formatted = premiumize_text(raw)

await bot.send_message(chat_id=user_id, text=formatted, parse_mode="HTML")
```

#### Protecting Native Emojis (`<raw>` tag)
If you specifically want a standard emoji to remain untouched without being upgraded to custom animation, wrap it in `<raw>...</raw>`:
```python
text = premiumize_text("Custom diamond 💎 vs native diamond <raw>💎</raw>")
```

---

### Manual Tag Insertion (`custom_tag`)

For maximum precision, generate tags using semantic names:

```python
from custom_emojis import custom_tag

msg = (
    f"{custom_tag('VIOLET_TROPHY')} <b>CHAMPIONSHIP ANNOUNCEMENT</b>\n\n"
    f"• Game: {custom_tag('TBOI_RED_D6_DIE')} High Stakes Roulette\n"
    f"• Prize: {custom_tag('VIOLET_DIAMOND')} 5,000 USDT\n"
    f"• Date : {custom_tag('CALENDAR_MON')} {custom_tag('CALENDAR_DAY_12')}"
)
await bot.send_message(chat_id, msg, parse_mode="HTML")
```

---

## 4. How to Insert Premium Emojis into Inline Buttons

In modern Telegram Bot API (v6.5+ / v7.0+), buttons can display **animated custom emoji icons** on their left edge.

### `icon_custom_emoji_id` in Aiogram 3.x

```python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Play Dice Game",
            callback_data="game_dice",
            icon_custom_emoji_id="5199918773578016345"  # TBOI Red 3D D6 Dice
        )
    ]
])
```

---

### The High-Level `styled_btn()` Factory

The `custom_emojis` module provides `styled_btn()`, which eliminates ID lookups and automatically cleans up duplicate icons:

```python
from custom_emojis import styled_btn
from aiogram.types import InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        styled_btn(
            text="Claim Daily Gift",
            callback_data="claim_gift",
            icon="VIOLET_TROPHY",       # Direct semantic token name
            style="success"             # Green color palette
        ),
        styled_btn(
            text="VIP Lounge",
            callback_data="vip_lounge",
            icon="VIOLET_DIAMOND",      # Violet diamond icon
            style="primary"             # Blue brand accent
        )
    ],
    [
        styled_btn(
            text="Emergency Cancel",
            callback_data="cancel_action",
            icon="TBOI_SACRED_HEART",   # Flaming red heart
            style="danger"              # Red alert color
        )
    ],
    [
        styled_btn(
            text="Open Web App Portal",
            web_app_url="https://kronos.app",
            icon="EDU_LAPTOP"           # White laptop icon
        )
    ]
])
```

> **Why `styled_btn()` is superior:** If you pass `text="🎲 Roll Dice"`, `styled_btn()` detects that an animated custom icon is already assigned and automatically strips the redundant unicode `🎲` from the label, rendering clean, professional typography!

---

## 5. How to Set COLOR to Any Button (Exhaustive Masterclass)

Telegram does not provide arbitrary CSS background colors for inline chat buttons. However, professional bots achieve vibrant button coloring using **four proven production techniques**:

### Technique 1: Native Bot API 7.0+ Button Styles

Telegram Bot API 7.0+ introduced the `style` parameter on `InlineKeyboardButton`:

```python
# 1. PRIMARY (Brand Accent Blue / Active Theme Color)
styled_btn("Confirm Order", callback_data="confirm", style="primary")

# 2. SUCCESS (Vibrant Green — Approvals, Payments, Bonuses)
styled_btn("Add Funds", callback_data="deposit", style="success")

# 3. DANGER (Alert Red — Deletions, Exits, Cancelations)
styled_btn("Delete Account", callback_data="delete", style="danger")
```

When rendered on modern Telegram clients supporting Bot API 7.0+, these buttons display the designated accent, green, or red tint.

---

### Technique 2: Chromatic Animated Icon Anchors

Every custom animated sticker has a dominant, glowing color. Placing high-contrast custom emojis on buttons gives them instant visual color identity:

| Desired Color Theme | Recommended Custom Icon Token | Visual Vibe |
|:---|:---|:---|
| 🟣 **Violet / Neon Purple** | `VIOLET_DIAMOND`, `VIOLET_TROPHY`, `VIOLET_HEART` | Luxury, Royalty, Crypto |
| 🔴 **Ruby Red / Danger** | `TBOI_RED_D6_DIE`, `TBOI_SACRED_HEART`, `TBOI_BLOOD_BOTTLE` | Casino, Stakes, Critical Alerts |
| 🟢 **Emerald Green / Cash** | `SCHOOL_GRADE_5_PLUS`, `PVZ_1UP_MUSHROOM`, `SCHOOL_CHECKMARK_GREEN` | Profit, Approval, Wallets |
| 🟡 **Gold / Amber** | `TBOI_DOLLAR_BILLS`, `TBOI_GOLDEN_COMPASS`, `AXOLOTL_STAR_5_PUFFY` | VIP, Jackpots, Coins |
| 🔵 **Cyan / Ice Blue** | `AXOLOTL_PEARL_SPHERE`, `TBOI_BLUE_ORB`, `AXOLOTL_STAR_4_BIG` | Tech, Support, Info |
| ⚪ **Pearl / Minimalist** | `AXOLOTL_CLAM_PEARL`, `TBOI_WHITE_URN`, `AXOLOTL_SEASHELL` | Elegance, Clean UI |

---

### Technique 3: Telegram Mini App (Web App) Full RGB/Hex Control

When maximum visual customization is required (e.g. gradients, shadows, borders, custom hex codes), use a **Telegram Mini App** via `web_app=WebAppInfo(...)`.

Inside the Web App JavaScript, you have 100% unrestricted control over button colors:

```javascript
// Set the Telegram native bottom bar button color to ANY hex code:
Telegram.WebApp.MainButton.setText("⚡ CONFIRM $5,000 DEPOSIT");
Telegram.WebApp.MainButton.setColor("#8B5CF6"); // Electric Purple
Telegram.WebApp.MainButton.setTextColor("#FFFFFF");
Telegram.WebApp.MainButton.show();

// Set Secondary Action Button
Telegram.WebApp.SecondaryButton.setText("CANCEL");
Telegram.WebApp.SecondaryButton.setColor("#EF4444"); // Alert Red
Telegram.WebApp.SecondaryButton.show();
```

Inside the Mini App HTML/CSS, you can use modern CSS:
```css
.neon-button {
  background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
  box-shadow: 0 0 20px rgba(168, 85, 247, 0.4);
  border-radius: 12px;
  color: #fff;
  font-weight: 700;
}
```

---

### Technique 4: Unicode Badges & Text Contrast

You can reinforce button colors using high-contrast Unicode badge chips in the button label:

```python
# Green badge
styled_btn("🟢 ACTIVE  |  SMM Server #1", callback_data="srv_1")

# Red badge
styled_btn("🔴 OFFLINE |  Backup Server", callback_data="srv_2")

# Yellow badge
styled_btn("🟡 PENDING |  Awaiting Confirm", callback_data="srv_3")

# Mathematical Bold text for emphasis
styled_btn("⚡ 𝗕𝗨𝗬 𝗞𝗥𝗢𝗡𝗢𝗦 𝗣𝗔𝗦𝗦", callback_data="buy_pass", icon="VIOLET_DIAMOND")
```

---

## 6. How to Discover & Add New Custom Emojis

Whenever you find a new Telegram sticker pack or custom emoji set:

1. **Get the 64-bit ID**:
   - Open Telegram and forward the emoji/sticker to [@GetEmojiIdBot](https://t.me/GetEmojiIdBot) or [@fStikBot](https://t.me/fStikBot).
   - The bot replies with the 64-bit numerical ID (e.g. `[5215221866607716402]`).

2. **Register in `custom_emojis.py`**:
   - Add the ID and its semantic name to `EMOJI_ICONS`:
     ```python
     EMOJI_ICONS["MY_NEW_TOKEN"] = "5215221866607716402"
     ```

3. **Register in `named_emoji_registry.json`**:
   - Add it to the JSON file so all scripts and bots see it automatically.

---

## 7. Full Pack Directory & Cheat Sheet

| # | Pack Name | Item Count | Fallback | Primary Theme / Typical Use |
|:---:|:---|:---:|:---:|:---|
| 1 | **Violet Flame** | 75 | 🔥 | Glowing purple neon font (A-Z, А-Я, 0-9), trophy, diamond, hearts |
| 2 | **Autumn 2024** | 103 | 🍂 | Cozy aesthetic, leaves, pumpkins, lanterns, coffee, fire |
| 3 | **PVZ: DS** | 138 | 🌱 | Retro pixel-art plants, zombies, coins, cherry bomb, potato mine |
| 4 | **Loki** | 33 | 🎭 | TVA aesthetic, time doors, temp pads, golden horns, dagger, wine toast |
| 5 | **Education 2026** | 200 | 🏫 | Laptops (#185), stars (#186), chat bubbles (#187), microscopes, trophies |
| 6 | **TBOI** | 171 | 😭 | Isaac characters, Red D6 Gaming Dice (#155), Sacred Heart, Godhead |
| 7 | **Axolotl Font** | 119 | 🤍 | 3D pastel iridescent balloon letters, digits, punctuation, dividers, hands |
| 8 | **Calendar** | 54 | 📅 | Daily flip days 1-31, weekdays Mon-Sun (#33-#39), months Jan-Dec (#41-#52) |
| 9 | **Back to School** | 134 | 📚 | 3D playful school digits (0-9), cursive notebooks, illustrated Cyrillic |
| 10 | **StickerXtara (NFT)** | 105 | ⭐ | Expressive 3D characters, sunglasses, playful luxury avatars |
| 11 | **Snoopcar (NFT)** | 50 | 🚗 | Automotive, gifts, wheels, speed badges, urban culture |
| 12 | **Pellegrrrxtara (NFT)**| 134 | 💎 | High-fashion characters, handshakes, gestures, street style |
| 🏆 | **TOTAL** | **1,316** | — | **1,471 Named Tokens Available Across All Engines** |

---

## 🚀 Interactive Test & Verification

To verify that the custom emoji engine is working properly on any machine, simply run:

```bash
python3 demo.py
```

To send a live interactive showcase message directly to your Telegram chat:
```bash
python3 demo.py --live
```

---
*Created by Aryan for the Kronos Ecosystem. All Rights Reserved (C) 2026.*
