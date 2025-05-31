import uuid
from datetime import datetime
from langchain.prompts import ChatPromptTemplate

def prompt_composer(system_prompt: str, human_prompt: str, variables: dict,
                    preview: bool = False, save_to: str = None, versioning: bool = False, return_mode="parsed") -> str:
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt)
    ])

    formatted_messages = prompt.format_messages(**variables)

    # Generate full prompt text
    full_prompt = "\n\n".join(
        f"{msg.type.upper()}:\n{msg.content}" for msg in formatted_messages
    )

    if preview:
        prompt.pretty_print()
        print("\n" + "-" * 80)
        print("\nPLACEHOLDERS:", prompt.input_variables)
        print("\n" + "-" * 80)
        print(full_prompt + "\n")

    if save_to:
        if versioning:
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_id = uuid.uuid4().hex[:8]
            base, ext = save_to.rsplit('.', 1)
            save_to = f"{base}_{now}_{unique_id}.{ext}"

        with open(save_to, "w", encoding="utf-8") as f:
            f.write(full_prompt)
        print(f"✅ PROMPT SAVED TO : {save_to}")

    if return_mode =="parsed":
      return prompt.invoke(variables)
    elif return_mode == "raw"
      return full_prompt
    else:
      raise ValueError("return_mode must be either 'parsed' or 'raw'")

## USAGE

system_prompt = "You are a helpful assistant with access to {tool_name}."
human_prompt = "Can you help me understand how to use {feature} in {tool_name}?"

bindings = {
    "tool_name": "tools_buffer",
    "feature": "auto-summarize"
}
prompt_composer(system_prompt, human_prompt, bindings, preview=True, save_to="full_prompt.txt", versioning=True)
