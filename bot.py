from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import re
import os

TOKEN = os.getenv("BOT_TOKEN")

BAD_PATTERNS = [
    r"فردین\s*پور",
    r"فردینپور",
    r"فردین"
]

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg or not msg.text:
        return

    for p in BAD_PATTERNS:
        if re.search(p, msg.text):
            try:
                await msg.delete()
            except:
                pass

            await context.bot.send_message(
                chat_id=msg.chat.id,
                text="خودت روش کراش داری روت نمیشه منو میندازی وسط",
                reply_to_message_id=msg.message_id
            )
            break

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

app.run_polling()
