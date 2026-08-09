import uuid

from helper.runtime import run_agent
from mongodb.repository import find_chat_result, insert_chat_session, update_chat_message
from mongodb.schema import CategoryEnum, RoleEnum

NO_MATCHING_FAQ = "There is no matching FAQ."
NON_IT_ANSWER = "IT 헬프 데스크에서 처리할 수 없는 요청입니다."
AGENT_EXECUTION_ERROR_ANSWER = "요청 처리 과정에서 오류가 발생했습니다. 잠시 후 다시 시도해 주세요."
TICKET_CREATION_ERROR_ANSWER = "관련 FAQ를 찾지 못했고 문의 티켓도 생성하지 못했습니다. 잠시 후 다시 시도해 주세요."


def build_final_answer(category: str | None, ticket_id: str | None, tool_result: str | None) -> str:
    if ticket_id is not None:
        return (
            "관련 FAQ를 찾지 못해 IT 담당자에게 문의 티켓을 생성했습니다. "
            f"티켓 ID: {ticket_id}"
        )

    if tool_result is None:
        return AGENT_EXECUTION_ERROR_ANSWER

    if tool_result != NO_MATCHING_FAQ:
        return tool_result

    if category == CategoryEnum.NONIT:
        return NON_IT_ANSWER

    return TICKET_CREATION_ERROR_ANSWER


async def process_chat(question: str) -> tuple[str, str | None, str]:
    session_id = str(uuid.uuid4())

    await insert_chat_session(session_id, question)

    await run_agent(session_id, question)

    category, ticket_id, tool_result = await find_chat_result(session_id)

    final_answer = build_final_answer(category, ticket_id, tool_result)

    await update_chat_message(session_id, None, RoleEnum.AGENT, final_answer)

    return session_id, ticket_id, final_answer