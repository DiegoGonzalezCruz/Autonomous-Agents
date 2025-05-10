from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


class Country(BaseModel):
    """Information about a country."""

    name: str = Field(description="The name of the country.")
    language: str = Field(description="The official language of the country.")
    capital: str = Field(description="The capital city of the country.")


structured_llm = llm.with_structured_output(Country)
response = structured_llm.invoke("Tell me about Chile")

print(response)
