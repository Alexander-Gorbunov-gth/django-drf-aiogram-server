from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=["api"]))
async def handle_api_command(message: Message) -> None:
    if message.from_user is None:
        return

    await message.answer('Hello from "Api" app!')
