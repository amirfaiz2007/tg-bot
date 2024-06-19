from aiogram.types import Message, FSInputFile, PollAnswer

question = "вопрос"
options = ["вариант 1", "вариант 2"]
await message.answer_poll(question=question, options=options, is_anonymous=False)
await message.delete()


@router.poll_answer()
async def poll_answer(poll_answer: PollAnswer):
    answer_ids = poll_answer.option_ids
    print(answer_ids)