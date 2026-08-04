from semantic_router.routers import SemanticRouter
from semantic_router import Route
from semantic_router.encoders import HuggingFaceEncoder


encoder = HuggingFaceEncoder(
    name="BAAI/bge-small-en-v1.5"
)

faq = Route(
    name='faq',
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
    ]
)

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ]
)

smart_talk=Route(
    name='talk',
    utterances=[
        "How are you?"
        "What is your name?"
        "Are you a robot?"
        "What are you?"
        "What do you do?"
    ]
)
routes=[faq, sql,smart_talk]
router = SemanticRouter(routes=routes, encoder=encoder)
router.add(routes)

if __name__ == "__main__":
    print(router("").name)
    print(router("Do you offer international shipping?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)
    print(router("What do you do?").name)