"""
==============================================================================
💎 KRONOS CUSTOM EMOJI SYSTEM — INTERACTIVE SHOWCASE & DEMO
👑 Architect: Aryan (@thatonearyan)
==============================================================================
This script demonstrates:
  1. Rendering animated custom emojis in text messages via <tg-emoji>
  2. Automatic upgrade of plain emojis to custom stickers via premiumize_text()
  3. Building interactive Inline Buttons with animated custom icons (icon_custom_emoji_id)
  4. Setting button colors, styles, and visual palettes
  5. Sending live interactive messages to Telegram

Usage:
  python3 demo.py
==============================================================================
"""

import asyncio
import os
import sys
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Import the master toolkit
from custom_emojis import (
    custom_tag,
    premiumize_text,
    get_custom_emoji_id,
    styled_btn,
    calendar_day_tag,
    calendar_weekday_tag,
    calendar_month_tag,
    school_number_tag,
    divider_tag,
    EMOJI_ICONS,
    CALENDAR_WEEKDAYS,
    CALENDAR_MONTHS
)


def local_demo():
    print("=" * 70)
    print("💎 KRONOS CUSTOM EMOJI TOOLKIT — LOCAL DEMO")
    print("=" * 70)

    # 1. Generating single tags
    print("\n--- 1. SINGLE CUSTOM EMOJI TAGS ---")
    trophy_tag = custom_tag("VIOLET_TROPHY")
    diamond_tag = custom_tag("VIOLET_DIAMOND")
    heart_tag = custom_tag("TBOI_SACRED_HEART")
    dice_tag = custom_tag("TBOI_RED_D6_DIE")
    print(f"Trophy Tag : {trophy_tag}")
    print(f"Diamond Tag: {diamond_tag}")
    print(f"Heart Tag  : {heart_tag}")
    print(f"Dice Tag   : {dice_tag}")

    # 2. Automated Text Upgrade (premiumize_text)
    print("\n--- 2. AUTOMATIC TEXT UPGRADE (premiumize_text) ---")
    raw_message = "Welcome to Kronos Casino! 🎰 Roll the dice 🎲 and win 💎 diamonds! 🚀"
    upgraded = premiumize_text(raw_message)
    print("Raw Input      :", raw_message)
    print("Upgraded Output:", upgraded)

    # 3. Calendar Engine
    print("\n--- 3. DYNAMIC CALENDAR ENGINE ---")
    print("Today: ", calendar_weekday_tag("MON") + " " + calendar_day_tag(12) + " " + calendar_month_tag("SEP"))

    # 4. School 3D Digit Engine
    print("\n--- 4. 3D SCHOOL NUMBERS ---")
    print("Score: ", school_number_tag("2026"))

    # 5. Inline Keyboard Button with Custom Icon
    print("\n--- 5. INLINE BUTTONS WITH CUSTOM ICONS ---")
    btn1 = styled_btn("Claim Daily Bonus", callback_data="claim_bonus", icon="VIOLET_TROPHY", style="success")
    btn2 = styled_btn("High Roller Casino", callback_data="play_casino", icon="TBOI_RED_D6_DIE", style="primary")
    btn3 = styled_btn("VIP Support", url="https://t.me/thatonearyan", icon="EDU_STAR")
    
    print("Button 1 dict:", btn1.model_dump(exclude_none=True))
    print("Button 2 dict:", btn2.model_dump(exclude_none=True))
    print("Button 3 dict:", btn3.model_dump(exclude_none=True))
    print("\n✅ Local demonstration complete!")


if __name__ == '__main__':
    local_demo()
